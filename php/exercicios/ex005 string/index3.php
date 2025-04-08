<?php

//HEREDOC e NOWDOC (outras formas de delimitação)
//apesar de nao serem muito comuns, podem ser usadas para tratamento de maiores blocos de texto.

// HEREDOC - permite fazer o parse de variaveis

$cliente = 'João Ribeiro';
$email = 'joao.ribeiro@gmail.com';

$texto = <<<Label
Olá, sr. $cliente.
Serve a presente mensagem para informar que se encontra inscrito no proximo concurso.
Enviamos o regulamento para o seu email $email
Obrigado pela simpatia.
Label;

echo $texto;

die();