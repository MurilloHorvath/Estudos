<?php

//null coalescing operator

/*
basicamente este operador é um atalho para alguns casos do operador
condicional ternário.
*/

$x = null;
$nome = $x ?? 'sem nome';

// este exemplo é semelhante a:

$nome1 = isset($x) ? $x : 'sem nome';

//portanto se x for null, entao é atribuido o valor definido
//a frente dos dois sinais de interrogação

//existe uma maneira mais simples para definir variaveis nulas ou sem valor atribuido

$apelido = null;
$apelido ??= 'apelido desconhecido.';

echo $nome;
echo '<br>';
echo $apelido;