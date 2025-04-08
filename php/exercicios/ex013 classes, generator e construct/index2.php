<?php

//classes

class Humano{
    public $nome = 'Joao';
    public $apelido = 'Ribeiro';

    public function nomeCompleto(){
        return $this->nome . ' ' . $this->apelido;
    }
}

//instanciar um objeto

$homem = new Humano();

echo $homem->nomeCompleto();