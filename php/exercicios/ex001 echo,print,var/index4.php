<?php

//variaveis
//definem se com um $ + um identificador(no caso o nome da variavel)
//$varivel;

// podemos definir e iniciar uma variavel
//  $variavel = 100;

// podemos alterar o tipo de valores de uma variavel
//  $variavel = 'teste';

// as variaveis sao case sensitive
// $varivel = 'uma variavel';
// $Variavel = 'outra variavel';

// forma errada
// $1var = 0;
// $!var = 0;
// $variavel(1) = 0;
// $variavel um = 0;
// $variavel-um= 0;

// forma correta
$var1 = 0;
$var_um = 0;
$varum = 0;
$_um = 0;
$_1 = 0;

// convençoes
$umaVariavel = 0; //camel case
$uma_variavel = 0; //com undersores (snake case)
$UmaVariavel = 0; //studly case (não recomendado)

//deve ser sempre mantido o mesmo estilo ao longo do projeto
$variavel = 100;
echo $variavel;