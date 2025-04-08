<?php

//funções

// parametros, conteudo dentro dos parenteses
//exemplo
function adicao($a,$b){
    //codigo executavel
}

adicionar(10,20);

function adicionar($a,$b){
    echo "$a + $b = " . ($a + $b);
}

echo '<br>';

//utilizando arrays

$nomes = ['joao', 'ana', 'carlos'];

foreach($nomes as $nome){
    saudacao($nome);
}

function saudacao($value){
    echo "Bom dia, $value.<br>";
}

//parametros opcionais

function multiplicar($a, $b = 2){
    //codigo executavel
    // $a sera o valor passado no argumento
    //$b sera o valor se ele for passado na chamada ou o valor 2 se nao for passado no argumento
    echo $a * $b;
}

multiplicar(4); // 4 * 2 = 8
echo '<br>';
multiplicar(10,20); // 10 * 20 = 200

//os parametros opcionais tem que ser definidos apos os parametros nao opcionais

function dividir($a=2,$b){
    echo '<br>';
    echo "$a e $b";
}

dividir(2,10);