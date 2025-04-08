<?php

//podemos comparar strings da seguinte forma;

$a = 'Joao';
$b = 'Carlos';

$c = ($a == $b); //false
$d = ($a != $b); //true

//existem muitas funções nativas no php para operar com strings

//exemplos:

$frase = 'esta frase tem 29 caracteres.';

//retorna o numero de caracteres da string
$numero_caracteres_total = strlen($frase);

//retorna as letras a partir da posição 0 e durante 4 caracteres
$primeira_palavra = substr($frase, 0, 4); 
//esta

//converte toda a string em letras maiusculas
$todas_maiusculas = strtoupper($frase);

//converte em letras minusculas
$todas_minusculas = strtolower($frase);

//substituir uma letra por outra
$nova_frase = str_replace('a', 'x', $frase);
//estx frxse tem 29 cxrxcteres.

//verifica qual é a poisição de um caracter dentro da string
$posicao = strpos($frase, 'a'); // 3
