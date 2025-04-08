<?php

// class
// final
// para impedir que uma classe derivada possa fazer override de metodos

class Veiculo{

    function mover(){
        //codigo executavel
    }
}

class bicicleta extends Veiculo{

    function mover(){
        // override do codigo original
    }
}

//pode se definir uma classe como nao sendo passivel de ser herdada
//colocando FINAL antes de class

class humano{
    //codigo
    function teste(){
        echo 'teste';
    }
}

class Homem extends humano{
    //codigo aqui
}

$a = new homem();
$a->teste();