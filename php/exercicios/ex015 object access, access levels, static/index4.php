<?php

//static

//a palavra chave static pode ser usada para declarar propriedades e metodos de uma classe
//que podem ser acedidos sem que seja necessario criar um objeto a partir dessa classe.

class teste{

    // instance members - um membro por cada objeto criado a partir da classe
    public $nome;
    function teste(){
        //codigo
    }

    //static ou class members - apenas existentes uma vez na classe
    static $idade;
    static function mover(){
        //codigo
    }
}