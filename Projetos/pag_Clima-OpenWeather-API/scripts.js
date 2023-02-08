// elementos
const apiKey = "751c78764d765cc5ea33f054c3ed6c43"
const apiCountryURL = "https://countryflagsapi.com/png/"

const cityInput = document.querySelector("#city-input")
const searchBtn = document.querySelector("#search")

const cityElement = document.querySelector("#city")
const tempElement = document.querySelector("#temperature span")
const descElement = document.querySelector("#description")
const weatherIconElement = document.querySelector("#weather-icon")
const countryElement = document.querySelector("#country")
const umidityElement = document.querySelector("#umidity span")
const windElement = document.querySelector("#wind span")

// funcoes
const getWeatherData = async(city) => {

    const apiWeatherURL = `https://api.openweathermap.org/data/3.0/weather?q=${city}&units=metric&appid=${apiKey}&lang=pt_br`

    const res = await fetch(apiWeatherURL)
    const data = await res.json()

    console.log(data)

}

const showWeatherData = (city) => {

    getWeatherData(city)

}

// eventos
searchBtn.addEventListener("click", (e) => {

   e.preventDefault()
   
   const city = cityInput.value

   showWeatherData(city)

})
