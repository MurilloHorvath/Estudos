function iniciar(){
    var nome = window.prompt('Qual é o nome do funcionário?')
    var salarioatual = Number(window.prompt(`Qual é o salário de ${nome}?`))
    var porcentagem = Number(window.prompt(`O salário de ${nome} vai ser reajustado em qual porcentagem`))

    var aumento = salarioatual * (porcentagem / 100)
    var salario2 = salarioatual + aumento

    var res = window.document.getElementById('res')
    res.innerHTML = `<h3>${nome} recebeu um aumento salarial!</h3>`
    res.innerHTML += `<p>O salário atual era R$ ${salarioatual}</p><p>Com um aumento de ${porcentagem}%, o salário vai aumentar ${aumento}</p>E a partir daí, ${nome} vai passar a ganhar R$ ${salario2}.`
}