<?php

//escopo e ciclo de vida de uma variavel

$variavel = 10;

echo "<p>$variavel</p>";

funcao(20,30);
echo "<p>$a e $b</p>";//estas variaveis so existem dentro da função, mas nao existem fora...
function funcao($a,$b){
    echo "<p>$variavel</p>";//variavel desconhecida
    echo "<p>$a e $b</p>";
}

function funcao2(){
    $v = 100;
}

funcao2();
echo "<p>$v</p>";

