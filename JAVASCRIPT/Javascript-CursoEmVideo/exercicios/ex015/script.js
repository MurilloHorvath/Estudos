function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    
    if(fano.value.length == 0 || fano.value > ano){
        window.alert('[ERRO] Verifique se você preencheu corretamente...')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')

        img.setAttribute('id', 'foto')

        if(fsex[0].checked){
            genero = 'Homem'
            if(idade >=0 && idade < 10){
                //crianca
                img.setAttribute('src', 'imagens/criancaM.png')
            }else if(idade < 21){
                //jovem
                img.setAttribute('src', 'imagens/jovemM.png')
            }else if(idade < 50){
                //adulto
                img.setAttribute('src', 'imagens/adultoM.png')
            }else{
                //idoso
                img.setAttribute('src', 'imagens/idosoM.png')
            }
        }else if(fsex[1].checked){
            genero = 'Mulher'
            if(idade >= 0 && idade < 10){
                //crianca
                img.setAttribute('src', 'imagens/criancaF.png')
            }else if(idade < 21){
                //jovem
                img.setAttribute('src', 'imagens/jovemF.png')
            }else if(idade < 50){
                //adulto
                img.setAttribute('src', 'imagens/adultoF.png')
            }else{
                //idoso
                img.setAttribute('src', 'imagens/idosoF.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `<p>Detectamos ${genero} com ${idade} anos.</p>`
        res.appendChild(img)
    }
}