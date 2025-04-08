<?php


//traits

/*
São um grupo de metodos que podem ser inseridos dentro de classes.
foram adicionados a linguagem na sua versao 5.4 para aumentar a reutilização 
de codigo.

os traits sao definidos com a expressão trait, seguido pelo nome e por um bloco
de codigo. as regras para dar nomes a traits são as mesmas que usamos nas classes
*/

trait MinhasHabilidades{

    public function falar($mensagem){
        echo "Eu digo: $mensagem";
    }

    public function saltar($metros){
        echo "Eu salto $metros metros.";
    }
}

// as classes que necessitarem de usar estes metodos do trait,apenas terao
//que ter o seguinte

class Humano{
    use MinhasHabilidades;
}

$h = new Humano();
$h->falar('Olá Mundo!');
echo '<br>';
$h->saltar(3);