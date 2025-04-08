// inserindo no body
var novoParagrafo = document.createElement("p")
var texto = document.createTextNode("Este é o conteúdo do paragráfo")
novoParagrafo.appendChild(texto)

var body = document.querySelector("body")

body.appendChild(novoParagrafo)

// inserindo em um container
var container = document.querySelector("#container")

var ele = document.createElement("span")
ele.appendChild(document.createTextNode("Texto do SPAN"))

container.appendChild(ele)