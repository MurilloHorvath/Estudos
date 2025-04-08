<?php

//access levels - niveis de acesso
// public, protected e private

class MinhaClasse{

    public $v1;
    protected $v2;
    private $v3;
}

$a = new MinhaClasse();
$a->v1 = '111'; //possivel
$a->v2 = '222'; //não é possivel. resulta em erro
$a->v3 = '333'; //não é possivel. resulta em erro




//public
//membros publics de uma classe, estão sempre acessiveis
// se criarmos um objeto a partir da classe, temos acesso direto a esses elementos

class tudopublico{
    public $propriedade;

    public function metodo(){
        echo 'metodo publico';
    }
}

$obj1 = new tudopublico();
$obj1->propriedade = 'a';
$obj1->metodo();



// protected
//um elemento protected pode ser alcançado dentro da classe
//e dentro de uma qualquer classe que seja uma extenção de outra classe

class classeteste{

    public $publica = "a";
    protected $protegida = "b";
    private $privada = "c";
}
class classederivada extends classeteste{
    function teste(){
        echo $this->publica;    //possivel
        echo $this->protegida;  //possivel
        echo $this->privada;    //erro
    }
}

$a = new classeteste();
$a->publica = "1";  //possivel
$a->protegida = "2";    //gera erro
$a->privada = "3";  //gera erro

$b = new classederivada();
$b->publica = "a";  //possivel
$b->protegida = "b";    //erro
$b->privada = "c";  //erro



//private
//so pode ser visivel dentro da propria classe
//nao é visivel nos objetos instanciados nem noutras classes herdadas.

class teste{
    private $valor ='a';

    function mover(){
        echo $this->valor;
    }
}

$a = new teste();
$a->mover();    //possivel