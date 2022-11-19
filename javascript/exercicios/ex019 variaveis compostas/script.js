let num = [ 2 , 5 , 8 , 1 , 4 , 6]
num[6] = 7
num.push(3)
num.sort()

//num.length metodo para mostrar quantos elementos possui
//num.sort() metodo para deixar os numeros em ordem crescente
//num.indexOf(7) metodo para procurar o valor no vetor(no caso esta procurando o valor 7) se ele procurar e não achar vai ser sinalizado (-1)

console.log(`Nosso vetor é o ${num}`)
console.log(`Nosso vetor num possui ${num.length} elementos`)
let inof = num.indexOf(5)
console.log(`O valor 5 esta na posição ${inof}`)

/*
for(let pos = 0; pos < num.length ;pos++){
    console.log(`Na posição ${pos} possui o valor ${num[pos]}`)
}
*/

for(let pos in num){
    //esse formato de for so funciona para arrays e objetos
    console.log(`Na posição ${pos} possui o valor ${num[pos]}`)
}