const objs = [
    {
        nome: 'Murillo',
        idade: 19,
        hobbies: ['Academia','Estudar'],
        esta_trabalhando: false,
        detalhes_profissao: {
            profissao: null,
            empresa: null,
        },
    },
    {
        nome: 'Maria',
        idade: 25,
        hobbies: ['Viajar','Ler'],
        esta_trabalhando: true,
        detalhes_profissao: {
            profissao: 'Empresária',
            empresa: 'empresa x',
        },
    },
]

console.log(objs)

// JSON
// Converter obj para json
const jsonData = JSON.stringify(objs)

console.log(jsonData)
console.log(typeof jsonData)

// converter json para objeto
const objData = JSON.parse(jsonData)

console.log(objData)
console.log(typeof objData)

objData.map((pessoa) => {
    console.log(pessoa.nome)
    console.log(pessoa.idade)
})