#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num_1, num_2, operacao):
    if(operacao == '+'):
        print('Soma: ', num_1 + num_2)
    elif(operacao == '-'):
        print('Subtração: ', num_1 - num_2)
    elif (operacao == '/' and num_2 != 0):
        print('Divisão: ', num_1 / num_2)
    elif (operacao == '*'):
        print('Multiplicação: ', num_1 * num_2)
    else:
        print('Operação não aceita! \n Resultado = 0 \n\n')

numero_1 = int(input('Coloque o primeiro número: '))
numero_2 = int(input('Coloque o segundo número: '))
condicao = str(input('Indique a operacao: '))

calculadora(numero_1, numero_2, condicao)
