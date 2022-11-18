function iniciar(){
    var txtyear = window.prompt('Qual é o ano que você quer verificar?')
    var year = Number(txtyear)

    var res = document.getElementById('res')
    res.innerHTML = ''
    if ((year % 400 == 0 || year % 100 !== 0) && year % 4 == 0){
        res.innerHTML = `<h3>Analisando o ano de ${year}</h3>`
        res.innerHTML += `<p>O ano de ${year} <mark><strong>É BISSEXTO</strong></mark> \u2705</p>`
    }else{
        res.innerHTML = `<h3>Analisando o ano de ${year}</h3>`
        res.innerHTML += `<p>O ano de ${year} <mark><strong>NÃO É BISSEXTO</strong></mark> \u274C</p>`
    }

}