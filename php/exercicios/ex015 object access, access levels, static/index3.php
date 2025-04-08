<?php

class tempo{

    private $segundos;

    function setsegundos($valor){
        if(!is_numeric($valor) || $valor < 0){
            $this->segundos = 0;
        }else{
            $this->segundos = $valor;
        }
    }


    function getminutos(){
        return $this->segundos / 60;
    }

    function setminutos($valor){
        if($valor == 0){
            $this->segundos = 0;
        }else{
            $this->segundos = $valor * 60;
        }
    }
}