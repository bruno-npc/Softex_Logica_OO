#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair
#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 
import time

def isInt(valor):
  try:
    int(valor)
    return True
  except:
    return False

def calculadora(num_1, num_2, op):
    if(op == 1):
        print('Soma: ', num_1 + num_2)
        time.sleep(5)
    elif(op == 2):
        print('Subtração: ', num_1 - num_2)
        time.sleep(5)
    elif (op == 3):
        print('Multiplicação: ', num_1 * num_2)
        time.sleep(5)
    elif (op == 4 and num_2 != 0):
        print('Divisão: ', num_1 / num_2)
        time.sleep(5)
    elif(op > 4 or op < 1):
        print('Operação não aceita! \n Resultado = 0 \n')


runApp = 1
while(runApp == 1):
    print('\n1: Soma \n2: Subtração \n3: Multiplicação \n4: Divisão \n0: Sair')
    operacao = input('\nOpção: ')
    isNum = isInt(operacao)

    if(isNum):
        operacao = int(operacao) #Convert str to int

        if (operacao >= 1 and operacao <= 4):

            numero_1 = int(input('\nColoque o primeiro número: '))
            numero_2 = int(input('Coloque o segundo número: '))
            print('\n\nResultado: ')
            calculadora(numero_1, numero_2, operacao)

        elif(operacao == 0):
            print('Desligando!')
            runApp -= 1

        else:
            print('\n\n\n\n\n Essa opção não existe!')
