#include <Wire.h> 
#include <LiquidCrystal_I2C.h> 
#include <ESP8266WiFi.h> 
#include <BlynkSimpleEsp8266.h> 
#include <TimeLib.h> 
#include <WiFiUdp.h> 
#include <SPI.h> 

LiquidCrystal_I2C lcd(0x27, 16, 2); 
#define DS1307_ADDRESS 0x68 
#define BLYNK_PRINT Serial 

int pressurizador =0;   //PINO VIRTUAL QUE CONTROLA O RELÉ DO MOTOR DO PESSURIZADOR 
int motorblynk = 0;     //PINO VIRTUAL QUE CONTROLA O RELÉ DO MOTOR DA MOTOBOMBA 
const int nivel_sensor_max = 13; //PINO DIGITAL EM QUE O SENSOR DE NÍVEL MÁXIMO ESTÁ CONECTADO 
const int rele_bomba_dagua = 14; //PINO DIGITAL EM QUE O MÓDULO RELÉ 5V ESTÁ CONECTADO 
const int controle_manual = 12;  //PINO DIGITAL EM QUE O MÓDULO RELÉ 5V ESTÁ CONECTADO 
byte leitura_nivel_max = 0;      //VARIÁVEL ÁRA ARMAZENAR A LEITURA DO SENSOR  
byte leitura_botao_manual = 0;   //VARIÁVEL ÁRA ARMAZENAR A LEITURA DO BOTÃO DE CONTROLE MANUAL 
char auth[] = "-ic0r3pyA*******************";   // LOGIN NO SERVIDOR DO APP BLYNK 
char ssid[] = "xxxxxxxxxxx";    // LOGIN NO WI-FI 
char pass[] = "xxxxxxxxxx";     // SENHA DO WI-FI 
static const char ntpServerName[] = "us.pool.ntp.org"; 
const int timeZone = -3;    // Central European Time 
WiFiUDP Udp; 
unsigned int localPort = 8888;  // local port to listen for UDP packets 
time_t getNtpTime(); 
void digitalClockDisplay(); 
void printDigits(int digits); 
void sendNTPpacket(IPAddress &address);

void setup(){ 
lcd.begin();    // INICIA A COMUNICAÇÃO COM O DISPLAY 
lcd.backlight();    // LIGA A ILUMINAÇÃO DO DISPLAY 
lcd.clear();    // LIMPA O DISPLAY 
Serial.begin(9600); // inicializa a porta serial 
pinMode(nivel_sensor_max, INPUT);  //DEFINE O PINO COMO ENTRADA 
pinMode(controle_manual, INPUT);   //DEFINE O PINO COMO ENTRADA 
pinMode(rele_bomba_dagua, OUTPUT); //DEFINE O PINO COMO SAÍDA 
Blynk.begin(auth, ssid, pass);  // FAZ A AUTENTIFICAÇÃO DO APLICATIVO BLINK NO SERVIDOR 
WiFi.begin(ssid, pass);           
Udp.begin(localPort); 
setSyncProvider(getNtpTime); 
setSyncInterval(300); 
pinMode(1,INPUT); 
} 

BLYNK_READ(V0){ Blynk.virtualWrite(V0, millis() / 1000);}   // FAZ A AUTENTIFICAÇÃO DA INTERNET VIA WI-FI   
BLYNK_READ(V1) {Blynk.virtualWrite(V1, millis());} 
time_t prevDisplay = 0; 

void loop() 
{ 
Blynk.run(); 
lcd.clear(); 
lcd.setCursor(0,0); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 2 COLUNA 1) 
lcd.print(">>VERIFICANDO<<"); //ESCREVE "VERIFICANDO" NA SEGUNDA LINHA DO DISPLAY LCD 
lcd.setCursor(0,1); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 2 COLUNA 1) 
lcd.print("   SENSORES  "); //ESCREVE "SENSORES" NA SEGUNDA LINHA DO DISPLAY LCD 
delay(1500);    //INTERVALO DE 1,5 SEGUNDOS 
leitura_nivel_max = digitalRead(nivel_sensor_max); //VARIÁVEL RECEBE O VALOR LIDO NO SENSOR  
leitura_botao_manual = digitalRead(controle_manual); //VARIÁVEL RECEBE O VALOR LIDO NO BOTÃO MANUAL 
motorblynk = digitalRead(1); 

