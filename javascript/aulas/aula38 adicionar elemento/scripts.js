// criar elemento
var el = document.createElement("div")
el.classList = "div-criada"
console.log(el)

var container = document.querySelector("#container")

// inserindo elemento filho
container.appendChild(el)

// insertBefore - inserindo antes
var el2 = document.createElement("div")
el2.classList = "div-before"

var el3 = document.querySelector("#container .div-criada")

container.insertBefore(el2, el3)