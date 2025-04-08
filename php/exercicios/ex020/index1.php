<?php

// testando variaveis

// isset
/*
esta construção permite verificar se uma variavel esta ou não definida
ela retorna verdadeiro se a variavel existe, a false se nao existe.
*/

$a = 1;
if(isset($a)){
    echo 'Variavel existe<br>';
} else {
    echo 'Variavel nao existe<br>';
}

//se tivermos uma variavel definida, mas o seu valor for null, é considerado como uma variavel inexistente.

$b = null;
echo isset($b) ? 'sim' : 'nao';


// empty
/*
Verifica se a variavel tem um valor vazio(null,0, false ou string vazia)
e retorna verdadeiro ou falso
*/

$b = 'joao';
empty($b); //false

$c = false;
empty($c);  //true

$nomes = [];
empty($nomes); //true

$outro = null;
empty($outro); //true