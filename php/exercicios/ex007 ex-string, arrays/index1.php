<?php

$nome = 'Murillo';
$sobrenome = 'Horvath';
$nome_completo = "$nome $sobrenome";

?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercicio 2</title>
</head>
<body>
    <p>
        <?= "$nome $sobrenome"?>
    </p>
    <p>
        O meu nome tem 
        <?=strlen($nome_completo);?>
        caracteres.
    </p>
</body>
</html>