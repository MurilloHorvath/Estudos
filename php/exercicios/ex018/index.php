<?php

/*
alem do include existem mais 3 formas de importação de scripts
    require
    include_once
    require_once

require é semelhante ao include
a diferença entre eles é se caso do include falhar, o código avança com um aviso.
no caso do require falhar, a apalicação termina com um erro.
*/

include 'teste.php';
echo 'momento 1';

//require 'teste.php'
//echo 'momento 2';

//aconselhavel uso do require em codigos grandes
//em codigos pequenos aconselhavel uso do include