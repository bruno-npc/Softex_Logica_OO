#Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
#O método deve:

#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números.

import operacoes

cond = 0

print("Esta Funcionando")
print("---------CALCULADORA--------")
print("- [1]- Adição              -")
print("- [2]- Subtração           -")
print("- [3]- Divisao             -")
print("- [4]- Multiplicacao       -")
print("----------------------------")

while cond == 0:
    escolha = int(input("Escolha Uma Opção: "))
    if escolha >= 1 and escolha <= 4:
        cond = 1
    else:
        print("Opção Invalida !!")

Valor1 = float(input("Escolha O Valor 1: "))
Valor2 = float(input("Escolha O Valor 2: "))

final = resul = operacoes.operacoes.operar(Valor1, Valor2, escolha)

print("Resultado: ", final)
