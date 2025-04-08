<?php

//concatenação de strings
//é o processo que, atraves do codigo, permite juntar varias strings.
//existem dois operadores de concatenação

// .
// .=

$a = 'Joao' . ' ' . 'Ribeiro';  //o ponto liga as diferentes strings
$b = 'Joao';
$b .= ' ' . 'Ribeiro';          // .= faz uma concatenação com o valor ja existente na string

echo $b;
echo '<br>';

$nome = 'Murillo';
$apelido = 'Silveira';
$nome_completo = $nome . ' ' . $apelido;

echo $nome_completo;
die();