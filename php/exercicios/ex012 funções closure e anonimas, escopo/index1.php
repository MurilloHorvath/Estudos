<?php

//escopo
//global

//neste exemplo a variavel $a existe em dois escopos diferentes

$a = 10;

function funcao(){
    //global $a //se usarmmos esse expressao o valor de a vai resgatar a expressao de fora da funcao
    $a = 20;
}

funcao();
echo "<p>$a</p>";

//outro exemplo

$b = 100;

function funcao2(){
    $b = 200;
    // $GLOBALS['b'] = 200;
}

funcao2();
echo "<p>$b</p>";