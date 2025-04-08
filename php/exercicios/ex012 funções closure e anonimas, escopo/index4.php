<?php

//funções closure

$x = 20;
$y = 30;

$minhaclosure = function($z) use($x, $y){
    echo "$z - $x - $y";
    $y += 1000; //esta instrução nao vai altera o valor de $y
};

$minhaclosure(10);

echo "<p>$y</p>"; //o valor de $y nao foi alterado na closure




//arrow functions
//capturam automaticamente as variaveis globais
$x = 20;
$y = 30;

$minhafuncao = fn($z) => "$x - $y - $z";

echo $minhafuncao(10);

//usam a palavra reserva fn e nao precisam de chaves...
