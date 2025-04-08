<?php
//operador ternário

// o operador necessita de tres expressoes ou areas
// 1 expressao que sera avaliada como verdadeira
// 2 expressao que sera executada como true
// 3 expressao que sera executada como false

$opcao = 0;

$nome = $opcao == 1 ? 'joao' : 'antonio';

//pode ser usado da seguinte forma

$opcao == 1 ? $nome = 'joao' : $nome = 'antonio';

//pode ser usado para mostrar um determinado texto

echo $opcao == 1 ? 'sim' : 'nao';

?>

<!--com instrução condicional if -->
<?php if($opcao == 1):?>
    <h2>SIM</h2>
<?php else: ?>
    <h2>NAO</h2>
<?php endif; ?>

<!-- com operador ternario -->
<h2><?= $opcao === 1 ? 'SIM' : 'NAO'?></h2>

<!-- por exemplo, para controlar css -->
<h2 style="color: <?= $opcao == 1? 'red' : 'blue'?>">Este texto tem cor definida pelo PHP</h2>

