<?php

// sintaxe alternativa

//normal
$valor = 5;
if($valor == 10){
    //codigo 1
} else {
    //codigo 2
}

//alternativa
if($valor == 10):
    // codigo 1
else:
    // codigo 2
endif;

// switch
switch ($variable):
    case 'value':
        break;
    
    default:
    // code
    break;
endswitch;