<?php

//operadores logicos

// &&, ||, and, or, xor

// os operadores logicos sao frequentemente usados com os operadores de comparação
//eles permitem 'ligar' varias comparações avaliando se sao verdadeiras ou falsas

// no php a construção correta de instruções condicionais depende destes operadores
// (instruções condicionais verificam se uma situação é verdadeira(true) ou falsa(false))

$a = 100;
$b = 200;

$x = ($a < $b) && ($a < 10000); // and -> true
$x = ($a > $b) || ($a > 10000); // or -> false
$x = ($a < 150) && ($b > 300); // false
$x = ($a > 10) || ($b > 500); //true
$x = ($a == 100) && ($b < $a); //false

$x = (10 > 5) && (20 > 30);
$x = (true && false); //false

$x = (2 > 1) && (3 > 2);
$x = (true && true); //true

$x = (2 < 4) || (4 > 10);
$x = (true || false); //true

$x = (2 == 3) || (3 > 1);
$x = (false || true); //true