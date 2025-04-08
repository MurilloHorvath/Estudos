<?php

// ciclos/loops

$x = 1;

while ($x < 10){
    echo 'ciclo em execução<br>';
    $x++;
}

echo '<hr>';

//outro exemplo

$i = 0;
while ($i < 10) {
    echo $i++ . '<br>';
}

echo '<hr>';

//exemplo sem as chaves

$i = 0;
while($i < 10) echo $i++ . '<br>';