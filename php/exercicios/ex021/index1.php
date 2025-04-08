<?php

//apresentaçã de informações de variaveis
/*
    print_r
    var_dump
    var_export
*/

//print_r
/*
Permite ver dados de uma variavel de uma forma simples de ler.
é frequentemente usada para efeitos de debug.
*/

echo '<pre>';
$a = 'joao';
print_r($a);
echo '<br>';
$b = [1,2,3];
print_r($b);