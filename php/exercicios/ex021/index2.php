<?php

//var_dump

/*
Tem um resultado semlhante ao print_r, mas para alem dos valores
apresenta tambem a informação sobre o tipo de valores.
*/

echo '<pre>';

$nome = 'joao';
var_dump($nome);

echo '<br>';

$valores = [1,2,3];
var_dump($valores);