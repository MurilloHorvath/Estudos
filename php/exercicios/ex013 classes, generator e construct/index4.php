<?php

//construct

//exemplos

class Humano3{
    public $nome;
    public $apelido;
}

class Humano4{
    public function falar(){
        //codigo executavel
    }
    private function andar(){
        //metodo apenas acessivel dentro da class
    }
    public function movimento(){
        $this->andar();
    }
}

//podemos ter classes sem qualquer tipo de metodo e podemos ter classes sem qualquer tipo de propriedades

$homem = new Humano3();
$homem->nome = 'joao';
$homem->apelido = 'ribeiro';

$mulher = new Humano4();
$mulher->movimento();