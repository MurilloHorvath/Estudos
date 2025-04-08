<?php

//INCLUDE_ONCE e REQUIRE_ONCE

/*
A expressao include_once funciona exatamente como o include, no entanto 
se o script ja foi anteriormente incluido, o php nao o volta a incluir
*/

include_once 'config.php';
echo 'AAA';
include_once 'config.php';
echo 'BBB';

/*
no caso do require_once funciona exatamente como o require, 
mas com o mesmo comportamento do include_once...
*/

require_once 'config.php';
echo 'CCC';
require_once 'config.php';
echo 'DDD';