<?php

// do while

$x = 0;
do {
    echo $x++ . '<br>';
} while ($x < 10);

echo '<hr>';

//modo sem utilizar as chaves
//apenas para uma expressao

$x = 0;
do
    echo $x++ . '<br>';
while($x < 10);

echo '<hr>';

// ou

$x = 0;
do echo $x++ . '<br>'; while($x < 10);