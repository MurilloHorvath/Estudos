function iniciar(){
    var celsius = Number(window.prompt('Digite uma temperatura em °C (Celsius)'))
    var kel =  celsius + 273.15
    var fah =  (celsius * 9 / 5) + 32

    var res = window.document.getElementById('res')
    res.innerHTML = `<h3>A temperatura de ${celsius}°C, correspode a...</h3>`
    res.innerHTML += `<p>${kel}°K (Kelvin)</p><p>${fah}°F (Fahrenheit)</p>`

}