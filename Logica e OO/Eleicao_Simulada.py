#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. 
# Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. 
# Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, 
# também, a quantidade de votos de cada candidato, os brancos e nulos 
import array
from ast import Try

candidatos = array.array("i", [0, 0, 0, 0])
eleicao = True

def finalizarEleicao():
    finalizar = input ('\nDeseja terminar a eleição? \n(Y) para sim  |  (N) para não.\n')
    print ("\n\nEscolha finalização: ", finalizar.lower())
    if finalizar.lower() != 'y' and finalizar.lower() != 'n':
        print('Digite apenas Y ou N.')
        finalizarEleicao()
    elif finalizar.lower() == 'y':
        print("\n\n\nFinalização da eleição!")
        contagemVotos()
    elif finalizar.lower() == 'n':
        print("Continuação da eleição!")

def contagemVotos():
    if candidatos[0] > candidatos[1] and candidatos[0] > candidatos[2]:
        print ("Candidato_X venceu com: ", candidatos[0], " Votos!\n")

    elif candidatos[1] > candidatos[0] and candidatos[1] > candidatos[2]:
        print ("Candidato_Y venceu com: ", candidatos[1], " Votos!\n")

    elif candidatos[2] > candidatos[0] and candidatos[2] > candidatos[1]:
        print ("Candidato_Z venceu com: ", candidatos[1], " Votos!\n")
    else:
        print("Nenhum candidato venceu!")

    print("\nRestante dos votos: \nCandidato_X: ", candidatos[0], " votos.")
    print("\nCandidato_Y: ", candidatos[1], " votos.")
    print("\nCandidato_Z: ", candidatos[2], " votos.")
    print("\nVotos em branco: ", candidatos[3])

    desligarUrna()

def desligarUrna():
    global eleicao
    eleicao = False

def isInt(voto):
    try:
        int(voto)
        return True
    except:
        return False

while(eleicao):
    print("\n\nCANDIDATOS: \n- candidato_X => 889 \n- candidato_Y => 847 \n- candidato_Z => 515 \n- branco => 0\n")
    voto = input('\n####### Divite seu voto #######\n')
    confirmVoto = isInt(voto)

    if confirmVoto == False:
        print ("\n\n\nDigite apenas números!")
    else:
        if voto == 889:
            print("Voto no candidato_X confirmado!")
            candidatos[0] += 1
            finalizarEleicao()
        elif voto == 847:
            print("Voto no candidato_Y confirmado!")
            candidatos[1] += 1
            finalizarEleicao()
        elif voto == 515:
            print("Voto no candidato_Z confirmado!")
            candidatos[2] += 1
            finalizarEleicao()
        else: 
            print("Voto em branco confirmado!")
            candidatos[3] += 1
            finalizarEleicao()