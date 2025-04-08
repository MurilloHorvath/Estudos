<?php

//importar scripts com include


// primeiro modo de incluir um script
//com o script estando na mesma pasta

include 'config.php';

//esta instrução vai inserir o docdigo de programação de script config.php
// dentro do script atual.

// segundo metodo 
//incluir o script que esta dentro de uma pasta

include 'inc/dados.php';

//terceiro metodo
//quando é necessario voltar uma pasta para acessar o script

include '../ex017b/outro_script.php';

//quarto metodo
//caminho absoluto

include 'C:\xampp\htdocs\Estudos-back-end\php\exercicios\ex017b\absoluto.php';
