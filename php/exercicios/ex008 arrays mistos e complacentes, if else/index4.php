<?php

$numero = 20;
if($numero > 10 && $numero != 30){
    //ação
}else{
    //ação
}

$numero = 10;
if($numero >= 0){
    if($numero >= 100){
        echo 'O numero é igual ou maior que 100';
    }else{
        echo 'O numero é positivo, mas inferior que 100';
    }
} else {
    echo 'O numero é negativo.';
}