# Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. 
# O arquivo deve ter a seguinte estrutura:

#aluno: Nome do aluno;
#nota_1: Primeira nota;
#nota_2: Segunda nota;
#faltas: Número de faltas;

# O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, 
# que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

# O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. 
# O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

#Por fim, o programa deverá mostrar na tela:
#- o maior número de faltas;
#- a média geral das notas dos alunos;
#- e a maior média.

import pandas as pd

df = pd.read_csv('notas_alunos.csv', names=['nome', 'nota1', 'nota2', 'faltas', 'media', 'aprovacao'], header=None)
df = df.iloc[1: , :]

df['media'] = (df['nota1'].astype('int') + df['nota2'].astype('int')) / 2

df.loc[df['media'] >= 7, 'aprovacao'] = 'aprovado'
df.loc[df['media'] < 7, 'aprovacao'] = 'reprovado'

df.to_csv('alunos_situacao.csv')

print("\n\nMaior número de faltas: ", df['faltas'].max())
print("\nMédia geral: ", df['media'].mean())
print("\nMaior média: ", df['media'].max())