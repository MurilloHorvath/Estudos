// criar elemento
var el = document.createElement("h3")
el.classList = "testando-classe"
var texto = document.createTextNode("Este é o texto do h3")

el.appendChild(texto)

// selecionar o elemnto que quero trocar
var title = document.querySelector("#title")

// selecionar o  pai do elemento
var pai = title.parentNode

// trocar o elementos
pai.replaceChild(el, title)