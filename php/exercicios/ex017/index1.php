<?php

//constantes magicas

//as constantes magicas sao 8 e sao designadas assim porque
// o seu valor varia automaticamente dependendo onde estao a ser usadas
// vamos perceber como funcionam

echo __LINE__ . '<br>'; //indica o numero da linha de codigo no script.
echo __FILE__ . '<br>'; //indica o caminho completo do script.
echo __DIR__ . '<br>'; //indica a pasta onde o script esta alojado.

teste();
function teste(){
    $a = true;
    echo __FUNCTION__ . '<br>'; //indica o nome da funcao
}

class MinhaClasse{
    function identificar(){
        echo __CLASS__ . '<br>'; // indica o nome da classe
        echo __METHOD__ . '<br>'; // indica o noe do metodo
    }
}

$a = new MinhaClasse();
$a->identificar();

// __TRAIT__ esta relacionado com um mecanismo de reutilização de codigo

echo __NAMESPACE__; // indica o nome do namespace atual