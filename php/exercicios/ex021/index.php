<?php

//verificar o tipo de variavel

//exemplos

$nome = 'meu nome';
$idade = '19';
$acordado = true;

if(is_array($nome)){
    echo 'é um array'; //nao vai aparecer
}

if(is_bool($acordado)){
    echo 'é um valor boleano'; //vai ser apresentado
}

/*
Outras funções similares
is_callable()
is_float() ou is_double()
is_real()
is_int() ou is_integer()
is_long()
is_null()
is_numeric()
is_object()
is_string()
*/