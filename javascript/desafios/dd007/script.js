

    var cot = Number(window.prompt('Antes de mais nada. Quanto está a cotação do dólar atualmente?'))

function iniciar(){
    var reais = Number(window.prompt('Quantos R$ você tem na carteira?'))
    var dolar = reais / cot

    var res = window.document.getElementById('res')
    res.innerHTML = `<h3>Você possui atualmente US$ ${dolar} dolares na carteira!</h3>`
}