var valor1
var valor2
var operacao
var readlineSync = require('readline-sync');

operacao = readlineSync.question("Digite a operação: (+) (-) (*) (/)? : \n");
valor1 = parseFloat(readlineSync.question("Informe o primeiro numero: \n"));
valor2 = parseFloat(readlineSync.question("Informe o segundo numero: \n"));

function iniciarCalculadora(operador, primeiroValor, segundoValor) {
    if (operador == "+") {
        return primeiroValor + segundoValor;
    } else if
        (operador == "-") {
        return primeiroValor - segundoValor;
    } else if
        (operador == "*") {
        return primeiroValor * segundoValor;
    } else if
        (operador == "/") {
        return primeiroValor / segundoValor;
    } else {
        throw new Error('Operação inválida');
    }
}

console.log('Resultado', iniciarCalculadora(operacao, valor1, valor2)) 