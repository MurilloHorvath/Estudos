<?php

//constants

//define
//a função define permite definir constants globais e locais, mas nao permite ser usada
// dentro do contexto de uma classe.

define('APP_NAME', 'Aplicativo');
define('VERSAO', '1.0.0');
define('MOSTRAR_ERROS', true);
define('PI', 3.14);

echo APP_NAME;
echo '<br>';

//os nomes das constantes sempre com letras maiusculas