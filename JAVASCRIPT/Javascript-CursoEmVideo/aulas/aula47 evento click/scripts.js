var btn = document.querySelector("#btn")

console.log(btn)

btn.addEventListener("click", function() {

    console.log("Clicou no botão")
    console.log(this)
    this.style.color = 'red'

})

// click afetando outros elementos
var title = document.querySelector("#title")
console.log(title)

title.addEventListener("click", function() {

    console.log("Clicou no titulo")
    this.style.color = 'blue'

    var subtitle = document.querySelector("#subtitle")
    subtitle.style.display = 'none'

})

// double click
var subtitle = document.querySelector("#subtitle")
subtitle.addEventListener("dblclick", function() {

    console.log("click duplo")

})