<?php

$dados = [
    [10,20,30,40],
    [100,200,300,400],
    [1000,2000,3000,4000]
];

echo $dados[1][2];
echo '<br>';
echo $dados[0][3];

$estados = [
    'brasil' => ['Rio Grade do Sul', 'São Paulo', 'Rio de Janeiro'],
    'portugal' => ['Lisboa', 'Porto', 'Coimbra'],
    'espanha' => ['Madrid', 'Barcelona', 'Servilha']
];

echo '<br>';
echo $estados['brasil'][0];
echo '<br>';
echo $estados['portugal'][1];
echo '<br>';
echo $estados['espanha'][2];
