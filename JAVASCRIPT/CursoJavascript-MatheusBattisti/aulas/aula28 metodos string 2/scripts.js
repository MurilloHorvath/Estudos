// toLowerCase e toUpperCase

var frase = 'Esta é a frase que vamos manipular'

var caixaalta = frase.toUpperCase()

console.log(caixaalta)

console.log(frase.toLowerCase())

// trim

var nome = '        Murillo         '

var nomeTrim = nome.trim()


console.log(nome)
console.log(nomeTrim)

// split

console.log(frase.split(' '))

var tags = 'PHP, JavaScript, HTML, CSS'

console.log(tags.split(', '))

// lastIndexOf

var fraseDois = 'Eu quero a ultima palavra teste desta frase teste'

console.log(fraseDois.indexOf('teste'))

console.log(fraseDois.lastIndexOf('teste'))