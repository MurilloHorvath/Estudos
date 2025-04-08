<?php

//testando variaveis

//unset
/*
Permite 'destruir' uma variavel
existe duas formas de o fazer, mas com ligeiras diferenças de performance
e atuaçã no sistema.
*/

$a = 'joao';
unset($a);

$b = 'antonio';
$b = null;

/*
No primeiro caso, a variavel é 'libertada' e no proximo ciclo de limpeza
(gabage collector) ela é removida da memoria

No segundo caso a variavel vai persistir na memoria, mas sem valor atribuido
apesar de libertar memória quanto a inexistencia de valor.

segure-se a utilização do unset nestes casos.
*/