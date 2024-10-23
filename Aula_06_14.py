import pandas as pd
#IMPORTANDO A BASE DE DADOS
endereco_dados = 'BASES\Funcionarios.csv'
#CRIANDO DATAFRAME
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')
#EXIBINDO OS DADOS DO DATAFRAME
media_salario = df_funcionarios['Salário'].mean(axis=0)
media_idades = df_funcionarios['Idade'].mean(axis=0)
maior_tempo = df_funcionarios ['Tempo'].max(axis=0)
menor_tempo = df_funcionarios ['Tempo'].min(axis=0)
diferenca_tempo = maior_tempo - menor_tempo
media_tempo_casa = df_funcionarios['Tempo'].mean(axis=0)
func_tempo_velho = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
func_tempo_novo = df_funcionarios[df_funcionarios['Tempo'] == menor_tempo]['Nome']
qtd_funcionarios = df_funcionarios['Nome'].count()
maior_salario = df_funcionarios['Salário'].max(axis=0)
func_maior_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']

# Exibindo os Dados
print('\n---- DADOS DOS FUNCIONÁRIOS ----')
print(df_funcionarios.head())
print('\n---- DADOS SOLICITADOS ----')
print(f"A média de salários foi {media_salario:.2f}")
print(f"A média de idades foi {media_idades:.0f} anos.")
print(f"O maior Tempo de Casa é {maior_tempo} anos.")
print(f"O menor Tempo de Casa é {menor_tempo} anos.")
print(f"A diferença de tempodedores é {diferenca_tempo} anos.")
print(f"A média de tempo de empresa é {media_tempo_casa:.0f} anos")
print(f"O Funcionário com maior tempo é {func_tempo_velho.to_string(index=False)}")
print(f"O Funcionário com menor tempo é {func_tempo_novo.to_string(index=False)}")
print(f"A quantidade de funcionários são {qtd_funcionarios}")
print(f"O funcionário com maior salário é {func_maior_salario.to_string(index=False)}.")


