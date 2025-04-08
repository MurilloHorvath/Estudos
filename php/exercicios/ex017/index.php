<?php

//constants

//para verificar se uma constante ja existe
if(!defined('APP_NAME')){
   define('APP_NAME', 'Aplicativo');
}

echo APP_NAME;
echo '<br>';

// ou mais comum ainda
defined('CONSTANTE') or define('CONSTANTE', 'valor');

//constantes podem ser definidas como arrays
const NOMES = ['joao', 'ana', 'carlos'];
echo NOMES[0];
echo '<br>';

//podem ser definidas arrays no define tambem
define('NAMES', ['joao', 'ana', 'carlos']);
echo NAMES[2];