<?php

// arrays

$valores = array(1,2,3,10,20,30);
$nomes = array('joao','ana','carlos');

// pode ser escrito dessa maneira 
// $valores = [1,2,3,10,20,30];
// $nomes = ['joao', 'ana', 'carlos'];

echo $valores[0];
echo $nomes[1];

$dados = [
    10 => 1000,
    20 => 2000,
    30 => 3000
];

$dados[] = 4000;