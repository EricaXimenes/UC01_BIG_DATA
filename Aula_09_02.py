import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Titanic.csv'

df_titanic = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

print('\n-------EXIBINDO A BASE DE DADOS ---------')
print(df_titanic.head())

#Obtendo dados sobre tarifas 
array_tarifas_passageiros = np.array(df_titanic["Fare"])
array_idades = np.array(df_titanic["Age"])
array_nome = np.array(df_titanic["Name"])

#Obtendo média e mediana do valor das passagens.
media_tarifas = np.mean(array_tarifas_passageiros)
mediana_tarifas = np.median(array_tarifas_passageiros)
distancia_tarifas = abs((media_tarifas - mediana_tarifas) / mediana_tarifas)* 100

#OBTENDO O MÁXIMO E MINIMO DO VALOR DAS PASSAGENS
maximo_tarifas = np.max(array_tarifas_passageiros)
minimo_tarifas = np.min(array_tarifas_passageiros)
amplitude_tarifas = maximo_tarifas - minimo_tarifas

#OBTENDO MÉDIA E MEDIANA
media_idades = np.mean(array_idades)
mediana_idades = np.median(array_idades)
distancia_idades = abs((media_idades - mediana_idades) / mediana_idades)* 100

#OBTENDO O MÁXIMO E MINIMO DAS IDADES
maior_idades = np.max(array_idades)
menor_idades = np.min(array_idades)
amplitude_idades = maior_idades - menor_idades

# Obtendo os Quartis da tarifa - Método weibull
q1_tarifas = np.quantile(array_tarifas_passageiros, 0.25, method='weibull')
q2_tarifas = np.quantile(array_tarifas_passageiros, 0.50, method='weibull')
q3_tarifas = np.quantile(array_tarifas_passageiros, 0.75, method='weibull')
iqr_tarifas = q3_tarifas - q1_tarifas


# Obtendo os Quartis das idades - Método weibull
q1_idade = np.quantile(array_idades, 0.25, method='weibull')
q2_idade = np.quantile(array_idades, 0.50, method='weibull')
q3_idade = np.quantile(array_idades, 0.75, method='weibull')
iqr_idade = q3_idade - q1_idade

# Identificando os outliers superiores e inferiores da tarifa
limite_superior_tarifa = q3_tarifas + (1.5 * iqr_tarifas)
limite_inferior_tarifa = q1_tarifas - (1.5 * iqr_tarifas)

# Identificando os outliers superiores e inferiores das idades
limite_superior_idades = q3_idade + (1.5 * iqr_idade)
limite_inferior_idades = q1_idade - (1.5 * iqr_idade)

# Filtrando o DataFrame Tarifas
df_tarifa_outliers_superiores = df_titanic[df_titanic['Fare'] > limite_superior_tarifa]
df_tarifa_outliers_inferiores = df_titanic[df_titanic['Fare'] < limite_inferior_tarifa]

# Filtrando o DataFrame Idades
df_idade_outliers_superiores = df_titanic[df_titanic['Age'] > limite_superior_idades]
df_idade_outliers_inferiores = df_titanic[df_titanic['Age'] < limite_inferior_idades]

print('\n--------------------- DADOS DE EMBARQUE -------------------------')
print('\nMedidas de Tendência Central')
print(f"A média das tarifas pagas pelos passageiros é R$ {media_tarifas:.2f}")
print(f"A mediana das tarifas pagas pelos passageiros é R$ {mediana_tarifas:.2f}")
print(f"A distância entre a média e a mediana é {distancia_tarifas:.2f}")
print(f"O maior valor das passagens é R${maximo_tarifas:.2f}")
print(f"O menor valor das passagens é R${minimo_tarifas:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_tarifas:.2f}")
print(f"O valor do q1 - 25% da tarifa é R$ {q1_tarifas}")
print(f"O valor do q2 - 50% da tarifa é R$ {q2_tarifas}")
print(f"O valor do q3 - 75% da tarifa é R$ {q3_tarifas}")
print(f"O valor do iqr = q3 - q1 da tarifa é R$ {iqr_tarifas}")
print(f"O limite inferior da tarifa é R$ {limite_inferior_tarifa}")
print(f"O limite superior da tarifa é R$ {limite_superior_tarifa}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_tarifa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_tarifa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_tarifa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_tarifa_outliers_superiores)
print('\n')
print(f"A média das idades dos passageiros é {media_idades:.0f}")
print(f"A mediana das idades dos passageiros é {mediana_idades:.0f}")
print(f"A distância entre a média e a mediana  das idades é {distancia_idades:.0f}")
print(f"A maior idades dos passageiros é {maior_idades:.0f}")
print(f"O menor idade dos passageeiros é {menor_idades:.0f}")
print(f"A amplitude dos valores das idades é {amplitude_idades:.0f}")
print(f"O valor do q1 - 25% da idade é {q1_idade:.0f}")
print(f"O valor do q2 - 50% da idade é {q2_idade:.0f}")
print(f"O valor do q3 - 75% da idade é {q3_idade:.0f}")
print(f"O valor do iqr = q3 - q1 da idade é {iqr_idade:.0f}")
print(f"O limite inferior da idade é {limite_inferior_idades:.0f}")
print(f"O limite superior da idade é {limite_superior_idades:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_idade_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_idade_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_idade_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_idade_outliers_superiores)