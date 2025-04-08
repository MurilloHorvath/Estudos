function iniciar(){
    var metros = Number(window.prompt('Digite uma distância em metros (m)'))
    var quilometro = metros / 1000
    var hectometro = metros / 100
    var decametro = metros / 10
    var decimetro = metros * 10
    var centimetro = metros * 100
    var milimetro = metros * 1000


    var res = window.document.getElementById('res')
    res.innerHTML = `<h2>A distância de ${metros} metros, corresponde a...</h2>${quilometro} Quilômetros (KM)<br>${hectometro} Hectômetros (Hm)<br>${decametro} Decâmetros (Dam)<br>${decimetro} Decímetros (dm)<br>${centimetro} Centímetros (cm)<br>${milimetro} Milímetros (mm)`
    
}