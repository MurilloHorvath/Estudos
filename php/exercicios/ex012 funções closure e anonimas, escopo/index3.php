<?php

//funções anonimas

$a = function(){
    echo '<p>ola</p>';
};

$a();//ao executar esse variavel... a funcao acima sera executada

//outro exemplo

$falar = function($mensagem){
    echo "<p>eu digo: $mensagem</p>";
};

$falar('Estou aqui');

//outro exemplo

$andar = function($metros){
    return "Andei $metros metros";
};

echo $andar(100);

//outro exemplo

$a = function(){
    return '<p>funcao a</p>';
};

function falar($x){
    echo $x;
}

falar($a());