function carregar(){
var msg = window.document.getElementById('msg')
var img = window.document.getElementById('imagem')
var data = new Date()
var hora = data.getHours()


msg.innerHTML = `Agora são ${hora} Horas`
if (hora >= 0 && hora < 12){
    //img bom dia
    img.src = 'imagens/manha.png'
    document.body.style.background = '#F27405'
}else if(hora >= 12 && hora <= 18){
    //img tarde
    img.src = 'imagens/tarde.png'
    document.body.style.background = '#225473'
}else{
    //img noite
    img.src = 'imagens/noite.png'
    document.body.style.background = '#403231'
}
}