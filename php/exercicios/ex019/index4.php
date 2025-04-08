<?php

// strict typing

//tambem pode ter o valor nulo.
//para isso usamos o ? antes do tipo de valor

declare(strict_types=1);

function falar(?string $mensagem){
    echo $mensagem;
}

falar('minha mensagem');
falar(null);        //tambem passa a ser possivel

//tambem podem ser defidos mais de um tipo para o mesmo argumento

function conversar(int|string $mensagem){
    echo $mensagem;
}

conversar('ola mundo');
conversar(2500);

//ou no caso de tipos de retorno

function calcular_quadrado_de(int|float $v1): int|float{
    return $v1 * $v1;
    // return 'joao';
}

echo calcular_quadrado_de(25);
// echo calcular_quadrado_de('joao');