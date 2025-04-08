<?php

$dados = [
    'A' => 20,
    'B' => 30,
    'C' => 40,
    'D' => 50,
    'E' => 60
];

// ou

$dados = [
    'nome' => 'murillo',
    'email' => 'murillo@gmail.com',
    'nacionalidade' => 'Brasileiro',
    'telefone' => '999999999'
];

// não se deve existir duas chaves iguais

$dados = [
    'nome' => 'murillo',
    'nome' => 'carlos'
];

echo $dados['nome'];