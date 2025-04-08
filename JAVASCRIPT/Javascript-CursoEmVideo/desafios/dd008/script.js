function iniciar(){
    var produto = window.prompt('Qual produto que você está comprando?')
    var preço = Number(window.prompt(`Qual é o preço de ${produto}`))
    var desconto = preço * 0.10
    var preçodescontado = preço - desconto

    var res = window.document.getElementById('res')
    res.innerHTML = `Calculando desconto de 10% para ${produto}`
    res.innerHTML += `<p>O preço original era R$ ${preço}</p><p>Você acaba de ganhar R$ ${desconto} de desconto(-10%).</p><p>No fim, você vai pagar R$ ${preçodescontado} no produto ${produto}</p>`

}