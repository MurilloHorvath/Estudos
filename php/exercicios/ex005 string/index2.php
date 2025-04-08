<?php

//a diferença entre strings delimitadas por ' e por " é que, no segundo caso,
// podemos fazer o seguinte:

$nome = 'João';
$apelido = 'Ribeiro';
$nome_completo = "$nome $apelido";

echo $nome_completo;

//ao contrario das ", nas string ' as variaveis nao sao interpretadas
// relativamente ao seu valor(parse)