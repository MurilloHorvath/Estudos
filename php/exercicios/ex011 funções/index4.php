<?php

// return

function falar(){
    return;
    echo 'nao vai ser apresentado este texto';
}

function adicionar($a, $b){

    $resultado = $a + $b;
    return $resultado;
    // ou 
    return $a + $b;
}

echo adicionar(10,20);//vai aparecer 30...

// outro exemplo

$nome = 'joao';
if(avaliar_nome($nome)){
    echo 'O cliente esta correto.';
}

function avaliar_nome($n){
    if($n == 'joao'){
        return true;
    }else{
        return false;
    }
}

//uma função sem qualquer valor de retorno, devolve sempre um valor null

function teste(){
    //codigo executavel
}

if(falar() === null){
    echo 'função com returno igual a nulo.';
}