const data = [
    {name: "Murillo", age: 19, sallary: 0, driverLicense: true},
    {name: "João", age: 18, sallary: 1500, driverLicense: false},
    {name: "Mariana", age: 22, sallary: 4000, driverLicense: true},
    {name: "Pedro", age: 50, sallary: 7200, driverLicense: true},
    {name: "Jasmin", age: 16, sallary: 0, driverLicense: false},
]

// 1 - reverse
const reverseData = data.reverse()
console.log(reverseData)

// 2 - find
const highSallary = 5000
const highestSallary = data.find((user) => user.sallary > highSallary)
console.log(highestSallary)

// 3 - findIndex
const lowestSallary = data.findIndex((user) => user.sallary > 0 && user.sallary < 2000)
console.log(lowestSallary)
data[lowestSallary].sallary += 200
console.log(data)

// 4 - includes
const numbers = [1,2,3,4,5]
const hasFour = numbers.includes(4)
console.log(hasFour)
console.log(numbers.includes(100))

// 5 - map
data.map((user) => user.newsletter = false)
console.log(data)

// 6 - filter
const drivers = data.filter((user) => user.driverLicense)
console.log(drivers)

// 7 - reduce
const sallariesSum = data.reduce((totalSallary, user) => totalSallary += user.sallary, 0)
console.log(sallariesSum)

// 8 - forEach
const showUserNames = (users) => {

    users.forEach((user) => {
        console.log(`Olá ${user.name}!`)
    })

}

showUserNames(data)

// 9 - some
let someoneWithNewletter = data.some((user) => user.newsletter)
console.log(someoneWithNewletter)

data[0].newsletter = true
someoneWithNewletter = data.some((user) => user.newsletter)
console.log(someoneWithNewletter)

// 10 - every
const everyUserHasName = data.every((user) => user.name)
console.log(everyUserHasName)

const everyUserHasGoodSallary = data.every((user) => {
    return user.sallary > 2000
})
console.log(everyUserHasGoodSallary)