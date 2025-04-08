<?php

//object access

// no php, um objeto instanciado a partir de uma classe
// pode aceder a elementos privados e protegidos de outro objeto
//criado a partir da mesma classe.
//este comportamento nao acontece na maior parte das linguagens de programação.

class humano{

    private $nome = 'x';

    function setprivate($objeto,$valor){
        $objeto->nome = $valor;
    }
    function apresentar(){
        echo $this->nome;
    }
}

$a = new humano();
$b = new humano();
$a->setprivate($b,'joao');

$a->apresentar();
echo '<br>';
$b->apresentar();