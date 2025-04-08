<?php

//parametros opcionais e named arguments

function adicionar($a, $b = 10, $c = 30){
    echo $a + $b + $c;
}

// no php 7 para alterarmos o valor de c teriamos que fornecer todos os valores

adicionar(100,10,300);

echo '<br>';

// no php 8 podemos fazer da seguinte forma:

adicionar(c: 1000,a:0);

echo '<br>';

adicionar(500,c:1000);