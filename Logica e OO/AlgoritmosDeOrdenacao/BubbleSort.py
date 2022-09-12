#Construa um algoritmo de ordenação, utilizando o método bubble sort estudado. 
#(Lembre-se que se trata de uma série de instruções que devem ser seguidas passo a passo).
#Para isso, você deve criar um método em que o tamanho do vetor seja dez e deve estar em ordem crescente.

#O vetor deverá:
#- comparar seus elementos dois a dois adjacentes;
#- se os elementos não estiverem em ordem, então ordenar;
#- senão, avançar para o próximo par;
#- repetir a operação até que nenhuma troca possa ser feita no vetor inteiro.

def sort (lista):
    for final in range (len(lista), 0, -1):
        for atual in range(0, final -1):
            if lista[atual] > lista[atual + 1]:
                lista[atual], lista[atual + 1] = lista[atual + 1], lista[atual]



lista = [7, 4, 1, 2, 3, 6, 9, 10, 5, 8]

sort(lista)
print("\n\nLista ordenada: ", lista, "\n\n")