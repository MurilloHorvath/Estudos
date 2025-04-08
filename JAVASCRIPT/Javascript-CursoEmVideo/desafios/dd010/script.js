function iniciar(){
    var a = Number(window.prompt('Qual é o valor de a?'))
    var b = Number(window.prompt('Qual é o valor de b?'))
    var c = Number(window.prompt('Qual é o valor de c?'))

    var resultado = (b ** 2) - (4 * a * c)

    var res = window.document.getElementById('res')
    res.innerHTML = '<h2>Resolvendo Bhaskara</h2>'
    res.innerHTML += `<p>A equação atual é <strong>${a}x² + ${b}x + ${c} = 0</strong></p>O cálculo realizado sera <strong>△ = ${b}² - 4 . ${a} . ${c}</strong><p>O valor calculado foi <strong>△ = ${resultado}</strong></p>`
}