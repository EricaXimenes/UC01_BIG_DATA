import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame 
df_crimes = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_cvli = df_crimes[['cvli','aisp']]
df_cvli = df_cvli.groupby(['aisp']).sum(['cvli']).reset_index()

# Exibindo a base de dados do cvli
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_cvli.head())

# Criando o array do cvli
array_cvli = np.array(df_cvli["cvli"])

# Obtendo a média cvli
media_cvli = np.mean(array_cvli)

# Obtendo a mediana cvli
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana cvli
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) * 100

# Obtendo o máximo e o mínimo do cvli
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude do do cvli
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis do do cvli - Método weibull
q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli

# Identificando os outliers superiores e inferiores do cvli
limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame do cvli
df_cvli_outliers_superiores = df_cvli[df_cvli['cvli'] > limite_superior_cvli]
df_cvli_outliers_inferiores = df_cvli[df_cvli['cvli'] < limite_inferior_cvli]

# Obtendo as medidas de dispersão do do cvli
variancia_cvli = np.var(array_cvli)
distancia_var_cvli = variancia_cvli / (media_cvli**2)
desvio_padrao_cvli = np.std(array_cvli)
coeficiente_var_cvli = desvio_padrao_cvli / media_cvli


# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS CRIMES VIOLENTOS LETAIS INTERNACIONAIS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos crimes é {media_cvli:.0f}")
print(f"A mediana dos crimes é {mediana_cvli:.0f}")
print(f"A distância entre a média e a mediana é {distancia_cvli:.2f} %")
print(f"O menor valor dos crimes é {minimo_cvli:.0f}")
print(f"O maior valor dos crimes é {maximo_cvli:.0f}")
print(f"A amplitude dos valores dos crimes é {amplitude_cvli:.0f}")
print(f"O valor do q1 - 25% dos crimes é {q1_cvli:.0f}")
print(f"O valor do q2 - 50% dos crimes é {q2_cvli:.0f}")
print(f"O valor do q3 - 75% dos crimes é {q3_cvli:.0f}")
print(f"O valor do iqr = q3 - q1 dos crimes é {iqr_cvli:.0f}")
print(f"O limite inferior dos crimes é {limite_inferior_cvli:.0f}")
print(f"O limite superior dos crimes é {limite_superior_cvli:.0f}")
print(f"A variância dos crimes é {variancia_cvli:.0f}")
print(f"A distância da variância X média dos crimes é {distancia_var_cvli:.0f}")
print(f"O desvio padrão dos crimes é {desvio_padrao_cvli:.0f}")
print(f"O coeficiente de variação dos crimes é {coeficiente_var_cvli:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_cvli_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_cvli_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_cvli_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_cvli_outliers_superiores)

# Visualizando os dados sobre os crimes violentos letais internacionais
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre os crimes violentos letais internacionais')

# posição 01: Gráfico dos crimes violentos letais internacionais
plt.subplot(2,2,1)
plt.title('BoxPlot dos crimes violentos letais internacionais')
plt.boxplot(array_cvli,vert=False,showmeans=True )




# posição 02: Histograma dos crimes violentos letais internacionais
plt.subplot(2,2,2)
plt.title('Histograma os crimes violentos letais internacionais')
plt.hist(array_cvli,bins=100,edgecolor='green', color='yellow')

# posição 03: Medidas dos crimes violentos letais internacionais
plt.subplot(2,2,3)
df_cvli_outliers_superiores_order = df_cvli_outliers_superiores.sort_values(by='cvli',ascending=True)
plt.title('Ranking dos Batalhoes de PM com Outliers Superiores')
plt.barh(df_cvli_outliers_superiores_order['aisp'].astype(str),df_cvli_outliers_superiores_order['cvli'], edgecolor='black', color='red')

# posição 04: Medidas descritivas dos crimes violentos letais internacionais
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos crimes violentos letais internacionais')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Recuperações de Veículos {media_cvli:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Recuperações de Veículos {mediana_cvli:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Recuperações de Veículos {distancia_cvli:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Recuperações de Veículos {maximo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Recuperações de Veículos {minimo_cvli:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Recuperações de Veículos {distancia_var_cvli:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Recuperações de Veículos {coeficiente_var_cvli:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()