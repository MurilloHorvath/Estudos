// elementos 
const greenBtn = document.querySelector("#green")
const silverBtn = document.querySelector("#silver")
const goldenBtn = document.querySelector("#golden")
const grafiteBtn = document.querySelector("#grafite")
const blueBtn = document.querySelector("#blue")
const colorsBtn = document.querySelectorAll("color")
const imagemIphone = document.querySelector("#product-image")

// funçoes
const mudarCor = (cor) => {

    limpa()

    const selectedColor = cor.querySelector(".description").innerText
    const color = cor.querySelector(".color")
    color.classList.add('selected')

    switch(selectedColor){
        case "Verde-Alpino":
            imagemIphone.src="img/iphone_green.jpg"
            break
        case "Prateado":
            imagemIphone.src="img/iphone_silver.jpg"
            break
        case "Dourado":
            imagemIphone.src="img/iphone_golden.jpg"
            break
        case "Grafite":
            imagemIphone.src="img/iphone_grafite.jpg"
            break
        case "Azul-Sierra":
            imagemIphone.src="img/iphone_blue.jpg"
            break
    }

}

const limpa = () => {

    const limpaGreen = greenBtn.querySelector(".color")
    limpaGreen.classList.remove('selected')
    const limpaSilver = silverBtn.querySelector(".color")
    limpaSilver.classList.remove('selected')
    const limpaGolden = goldenBtn.querySelector(".color")
    limpaGolden.classList.remove('selected')
    const limpaGrafite = grafiteBtn.querySelector(".color")
    limpaGrafite.classList.remove('selected')
    const limpaBlue = blueBtn.querySelector(".color")
    limpaBlue.classList.remove('selected')

}

// eventos
[greenBtn, silverBtn, goldenBtn, grafiteBtn, blueBtn].forEach((el) => {
    
    el.addEventListener("click", () => mudarCor(el))

})