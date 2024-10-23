import pandas as pd

alunos = [ 
  ['João',18,100],
  ['Maria',15,80],
  ['Antonia',18,100],
  ['Erica',20,60],
  ['Pedro',16,10],
]

#Criando as colunas da tabela alunos
colunas = ['nome', 'idade', 'média']
#Criando o dataFrame
df_alunos = pd.DataFrame(alunos,columns=colunas)
#exibindo os dados
print(df_alunos)

soma_idade = df_alunos['idade'].sum(axis=0)
media_idade = df_alunos['idade'].mean(axis=0)
maior_idade = df_alunos['idade'].max(axis=0)
menor_idade = df_alunos['idade'].min(axis=0)
maior_nome = df_alunos[df_alunos['idade'] == maior_idade]['nome']
menor_nome = df_alunos[df_alunos['idade'] == menor_idade]['nome']

soma_media = df_alunos['média'].sum(axis=0)
media_media = df_alunos['média'].mean(axis=0)
maior_media = df_alunos['média'].max(axis=0)
menor_media = df_alunos['média'].min(axis=0)
maior_media_nome = df_alunos[df_alunos['média'] == maior_media]['nome']
menor_media_nome = df_alunos[df_alunos['média'] == menor_media]['nome']

#Exibindo os calculos das idades
print("\n-- Informações sobre as idades dos alunos --")
print(f"Soma das idades:{soma_idade} anos")
print(f"Média das idades:{media_idade:.0f} anos")
print(f"Maior idade:{maior_idade} anos")
print(f"Menor idade:{menor_idade} anos")
print(f"O nome do aluno mais velho é:{maior_nome.values[0]}")
print(f"O nome do aluno mais novo é:{menor_nome.values[0]}")

#Exibindo os calculos das médias
print("\n-- Informações sobre as Média dos alunos --")
print(f"Soma das médias é:{soma_media:.1f} anos")
print(f"Média da turma é::{media_media:.1f} anos")
print(f"Maior idade:{maior_media:.1f} anos")
print(f"Menor idade:{menor_media:.1f} anos")
print(f"O nome do aluno com maior média: {maior_media_nome.values[0]}")
print(f"O nome do aluno com menor média: {menor_nome.values[0]}")