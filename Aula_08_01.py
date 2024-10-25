import pandas as pd
import numpy as np 
#IMPORTANDO A BASE DE DADOS
endereco_dados = 'BASES\Funcionarios.csv'
#CRIANDO DATAFRAME
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

array_salarios = np.array(df_funcionarios["Salário"])
array_idades = np.array(df_funcionarios["Idade"])
array_tempo = np.array(df_funcionarios["Tempo"])

#EXIBINDO OS DADOS DO SALÁRIO
media_salarios = np.mean(array_salarios)
mediana_salarios = np.median(array_salarios)
distancia_salarios = abs((media_salarios - mediana_salarios) / mediana_salarios)* 100

maximo_salarios = np.max(array_salarios)
minimo_salarios = np.min(array_salarios)
amplitude_salarios = maximo_salarios - minimo_salarios

#EXIBINDO OS DADOS DAS IDADES
media_idades = np.mean(array_idades)
mediana_idades = np.median(array_idades)
distancia_idades = abs((media_idades - mediana_idades) / mediana_idades)* 100

maximo_idades = np.max(array_idades)
minimo_idades = np.min(array_idades)
amplitude_idades = maximo_idades - minimo_idades

#EXIBINDO OS DADOS DE TEMPO
media_tempo = np.mean(array_tempo)
mediana_tempo = np.median(array_tempo)
distancia_tempo = abs((media_tempo - mediana_tempo) / mediana_tempo)* 100


maximo_tempo = np.max(array_tempo)
minimo_tempo = np.min(array_tempo)
amplitude_tempo = maximo_tempo - minimo_tempo


# Exibindo os Dados
print('\n---- DADOS DOS FUNCIONÁRIOS ----')
print(df_funcionarios.head())
print('\n---- DADOS SOLICITADOS ----')
print(f"A média de salários foi R${media_salarios:.2f}")
print(f"A mediana de salários foi R${mediana_salarios:.2f}")
print(f"A distância entre a média e a mediana dos salários é {distancia_salarios:.2f}")
print(f"O maior salário é R${maximo_salarios:.2f}")
print(f"O menor salário é R${minimo_salarios:.2f}")
print(f"A amplitude dos valores dos salários é R${amplitude_salarios:.2f}")
print(f"A média das idades foi {media_idades:.0f}")
print(f"A mediana das idades foi {mediana_idades:.0f}")
print(f"A distância entre a média e a mediana das idades é {distancia_idades:.0f}")
print(f"A maior idade é {maximo_idades:.0f}")
print(f"A menor idade é {minimo_idades:.0f}")
print(f"A amplitude dos valores das idades é {amplitude_idades:.0f}")
print(f"A média dos tempos foi {media_tempo:.0f}")
print(f"A mediana dos tempos foi {mediana_tempo:.0f}")
print(f"A distância entre a média e a mediana dos tempos são {distancia_tempo:.0f}")
print(f"A maior idade é {maximo_tempo:.0f}")
print(f"A menor idade é {minimo_tempo:.0f}")
print(f"A amplitude dos valores das idades é {amplitude_tempo:.0f}")