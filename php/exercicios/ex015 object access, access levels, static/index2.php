<?php

//access level

class humano2{
    
    private $idade = 0;

    public function setIdade($valor){

        if(is_numeric($valor)){
            $this->idade = $valor;
        }
    }
    public function getIdade(){
        return $this->idade;
    }
}

$eu2 = new humano2();
$eu2->setIdade('murillo');
echo $eu2->getIdade();