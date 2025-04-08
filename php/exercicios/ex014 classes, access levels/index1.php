<?php

// herança de classes

//exemplo classe base
class Animais{
    public $especie;
    public $peso;

    function tipoEspecie(){
        return "Este animal é da espécie{$this->especie}";
    }
}


//exemplo classe herença
class Mamifero extends Animais{
    //não é necessario voltar a definir
    //as propriedades e metodos que ja exeistem na classe base

    //podemos acrescentar outras propriedades e outros metodos
    public $quantidade_pernas;
    public $tem_pelo;

    function temQuantasPernas(){
        return "O animal da espécie {$this->especie} tem {$this->quantidade_pernas}";
    }
}

$mamifero = new Mamifero();
$mamifero->especie = 'cavalo';
$mamifero->quantidade_pernas = 4;
echo $mamifero->temQuantasPernas();