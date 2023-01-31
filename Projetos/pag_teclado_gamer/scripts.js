document.addEventListener("keydown", function(event) {

    var teclas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','1','2','3','4','5','6','7','8','9','0','enter',' ','meta','contextmenu','alt','altgr','control','shift',',','.','/','capslock','dead',']','tab','[','backspace',]

    for(var j = 0; j<teclas.length; j++) {

        var doispontos = document.querySelector('.t-doispontos')
        if(event.key === ';'){
            doispontos.style.backgroundColor = 'red'
        }

        var virgula = document.querySelector('.t-virgula')
        if(event.key === ','){
            virgula.style.backgroundColor = 'red'
        }

        var ponto = document.querySelector('.t-ponto')
        if(event.key === '.'){
            ponto.style.backgroundColor = 'red'
        }

        var barra = document.querySelector('.t-barra')
        if(event.key === '/'){
            barra.style.backgroundColor = 'red'
        }

        var fchaves = document.querySelector('.t-fchaves')
        if(event.key === ']'){
            fchaves.style.backgroundColor = 'red'
        }

        var chaves = document.querySelector('.t-chaves')
        if(event.key === '['){
            chaves.style.backgroundColor = 'red'
        }

        var tecla = document.querySelectorAll('.t-' + teclas[j])
        if(event.key.toLowerCase() === teclas[j]) {
            tecla[0].style.backgroundColor = 'red'
            if(event.key.toLowerCase() === 'enter'){
                tecla[1].style.backgroundColor = 'red'
            }
            if(event.key.toLowerCase() === 'alt'){
                tecla[1].style.backgroundColor = 'red'
            }
            if(event.key.toLowerCase() === 'meta'){
                tecla[1].style.backgroundColor = 'red'
            }
            if(event.key.toLowerCase() === 'control'){
                tecla[1].style.backgroundColor = 'red'
            }
            if(event.key.toLowerCase() === 'shift'){
                tecla[1].style.backgroundColor = 'red'
            }
        }

    }

})



// keyup
document.addEventListener("keyup", function(event) {

    var teclas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','1','2','3','4','5','6','7','8','9','0','enter',' ','meta','contextmenu','alt','altgr','control','shift',',','.','/','capslock','dead',']','tab','[','backspace',]

    for(var j = 0; j<teclas.length; j++) {

        var doispontos = document.querySelector('.t-doispontos')
        if(event.key === ';'){
            doispontos.style.backgroundColor = '#e4e4e4'
        }

        var virgula = document.querySelector('.t-virgula')
        if(event.key === ','){
            virgula.style.backgroundColor = '#e4e4e4'
        }

        var ponto = document.querySelector('.t-ponto')
        if(event.key === '.'){
            ponto.style.backgroundColor = '#e4e4e4'
        }

        var barra = document.querySelector('.t-barra')
        if(event.key === '/'){
            barra.style.backgroundColor = '#e4e4e4'
        }

        var fchaves = document.querySelector('.t-fchaves')
        if(event.key === ']'){
            fchaves.style.backgroundColor = '#e4e4e4'
        }

        var chaves = document.querySelector('.t-chaves')
        if(event.key === '['){
            chaves.style.backgroundColor = '#e4e4e4'
        }

        var tecla = document.querySelectorAll('.t-' + teclas[j])
        if(event.key.toLowerCase() === teclas[j]) {
            tecla[0].style.backgroundColor = '#e4e4e4'
            if(event.key.toLowerCase() === 'enter'){
                tecla[1].style.backgroundColor = '#e4e4e4'
            }
            if(event.key.toLowerCase() === 'alt'){
                tecla[1].style.backgroundColor = '#e4e4e4'
            }
            if(event.key.toLowerCase() === 'meta'){
                tecla[1].style.backgroundColor = '#e4e4e4'
            }
            if(event.key.toLowerCase() === 'control'){
                tecla[1].style.backgroundColor = '#e4e4e4'
            }
            if(event.key.toLowerCase() === 'shift'){
                tecla[1].style.backgroundColor = '#e4e4e4'
            }
        }

    }

})
