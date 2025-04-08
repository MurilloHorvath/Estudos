function iniciar(){

    var txtprecoant = window.prompt('Qual o preço anterior do produto?')
    var txtprecoatu = window.prompt('Qual é o preço atual do produto?')

    var precoant = Number(txtprecoant)
    var precoatu = Number(txtprecoatu)

    var formatant = precoant.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
    var formatatu = precoatu.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});

    var res = document.getElementById('res')
    if(precoant < precoatu){

        var diferença = precoatu - precoant
        var formatdif = diferença.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
        var porcent = (precoatu/precoant - 1) * 100

        res.innerHTML = '<h3>Analisando os valores informados</h3>'
        res.innerHTML += `<p>O produto custava ${formatant} e agora custa ${formatatu}</p>`
        res.innerHTML += '<p>Hoje o produto está mais caro.</p>'
        res.innerHTML += `<p>O preço subiu ${formatdif} em relação ao preço anterior.</p>`
        res.innerHTML += `Uma variação de ${porcent}%.`

    }else{

        var diferença = precoant - precoatu
        var formatdif = diferença.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});
        var porcent = (precoatu/precoant - 1) * 100

        res.innerHTML = '<h3>Analisando os valores informados</h3>'
        res.innerHTML += `<p>O produto custava ${formatant} e agora custa ${formatatu}</p>`
        res.innerHTML += '<p>Hoje o produto está mais barato</p>'
        res.innerHTML += `<p>O preço caiu ${formatdif} em relação ao preço anterior.</p>`
        res.innerHTML += `Uma variação de ${porcent}%.`

    }
}

/*
var atual = 600000.00;

//com R$
var f = atual.toLocaleString('pt-br',{style: 'currency', currency: 'BRL'});

//sem R$
var f2 = atual.toLocaleString('pt-br', {minimumFractionDigits: 2}); 
*/