if((hour()22 && minute()>00)&&(hour()<9 && minute()>00)){   //DEFINE UM HORÁRIO PERMITIDO PARA QUE OS MOTORES TRABALHEM.  
lcd.clear();  //LIMPA DISPLAY 
lcd.print("HORA DE SILENCIO");  //ESCREVE "HORA DE SILENCIO" NO DISPLAY LCD      
lcd.setCursor(0,1);  
lcd.print(hour()); 
lcd.print(":"); 
lcd.print(minute()); 
lcd.setCursor(0,1); 
lcd.print("MOTOR DESLIGADO ");  //ESCREVE "MOTOR DESLIGADO" NO DISPLAY LCD 
digitalWrite(rele_bomba_dagua, LOW);  //DESATIVA RELE DA MOTOMOMBA 
delay(1500);

}else{  
if(leitura_botao_manual == HIGH){   // SE BOTÃO MANUAL ESTIVER DESATIVADO/ ABERTO  --- DESLIGA A BOMBA 
lcd.clear();  //LIMPA DISPLAY 
lcd.setCursor(0,0); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 1 COLUNA 1) 
lcd.print("BOTAO EMERGENCIA ");  //ESCREVE "BOTÃO DE EMERGENCIA" NO DISPLAY LCD 
lcd.setCursor(0,1); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 2 COLUNA 1) 
lcd.print("TRAVA ATIVA ");   //ESCREVE "TRAVA ATIVA" NO DISPLAY LCD        
digitalWrite(rele_bomba_dagua, LOW); //DESATIVA RELE DA MOTOMOMBA 
delay(1500);    //INTERVALO DE 1,5 SEGUNDOS    

}else if(motorblynk == LOW) { 
lcd.clear();  //LIMPA DISPLAY 
lcd.setCursor(0,0); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 1 COLUNA 1) 
lcd.print("CONTROLE POR APP "); //ESCREVE "CONTROLE POR APP" NO DISPLAY LCD     
lcd.setCursor(0,1); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 2 COLUNA 1) 
lcd.print("MOTOR DESATIVADO "); //ESCREVE "MOTOR DESATIVADO" NA SEGUNDA LINHA DO DISPLAY LCD 
digitalWrite(rele_bomba_dagua, LOW);  //DESATIVA RELE DA MOTOMOMBA 
delay(1500);    //INTERVALO DE 1,5 SEGUNDOS  

}else if(leitura_nivel_max == HIGH){    //HIGH = NÃO TEM AGUA, LOW = TEM AGUA 
lcd.clear(); //LIMPA DISPLAY 
lcd.setCursor(0,0); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 1 COLUNA 1) 
lcd.print("STATUS:");    //ESCREVE "STATUS"  DO DISPLAY LCD              
lcd.setCursor(0,1); //SETA A POSIÇÃO EM QUE O CURSOR RECEBE O TEXTO A SER MOSTRADO(LINHA 2 COLUNA 1) 
lcd.print("* MOTOR ATIVO * ");  //ESCREVE "ENCHENDO" NA SEGUNDA LINHA DO DISPLAY LCD 
digitalWrite(rele_bomba_dagua, HIGH);   //ATIVA RELE DA MOTOMOMBA 
delay(1500);    //INTERVALO DE 1,5 SEGUNDOS 
}}} 

//*********************************************************************************************** 
const int NTP_PACKET_SIZE = 48; // NTP time is in the first 48 bytes of message 
byte packetBuffer[NTP_PACKET_SIZE]; //buffer to hold incoming & outgoing packets 
time_t getNtpTime() 
{ 
IPAddress ntpServerIP; // NTP server's ip address 
while (Udp.parsePacket() > 0) ; // discard any previously received packets 
Serial.println("Transmit NTP Request"); 
// get a random server from the pool 
WiFi.hostByName(ntpServerName, ntpServerIP); 
Serial.print(ntpServerName); 
Serial.print(": "); 
Serial.println(ntpServerIP); 
sendNTPpacket(ntpServerIP); 
uint32_t beginWait = millis(); 
while (millis() - beginWait < 1500) { 
int size = Udp.parsePacket(); 
if (size >= NTP_PACKET_SIZE) { 
Serial.println("Receive NTP Response"); 
Udp.read(packetBuffer, NTP_PACKET_SIZE);  // read packet into the buffer 
unsigned long secsSince1900; 
// convert four bytes starting at location 40 to a long integer 
secsSince1900 =  (unsigned long)packetBuffer[40] << 24; 
secsSince1900 |= (unsigned long)packetBuffer[41] << 16; 
secsSince1900 |= (unsigned long)packetBuffer[42] << 8; 
secsSince1900 |= (unsigned long)packetBuffer[43]; 
return secsSince1900 - 2208988800UL + timeZone * SECS_PER_HOUR; 
} 
20 
} 
Serial.println("No NTP Response :-("); 
return 0; // return 0 if unable to get the time 
} 
// send an NTP request to the time server at the given address 
void sendNTPpacket(IPAddress &address) 
{ 
// set all bytes in the buffer to 0 
memset(packetBuffer, 0, NTP_PACKET_SIZE); 
// Initialize values needed to form NTP request 
// (see URL above for details on the packets) 
packetBuffer[0] = 0b11100011;   // LI, Version, Mode 
packetBuffer[1] = 0;    
 // Stratum, or type of clock 
packetBuffer[2] = 6;     
// Polling Interval 
packetBuffer[3] = 0xEC;  // Peer Clock Precision 
// 8 bytes of zero for Root Delay & Root Dispersion 
packetBuffer[12] = 49; 
packetBuffer[13] = 0x4E; 
packetBuffer[14] = 49; 
packetBuffer[15] = 52; 
// all NTP fields have been given values, now 
// you can send a packet requesting a timestamp: 
Udp.beginPacket(address, 123); //NTP requests are to port 123 
Udp.write(packetBuffer, NTP_PACKET_SIZE); 
Udp.endPacket(); 
} 
