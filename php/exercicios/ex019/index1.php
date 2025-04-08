<?php

// type declarations

// callable
//o tipo callable tem que ser uma função, metodo ou objeto
//podemos, por exemplo, usar uma funcao anonima

$falar = function($mensagem){echo 'A minha mensagem é ' . $mensagem;};

function minha_funcao(callable $funcao, $dados){
    $funcao($dados);
}

minha_funcao($falar, 'Esta é a minha mensagem.');