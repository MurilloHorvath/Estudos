// clearTimeout
var x = 0

var myTimer = setTimeout(function() {

    console.log("O x é 0")

},1500)

x = 5

if(x>0){
    clearTimeout(myTimer)
    console.log('O x é maior que 0')
}

// clearInterval
var myInterval = setInterval(function() {

    console.log("Intervalo")

}, 500)

setTimeout(function() {

    console.log("não precisa mais repetir")
    clearInterval(myInterval)

}, 2500)