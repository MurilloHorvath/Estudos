<?php

// type conversions

//uma variavel do tipo int não é o mesmo que uma string e vice-versa

$meu_boleano = true;
echo $meu_boleano; // resulta numa string vazia.
//echo (int)$meu_boleano;

/* 
designamos esta operação como convesao explicita (explicit cast)
podemos fazer converter os principais tipos de valores
(string), (int), (float), (array), etc.

vejamos o caso da conversão de um array num objeto
*/

$nomes = [
    'joao',
    'ana',
    'carlos'
];

$nomes1 = (object)$nomes;
echo '<pre>';
print_r($nomes1);

//por exemplo, podemos converter uma variavel num array com um unico valor
$nome = "joao";
$os_nomes = (array)$nome;
print_r($os_nomes);