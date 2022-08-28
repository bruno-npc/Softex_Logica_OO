#Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.


def categoriaHabilitacao (roda, peso, qtdPessoas):
    if roda < 4:
        print("A melhor categoria de habilitação para o veículo informado é: A")
    elif roda == 4 and qtdPessoas <= 8 and peso <= 3500:
        print("A melhor categoria de habilitação para o veículo informado é: B")
    elif roda >= 4 and peso > 3500 and peso <= 6000 :
        print ("A melhor categoria de habilitação para o veículo informado é: C")
    elif roda >= 4 and qtdPessoas > 8 and peso < 6000:
        print ("A melhor categoria de habilitação para o veículo informado é: D")
    elif roda >= 4 and peso > 6000 :
        print ("A melhor categoria de habilitação para o veículo informado é: E")
    else:
        print ("Categoria de veiculo não encontrada.")


print("#######Caracteristicas do veículo#########")

print("Digite a quantidade de rodas: ")
roda = int(input())

print("Digite o peso bruto em kg: ")
peso = float(input())

print("Digite a quantidade de pessoas que podem ocupar o veículo: ")
qtdPessoas = int(input())

categoriaHabilitacao(roda, peso, qtdPessoas)



