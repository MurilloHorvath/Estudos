<?php

//var_export
/*
Apresenta informação sobre uma variavel num estilo que pode
ser usado como codigo php.
*/

$nome = 'joao';
var_export($nome);

echo '<br>';

$valores = [1,2,3];
var_export($valores);

echo '<br>';

$numeros = [];
for($i=0; $i<10; $i++){
    $numeros[]=rand(0,100);
}

var_export($numeros);