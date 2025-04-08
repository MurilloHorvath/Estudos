<?php

//classes 
//constructor

class Humano1{
    private $nome;
    private $apelido;

    function __construct($n,$a){
        $this->nome = $n;
        $this->apelido = $a;
    }
    public function nomecompleto(){
        return $this->nome . ' ' . $this->apelido;
    }
}

$homem = new Humano1('joao', 'ribeiro');
$mulher = new Humano1('ana', 'martins');

echo $homem->nomecompleto();
echo '<br>';
echo $mulher->nomecompleto();

//classes que tem constructor sem parametros
//podemos instanciar da seguinte forma

class Humano2{
    function __construc(){
        //codigo executavel
    }
}

$homem = new Humano2;
// ou
$homem = new Humano2();