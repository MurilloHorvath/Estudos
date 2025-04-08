<?php

//break, continue e goto

// break 
// serve para interromper a execução de um loop

for($i = 0; $i < 20; $i++){
    echo $i . '<br>';
    if($i==10){
        break;//interrompe o loop
    }
}

echo '<hr>';

$nomes = ['joao', 'ana', 'carlos'];
foreach($nomes as $nome){
    echo $nome . '<br>';
    if($nome == 'ana'){
        break;
    }
}

echo '<hr>';

// continue
// permite avançar uma volta do ciclo ignorando o codigo que deveria ser executado

for($i = 0; $i < 20; $i++){
    if($i==10){
        continue; //volta a linha inicial do loop
    }
    echo $i . '<br>';
}

echo '<hr>';

$nomes = ['joao', 'ana', 'carlos'];
foreach($nomes as $nome){
    if($nome == 'ana'){
        continue;
    }
    echo $nome . '<br>';
}

echo '<hr>';

//  goto
//pouco usado... muito complexo a leitura
//permite sair do loop e ir para uma linha do codigo 
//definida por um label(nome seguido de :)

for ($i = 0; $i <20; $i++){
    if($i==10){
        goto teste; //vai pular par o label(teste)
    }
    echo $i.'<br>';
}

echo 'fim do loop';

teste:
echo 'aqui';