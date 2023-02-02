const previousOperationText = document.querySelector("#previous-operation")
const currentOperationText = document.querySelector("#current-operation")
const buttons = document.querySelectorAll("#buttons-container button")

class Calculator {
    constructor(previousOperationText, currentOperationText) {
        this.previousOperationText = previousOperationText
        this.currentOperationText = currentOperationText
        this.currentOperation = ""
    }

    // Adiciona digito na tela da calculadora
    addDigit(digit) {

        // analisa se a current operation ja tem um ponto
        if(digit === "." && this.currentOperationText.innerText.includes(".")) {
            return
        }

        this.currentOperation = digit
        this.updateScreen()

    }

    // processa as operações da calculadora
    processOperation(operation) {

        // checagem se o current esta vazio
        if(this.currentOperationText.innerText === "" && operation !== "C") {
            // mudança de operação
            if(this.previousOperationText.innerText !== "") {
                this.changeOperation(operation)
            }
            return
        }

        // pega os current e previous value
        let operationValue
        const previous = +this.previousOperationText.innerText.split(" ")[0]
        const current = +this.currentOperationText.innerText

        switch(operation) {
            case "+":
                operationValue = previous + current
                this.updateScreen(operationValue, operation, current, previous)
                break
            case "-":
                operationValue = previous - current
                this.updateScreen(operationValue, operation, current, previous)
                break
            case "*":
                operationValue = previous * current
                this.updateScreen(operationValue, operation, current, previous)
                break
            case "/":
                operationValue = previous / current
                this.updateScreen(operationValue, operation, current, previous)
                break
            case "DEL":
                this.processDelOperator()
                break
            case "CE":
                this.processCeOperator()
                break
            case "C":
                this.processCOperator()
                break
            case "=":
                this.processEqualOperator()
                break
            default:
                return
        }

    }

    // Muda os valores da tela da calculadora
    updateScreen(operationValue = null, 
        operation = null, 
        current = null, 
        previous = null
        ) {

            console.log(operationValue, operation, current, previous)

            if(operationValue == null) {
                this.currentOperationText.innerText += this.currentOperation
            } else {
                // checagem se o valor é zero, se for ele vai adicionar o current value
                if(previous === 0) {
                    operationValue = current
                }
                // adiciona o current value no previous
                this.previousOperationText.innerText = `${operationValue} ${operation}`
                this.currentOperationText.innerText = ""
            }
    }

    // mudança da operação matematica
    changeOperation(operation) {

        const mathOperations = ['+','-','/','*']

        if(!mathOperations.includes(operation)) {
            return
        }

        this.previousOperationText.innerText = this.previousOperationText.innerText.slice(0, -1) + operation

    }

    // operação de deletar um digito
    processDelOperator() {

        this.currentOperationText.innerText = this.currentOperationText.innerText.slice(0, -1)

    }

    // operação de limpar a current operation
    processCeOperator() {

        this.currentOperationText.innerText = ""

    }

    // operação de limpar a current e a previous operation
    processCOperator() {

        this.currentOperationText.innerText = ""
        this.previousOperationText.innerText = ""

    }

    // operação de mostrar o resultado da conta 
    processEqualOperator() {

        const operation = previousOperationText.innerText.split(" ")[1]

        this.processOperation(operation)

    }
}

const calc = new Calculator(previousOperationText, currentOperationText)

buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {

        const value = e.target.innerText

        if(+value >= 0 || value === ".") {
            calc.addDigit(value)
        } else {
            calc.processOperation(value)
        }

    })
})