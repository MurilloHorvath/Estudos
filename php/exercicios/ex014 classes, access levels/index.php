<?php

//constructor

class Humano5{
    public $nome;
    public $apelido;

    function __construct($n, $a){
        $this->nome = $n;
        $this->apelido = $a;
    }
}

//no php 8 podemos criar a mesma classe da seguinte forma

class Humano6{
    function __construct(public $nome, public $apelido){
        $this->nome = $nome;
        $this->apelido = $apelido;
    }
}




$h1 = new Humano5('joao', 'ribeiro');
$h2 = new Humano6('ana', 'martins');

echo $h1->nome . ' ' . $h1->apelido;
echo '<br>';
echo $h2->nome . ' ' . $h2->apelido;

//as classes sao case insentive(no caso nao é necessario escrevelas exetamente iguais) exemplo abaixo
$h3 = new humano5('nome', 'apelido');
echo '<br>';
echo $h3->nome . ' ' . $h3->apelido;