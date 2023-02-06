const addressForm = document.querySelector("#address-form")
const cepInput = document.querySelector("#cep")
const addressInput = document.querySelector("#address")
const cityInput = document.querySelector("#city")
const neighborhoodInput = document.querySelector("#neighborhood")
const regionInput = document.querySelector("#region")
const formInputs = document.querySelectorAll("[data-input]")

const closeButton = document.querySelector("#close-message")

const fadeElement = document.querySelector("#fade")


// validação do cep digitado
cepInput.addEventListener("keypress", (e) => {

    const onlyNumbers = /[0-9]/
    const key = String.fromCharCode(e.keyCode)

    // aceitar apenas numeros
    if(!onlyNumbers.test(key)) {
        e.preventDefault()
        return
    }

})

// evento de pegar o endereço 
cepInput.addEventListener("keyup", (e) => {

    const inputValue = e.target.value

    // checagem se possui a quantidade necessaria de digitos
    if(inputValue.length === 8) {
        getAddress(inputValue)
    }

})

// pegar endereço customizado da API
const getAddress = async (cep) => {
    
    toggleLoader()

    cepInput.blur()

    const apiUrl = `https://viacep.com.br/ws/${cep}/json/`

    const response = await fetch(apiUrl)

    const data = await response.json()

    // mostrar erro e resetar formulario
    if(data.erro === true){

        if(!addressInput.hasAttribute("disabled")) {
           toggleDisabled() 
        }

        addressForm.reset()
        toggleLoader()
        toggleMessage("CEP inválido, Tente novamente.")
        return
    }

    if(addressInput.value === "") {
        toggleDisabled()
    }

    addressInput.value = data.logradouro
    cityInput.value = data.localidade
    neighborhoodInput.value = data.bairro
    regionInput.value = data.uf

    toggleLoader()

}

// addicionar or remover o disabled attribute
const toggleDisabled = () => {

    if(regionInput.hasAttribute("disabled")) {
        formInputs.forEach((input) => {
            input.removeAttribute("disabled")
        })
    } else{
        formInputs.forEach((input) => {
            input.setAttribute("disabled", "disabled")
        })
    }

}

// mostrar ou esconder o loader
const toggleLoader = () => {
    const loaderElement = document.querySelector("#loader")

    fadeElement.classList.toggle("hide")
    loaderElement.classList.toggle("hide")

}

// mostrar ou esconder a mensagem
const toggleMessage = (msg) => {

    const messageElement = document.querySelector("#message")

    const messageElementText = document.querySelector("#message p")

    messageElementText.innerText = msg

    fadeElement.classList.toggle("hide")
    messageElement.classList.toggle("hide")

}

// fechar mensagem
closeButton.addEventListener("click", () => toggleMessage());

// savar cadastro
addressForm.addEventListener("submit", (e) => {

    e.preventDefault()

    toggleLoader()

    setTimeout(() => {

        toggleLoader()

        toggleMessage("Endereço salvo com sucesso!")

        addressForm.reset()

        toggleDisabled()

    }, 1500);

})