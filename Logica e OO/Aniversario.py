#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
from ast import If
from datetime import date

def calcularAno(dataAniversario): 
    hoje = date.today() 
    ano = hoje.year - dataAniversario.year - ((hoje.month, hoje.day) < (dataAniversario.month, dataAniversario.day)) 
    return ano

def takeData (): 
    try:
        dia = int(input('Informe seu dia de nascimento: '))
        mes = int(input('Informe seu mês de nascimento: '))
        ano = int(input('Informe seu ano de nascimento: '))
        return dia, mes, ano
    except:
        return 'Data informada não é valida!'

def mesesAniversario (mes):
    hoje = date.today()
    mesAniversario = mes - hoje.month
    return mesAniversario

runApp = 1
while(runApp):

    nome = input('Informe seu nome: ')
    data = takeData()

    if(data[2] >= 1922 and data[2] <= 2021):
        print('\n\n',nome, ' você tem:')
        print(calcularAno(date(data[2], data[1], data[0])), 'anos!')

        mesA = mesesAniversario(data[1])
        if (mesA > 0):
            print('\nFaltam: ', mesA, 'meses para o seu aniversário!')
            runApp = 0
        else:
            mesA = mesA * -1
            print('Seu aniversario foi a ', mesA, 'meses atrás.')
            runApp = 0
    else:
        print('Ano de nascimento inválido.')
