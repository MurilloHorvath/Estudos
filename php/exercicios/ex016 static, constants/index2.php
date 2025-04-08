<?php

//constants
//sao variaveis de valores inalteraveis

class circulo{
    const PI = 3.14;
}

//é possivel apresentar sem instanciar
echo circulo::PI;

echo '<br>';

// ou com instanciação
$c = new circulo();
echo $c::PI;