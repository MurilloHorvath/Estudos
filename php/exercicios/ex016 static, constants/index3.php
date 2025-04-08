<?php

const APP_NAME = 'aplicativo';
echo APP_NAME;

echo '<br>';

//dentro de uma funcao
function teste(){
    echo APP_NAME;
}

teste();

//nao é possivel concatenar constantes da mesma forma que fizemos com variaveis
echo "<br>nome: {APP_NAME}";


//tem que ser dessa maneira
echo "<br>Nome: " . APP_NAME;