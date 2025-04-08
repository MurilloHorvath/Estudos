<?php

$valores = [10,20,30];

$valores[1] = 2000;

$valores[] = 3000;

array_push($valores, 5000);

echo 'Os valores são: ' . $valores[0] . ' e ' . $valores[1];

echo "<br>Os valores são: $valores[0] e $valores[1]";