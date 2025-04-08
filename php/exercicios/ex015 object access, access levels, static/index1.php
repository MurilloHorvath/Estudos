<?php

//access level - aspectos importantes

class humano{
    public $idade;
}

$eu = new humano();
$eu->idade = 'ola mundo'; //isso é possivel por que o php nao é strongly typed

class humano1{
    private $idade;
}

$eu1->idade= 'murillo'; //nao é possivel por que a propriedade é privada