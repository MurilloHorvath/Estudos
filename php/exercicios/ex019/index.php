<?php

//type declarations 

//vejamos no caso de um array como parametro de uma função

function falar(array $mensagem){
    echo $mensagem;
}

falar('joao'); // não é possivel

//-----------------------------------

function conversar(string $mensagem){
    echo $mensagem;
}

//aqui var ser feito uma conversao de inteiro para string
conversar(2500);

// conversar(['a']); //não é possivel