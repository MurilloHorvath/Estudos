let pessoa = {
    nome: 'Murillo',
    idade: 19,
    falar: function() {
        console.log('Oi!')
    },
    soma: function(a, b) {
        return a + b
    }
}

console.log(pessoa.nome)
pessoa.falar()
console.log(pessoa.soma(5,3))