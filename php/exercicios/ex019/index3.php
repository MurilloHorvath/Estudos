<?php

//strict typing

//o comportamento do php é tentar converter os tipos declarados

function falar(string $mensagem){
    echo $mensagem;
}

falar('Olá Mundo');     //é possivel
falar(2500);            //é possivel

function somar(int $v1, int $v2){
    return $v1 + $v2;
}

echo somar(10,20);      //é possivel
echo somar('a','b');    //é possivel

// mas podemos 'obrigar' o PHP a seguir a regra definida

// declare(strict_types=1); //esta declaração tem que ser a primeira a ser apresentada no script