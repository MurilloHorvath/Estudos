<?php

//foreach

//ciclo para ter uma iteração com os valores do array

$nomes = ['joao', 'ana', 'carlos'];
foreach($nomes as $nome){
    echo $nome . '<br>';
}

echo '<hr>';

//outro modo que permite buscar a chave e o valor do array

$capitais = [
    'brasil' => 'Brasilia',
    'portugal' => 'Lisboa',
    'espanha' => 'Madrid'
];

foreach($capitais as $key => $value){
    echo "Para o país $key a capital é $value<br>";
}