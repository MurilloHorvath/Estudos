<?php

//classes abstratas

/*
Uma classe abstrata é constituida por uma implementação parcial
a partir das quais outras classes podem crescer.

Quando uma classe é declarada como abstrata, isso significa que ela tem 
métodos incompletos que, obrigatoriamente tem que ser implementados nas
classes que a herdam

As classes abstratas nao podem ser instanciadas. servem apenas para
poderem ser herdadas por outras classes.
*/

abstract class Forma{

    public $largura = 100;
    public $altura = 200;

    abstract public function area();

    function altura(){
        return $this->altura;
    }
}

// $quadrado = new Forma(); //isso nao é permitido

class Retangulo extends Forma{

    public function area(){
        return $this->largura * $this->altura;
    }
}

$r = new Retangulo();
echo $r->area();
echo '<br>';
echo $r->altura();