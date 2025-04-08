<?php

class operacoes{

    //retorna um numero sorteado entre $min e $max
    static function numeroaleatorio($min,$max){
        return rand($min,$max);
    }

    static function calculaformula($a,$b){
        //(a x 2) + (b x a)
        return ($a*2)+($b*$a);
    }

    static function criarnome(){

        $nomes = ['joao', 'ana', 'carlos', 'francisco', 'rui', 'nuno'];
        $apelidos = ['silva', 'almeida', 'santos', 'rodrigues', 'oliveira'];
        return $nomes[rand(0,count($nomes)-1)] . ' ' . $apelidos[rand(0,count($apelidos)-1)];
    }
}

echo operacoes::numeroaleatorio(1111,9999);
echo '<br>';
echo operacoes::calculaformula(10,20);
echo '<br>';
echo operacoes::criarnome();