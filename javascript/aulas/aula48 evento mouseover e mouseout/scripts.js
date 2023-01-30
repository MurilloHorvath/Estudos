// evento mouseover
var title = document.querySelector("#title")

title.addEventListener("mouseover", function() {

    this.style.backgroundColor = 'gray'

})

// evento mouseout
title.addEventListener("mouseout", function() {

    this.style.backgroundColor = 'white'

})

// afetar outro elemento com mouseover
var subtitle = document.querySelector("#subtitle")

subtitle.addEventListener("mouseover", function() {

    var legenda = document.querySelector("#legenda")

    this.style.backgroundColor = 'gray'

    legenda.classList.remove("hide")

})

subtitle.addEventListener("mouseout", function() {

    var legenda = document.querySelector("#legenda")

    this.style.backgroundColor = 'white'

    legenda.classList.add("hide")

})