/*O segundo código é um programa que o aluno deve escrever duas notas e o retorno informa a nota mínima que ele deve tirar na próxima 
prova para poder passar com nota sete.*/

var nota01
var nota02 
var nota03


var readlineSync = require('readline-sync');

nota01 = parseFloat(readlineSync.question("Informe a primeira nota: \n"));
nota02 = parseFloat(readlineSync.question("Informe a segunda nota: \n"));

necessidade = (nota01 + nota02) - 21

console.log('Resultado ', necessidade > 10 ? ("Não é possivel recuperar a 3° nota, necessidade: " + necessidade) : ("Pontos necessarios: " + necessidade)) 