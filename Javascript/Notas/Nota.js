/*Crie dois códigos de sistema de notas para uma escola. 
O primeiro código deve ser um programa que informa se o aluno reprovou, ou não, com base nas três notas que ele adicionou ao programa. 
Utilize, no mínimo, um operador de atribuição e um operador ternário. 
O segundo código é um programa que o aluno deve escrever duas notas e o retorno informa a nota mínima que ele deve tirar na próxima 
prova para poder passar com nota sete.*/


var nota01
var nota02
var nota03

var media

var readlineSync = require('readline-sync');

nota01 = parseFloat(readlineSync.question("Informe a primeira nota: \n"));
nota02 = parseFloat(readlineSync.question("Informe a segunda nota: \n"));
nota03 = parseFloat(readlineSync.question("Informe a segunda nota: \n"));
media = (nota01 + nota02 + nota03) / 3



console.log('Resultado ', media>= 7 ? ("Aprovado, média: " + media) : ("Reprovado, média: " + media)) 