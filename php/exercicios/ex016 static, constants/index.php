<?php

//static
//como se fazem as implementações

class operacoes{

    static $valor1;
    static $valor2;

    static function adicionar(){

        return self::$valor1 + self::$valor2;
    }
}

operacoes::$valor1 = 10;
operacoes::$valor2 = 20;
echo operacoes::adicionar();