#Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. 
#Depois, desenvolva três ou mais objetos para testar o código.
from Concecionaria import Carro


carro1 = Carro(modelo='teste1', ano=2005, potencia=70)
carro2 = Carro(modelo='teste2', ano=2012, potencia=80)
carro3 = Carro(modelo='teste3', ano=2016, potencia=50)

carro1.mostrar_modelo()
carro1.nome_dono('joão')
carro1.atualizacao_potencia(80)

carro2.mostrar_modelo()
carro2.nome_dono('Ana')
carro2.atualizacao_potencia(100)

carro3.mostrar_modelo()
carro3.nome_dono('Andre')
carro3.atualizacao_potencia(70)