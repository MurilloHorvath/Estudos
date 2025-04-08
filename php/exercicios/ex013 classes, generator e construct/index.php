<?php

//generetors
//permite gerar series de valores
//cada valor é devolvido pela função atraves da expressao yield
//diferente do return o yield continua do estado onde ficou na ultima chamada


function buscarnumero(){
    for($i = 0; $i < 10; $i++){
        yield $i;
    }
}

// a funcao generators funciona como um iterador, podebdo ser usada num ciclo
//ate que o gerador nao tenha mais valores para devolver com yield

foreach(buscarnumero() as $numero){
    echo "$numero<br>";
}

//introdução do yield from
//devolver valores de outro gerador
//devolver valores de um array

function buscarnomes(){
    yield 'joao';
    yield 'maria';
    yield from ['carlos', 'ana', 'antonio'];
    yield 'fernando';
}

echo '<hr>';
foreach(buscarnomes() as $nome){
    echo "$nome<br>";
}