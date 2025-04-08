<?php

//uma função nunca pode ser chamada sem que os valores obrigatoorios sejam fornecidos

//exemplo:

function funcao($a,$b){
    //codigo executavel
}

// funcao('teste');
//isso é errado.. apenas o valor de $a foi fornecido


//podemos passar tambem mais argumentos do que o solicitado

function outrafuncao($a){

    echo "$a<br>";

    $x = func_get_arg(0);
    $y = func_get_arg(1);
    $z = func_get_arg(2);
    echo "$x - $y - $z";

    echo '<br>';

    echo func_num_args(); // avalia quantos argumentos foram passados para a função
}

outrafuncao(10,20,30);

echo '<br>';


//pode ser utilizado um argumento especial
//designado por variadic parameter

function minhafuncao(...$argumentos){
    foreach($argumentos as $v){
        echo "$v<br>";
    }
}

minhafuncao(10,20,30,40,50);