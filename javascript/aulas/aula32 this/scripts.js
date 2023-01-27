console.log(this)

var teste = 5
console.log(this.teste)
console.log(teste)

let pessoa = {
    nome: 'Murillo',
    idade: 19,
    falar: function() {
        console.log('Oi!')
    },
    dizerNome: function() {
        console.log('O meu nome é ' + this.nome)
    },
    aniversario: function() {
        this.idade += 1
    },
    saudacao: function() {
        return 'Sr. ' + this.nome
    }
}

pessoa.dizerNome()
console.log(pessoa.idade)
pessoa.aniversario()
console.log(pessoa.idade)

console.log(pessoa.saudacao())
var sdc = pessoa.saudacao()
console.log('Oi,' , sdc)