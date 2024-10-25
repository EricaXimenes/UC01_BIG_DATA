import pandas as pd
import numpy as np

print('--------- OBTENDO DADOS ---------')

endereco_dados = 'BASES\Titanic.csv'

df_tarifas = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')

print('\n-------EXIBINDO A BASE DE DADOS ---------')
print(df_tarifas.head())

#Obtendo dados sobre tarifas 
array_tarifas_passageiros = np.array(df_tarifas["Fare"])
array_idades = np.array(df_tarifas["Age"])

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
maximo_idades = np.max(array_idades)
minimo_idades = np.min(array_idades)
amplitude_idades = maximo_idades - minimo_idades

print('\n--------------------- DADOS DE EMBARQUE -------------------------')
print(f"A média das tarifas pagas pelos passageiros é R$ {media_tarifas:.2f}")
print(f"A mediana das tarifas pagas pelos passageiros é R$ {mediana_tarifas:.2f}")
print(f"A distância entre a média e a mediana é {distancia_tarifas:.2f}")
print(f"O maior valor das passagens é R${maximo_tarifas:.2f}")
print(f"O menor valor das passagens é R${minimo_tarifas:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_tarifas:.2f}")
print('\n')
print(f"A média das idades dos passageiros é {media_idades:.2f}")
print(f"A mediana das idades dos passageiros é {mediana_idades:.2f}")
print(f"A distância entre a média e a mediana  das idades é {distancia_idades:.2f}")
print(f"A maior idadesdos passageiros é {maximo_idades:.2f}")
print(f"O menor valor das passagens é R${minimo_idades:.2f}")
print(f"A amplitude dos valores das passagens é {amplitude_idades:.2f}")