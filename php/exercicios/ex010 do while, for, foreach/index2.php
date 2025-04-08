<?php

//for

for($x = 1; $x < 10; $x++){
    echo $x . '<br>';
}

echo '<hr>';

//exemplo sem chaves
//utilizado apenas se for uma expressao

for($x = 1; $x < 10; $x++)
    echo $x . '<br>';


echo '<hr>';

//pode tambem ser escrito de uma
//forma diferente

$i = 1;
for (;$i < 10;){
    echo $i++ . '<br>';
}

echo '<hr>';

//pode contor mais de um paramentro
// separados por virgula

for($contador = 1, $x = 9; $contador < 10; $contador++, $x--){
    echo $x . '<br>';
}

echo '<hr>';

//por exemplo podemos mostrar todos
// os dados de um array

$nomes = ['joao', 'ana', 'carlos'];
for ($i = 0; $i < sizeof($nomes); $i++){
    echo $nomes[$i] . '<br>';
}