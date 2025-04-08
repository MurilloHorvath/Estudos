<?php

// caracteres de escape

echo '<p>Este é um paragrafo de HTML</p>';
echo '<br>';

// os caracteres de escape sao usados para escrever caracteres especiais,
// como é o caso de alguns simbolos que podem entrar em conflito com o codigo.

$frase_1 = 'I'm going to John's party!';
$frase_2 = "I'm going to John's party!";

$frase_3 = "I'm not sure John "The great" will win this fight";

// a \ é o simbolo para definir um caractere de escape

$frase_1 = 'I\'m going to John\'s Party!';

$frase_3 = 'I\'m not sure John "The great" will win this fight.';
$frase_3 = "I'm not sure John \"The great\"will win this fight";