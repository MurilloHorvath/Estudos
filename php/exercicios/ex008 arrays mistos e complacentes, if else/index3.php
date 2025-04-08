<?php

$nome = 'murillo';
if($nome == 'murillo'){
    echo 'Foi identificado o nome.';
}

echo '<br>';

$idade = 18;
if($idade <= 18){
    echo 'Adolescente';
}else{
    echo 'Adulto';
}

echo '<br>';

$nota = 5;
if($nota <= 2){
    echo 'Nota Fraca';
} elseif($nota <= 4){
    echo 'Nota Insufisiente';
} elseif($nota <= 6){
    echo 'Nota Positiva';
} elseif($nota <= 8){
    echo 'Nota Muito Positiva';
} else{
    echo 'Nota Excelente';
}

echo '<br>';
// se for apresentado apenas uma instrução nao precisa das chaves

if($nota <= 2)
    echo 'Nota Fraca';
elseif($nota <= 4)
    echo 'Nota Insufisiente';
elseif($nota <= 6)
    echo 'Nota Positiva';
elseif($nota <= 8)
    echo 'Nota Muito Positiva';
else
    echo 'Nota Excelente';

echo '<br>';
// pode ser usados os dois modos ao mesmo tempo...

if($nota <= 2)
    echo 'Nota Fraca';
elseif($nota <= 4)
    echo 'Nota Insufisiente';
elseif($nota <= 6){
    echo 'Nota Positiva';
    echo '<br>';
    echo 'Sua nota está na media';
}elseif($nota <= 8)
    echo 'Nota Muito Positiva';
else
    echo 'Nota Excelente';

