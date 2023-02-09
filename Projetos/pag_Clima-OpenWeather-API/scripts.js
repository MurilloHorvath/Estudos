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
const umidityElement = document.querySelector("#humidity span")
const windElement = document.querySelector("#wind span")

const weatherContainer = document.querySelector("#weather-data")

// funcoes
const getWeatherData = async(city) => {

    const dataLatLon = await getLatLonData(city)

    const apiWeatherURL = `https://api.openweathermap.org/data/2.5/weather?lat=${dataLatLon[0].lat}&lon=${dataLatLon[0].lon}&appid=${apiKey}&lang=pt_br`
    const res = await fetch(apiWeatherURL)
    const data = await res.json()

    return [data,dataLatLon]

}

const getLatLonData = async(city) => {

    const apiLatLonURL = `http://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=${apiKey}`
    const res = await fetch(apiLatLonURL)
    const data = await res.json()

    return data

}


const showWeatherData = async(city) => {

    const data = await getWeatherData(city)

    console.log(data)

    cityElement.innerText = data[1][0].name
    tempElement.innerText = `${parseInt(data[0].main.temp - 273.15)} °C`
    descElement.innerText = data[0].weather[0].description
    weatherIconElement.setAttribute("src", `http://openweathermap.org/img/wn/${data[0].weather[0].icon}.png`)
    countryElement.setAttribute("src", apiCountryURL + data[0].sys.country)
    umidityElement.innerText = `${data[0].main.humidity}%`
    windElement.innerText = `${data[0].wind.speed}km/h`

    weatherContainer.classList.remove("hide")

}

// eventos
searchBtn.addEventListener("click", (e) => {

   e.preventDefault()
   
   const city = cityInput.value

   showWeatherData(city)

})

cityInput.addEventListener("keyup", (e) => {

    if(e.code === "Enter") {

        const city = e.target.value

        showWeatherData(city)

    }

})