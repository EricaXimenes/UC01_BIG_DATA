import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_lesao_corp_dolosa = df_ocorrencias[['cisp','lesao_corp_dolosa']]
df_lesao_corp_dolosa = df_lesao_corp_dolosa.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()
df_lesao_corp_dolosa = df_lesao_corp_dolosa[df_lesao_corp_dolosa['ano'].isin([2022,2023,2024])]
df_lesao_corp_culposa = df_ocorrencias[['cisp','lesao_corp_culposa']]
df_lesao_corp_culposa = df_lesao_corp_culposa.groupby(['cisp']).sum(['lesao_corp_culposa']).reset_index()
df_lesao_corp_dolosa_ano = df_ocorrencias[['aisp', 'ano', 'lesao_corp_dolosa']]
df_lesao_corp_dolosa_ano = df_lesao_corp_dolosa.groupby(['ano']).sum(['lesao_corp_dolosa']).reset_index()


# Exibindo a base de dados lesão corporal dolosa
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesao_corp_dolosa.head())

# Criando o array das lesões corporais dolosas
array_lesao_corp_dolosa = np.array(df_lesao_corp_dolosa["lesao_corp_dolosa"])

# Obtendo a média das lesões corporais dolosas
media_lesao_corp_dolosa = np.mean(array_lesao_corp_dolosa)

# Obtendo a mediana das lesões corporais dolosa
mediana_lesao_corp_dolosa = np.median(array_lesao_corp_dolosa)

# Obtendo a distância entre a média e a mediana das lesões corporais dolosa
distancia_lesao_corp_dolosa = abs((media_lesao_corp_dolosa - mediana_lesao_corp_dolosa) / mediana_lesao_corp_dolosa) * 100

# Obtendo o máximo e o mínimo das lesões corporais dolosas
maximo_lesao_corp_dolosa = np.max(array_lesao_corp_dolosa)
minimo_lesao_corp_dolosa = np.min(array_lesao_corp_dolosa)

# Obtendo a amplitude das leões corporais dolosas
amplitude_lesao_corp_dolosa = maximo_lesao_corp_dolosa - minimo_lesao_corp_dolosa

# Obtendo os Quartis das lesões corporais dolosas - Método weibull
q1_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.25, method='weibull')
q2_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.50, method='weibull')
q3_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.75, method='weibull')
iqr_lesao_corp_dolosa = q3_lesao_corp_dolosa - q1_lesao_corp_dolosa

# Identificando os outliers superiores e inferiores das lesões corporais dolosas
limite_superior_lesao_corp_dolosa = q3_lesao_corp_dolosa + (1.5 * iqr_lesao_corp_dolosa)
limite_inferior_lesao_corp_dolosa = q1_lesao_corp_dolosa - (1.5 * iqr_lesao_corp_dolosa)

# Filtrando o DataFrame lesão corporal dolosa
df_lesao_corp_dolosa_outliers_superiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_corp_dolosa]
df_lesao_corp_dolosa_outliers_inferiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] < limite_inferior_lesao_corp_dolosa]

# Obtendo as medidas de dispersão lesão corporaç dolosa
variancia_lesao_corp_dolosa = np.var(array_lesao_corp_dolosa)
distancia_var_lesao_corp_dolosa = variancia_lesao_corp_dolosa / (media_lesao_corp_dolosa**2)
desvio_padrao_lesao_corp_dolosa = np.std(array_lesao_corp_dolosa)
coeficiente_var_lesao_corp_dolosa = desvio_padrao_lesao_corp_dolosa / media_lesao_corp_dolosa

# Obtendo a correlação entre os 
# 0,9 a 1,0 (positivo ou negativo): correlação muito forte;
# 0,7 a 0,9 (positivo ou negativo): correlação forte;
# 0,5 a 0,7 (positivo ou negativo): correlação moderada;
# 0,3 a 0,5 (positivo ou negativo): correlação fraca;
# 0,0 a 0,3 (positivo ou negativo): não possui correlação.
correlacao_culposa_dolosa = np.corrcoef(df_lesao_corp_dolosa['lesao_corp_dolosa'],df_lesao_corp_culposa['lesao_corp_culposa'])[0,1]

# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE LESÃO CORPORAL DOLOSO -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das lesões corporais dolosas é {media_lesao_corp_dolosa:.0f}")
print(f"A mediana das lesões corporais dolosas é {mediana_lesao_corp_dolosa:.0f}")
print(f"A distância entre a média e a mediana lesões corporais dolosas é {distancia_lesao_corp_dolosa:.2f} %")
print(f"O menor valor das lesões corporais dolosas é {minimo_lesao_corp_dolosa:.0f}")
print(f"O maior valor das lesões corporais dolosas é {maximo_lesao_corp_dolosa:.0f}")
print(f"A amplitude dos valores das lesões corporais dolosas é {amplitude_lesao_corp_dolosa:.0f}")
print(f"O valor do q1 - 25% das lesões corporais dolosas é {q1_lesao_corp_dolosa:.0f}")
print(f"O valor do q2 - 50% das lesões corporais dolosas é {q2_lesao_corp_dolosa:.0f}")
print(f"O valor do q3 - 75% das lesões corporais dolosas é {q3_lesao_corp_dolosa:.0f}")
print(f"O valor do iqr = q3 - q1 das lesões corporais dolosas é {iqr_lesao_corp_dolosa:.0f}")
print(f"O limite inferior das lesões corporais dolosas é {limite_inferior_lesao_corp_dolosa:.0f}")
print(f"O limite superior das lesões corporais dolosas é {limite_superior_lesao_corp_dolosa:.0f}")
print(f"A variância das lesões corporais dolosas é {variancia_lesao_corp_dolosa:.0f}")
print(f"A distância da variância X média das lesões corporais dolosas é {distancia_var_lesao_corp_dolosa:.0f}")
print(f"O desvio padrão das lesões corporais dolosas é {desvio_padrao_lesao_corp_dolosa:.0f}")
print(f"O coeficiente de variação das lesões corporais dolosas é {coeficiente_var_lesao_corp_dolosa:.0f}")
print(f"A correlação das lesões corporais dolosas e lesões corporais culposas é {correlacao_culposa_dolosa:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_lesao_corp_dolosa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesao_corp_dolosa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_lesao_corp_dolosa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_lesao_corp_dolosa_outliers_superiores)

# Visualizando os dados sobre Lesões corporais dolosas
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre lesões corporais dolosas')

# posição 01: Gráfico das lesões corporais dolosas
plt.subplot(2,2,1)
plt.title('BoxPlot dos lesões corporais dolosas')
plt.boxplot(array_lesao_corp_dolosa,vert=False,showmeans=True)

# posição 02: Histograma das lesões corporais dolosa
plt.subplot(2,2,2)
plt.title('Comparativo Lesão corporal Dolosas e Culposas')
plt.scatter(df_lesao_corp_dolosa['lesao_corp_dolosa'],df_lesao_corp_culposa['lesao_corp_culposa'])
plt.xlabel('Lesão corporal Dolosa')
plt.ylabel('Lesão corporal culposa')

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# Criando o gráfico de dispersão com mapa de cores
plt.scatter(x, y, c=z, cmap='viridis')
plt.colorbar() # Adiciona uma barra de cores para referência


# Criando o gráfico de dispersão com mapa de cores
plt.scatter(x, y, cmap='viridis')
plt.colorbar() # Adiciona uma barra de cores para referência
plt.show()
# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_lesao_corp_dolosa_outliers_superiores_order = df_lesao_corp_dolosa_outliers_superiores.sort_values(by='lesao_corp_dolosa',ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_lesao_corp_dolosa_outliers_superiores_order['cisp'].astype(str),df_lesao_corp_dolosa_outliers_superiores_order['lesao_corp_dolosa'])
plt.plot(df_lesao_corp_dolosa_ano['ano'].astype(str),df_lesao_corp_dolosa_ano['lesao_corp_dolosa'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas de lesões corporais dolosas')
plt.axis('off')
plt.text(0.1,0.9,f'Média das Lesões corporais dolosas: {media_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das Lesões corporais dolosas: {mediana_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das Lesões corporais dolosas: {distancia_lesao_corp_dolosa:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das Lesões corporais dolosas: {maximo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das Lesões corporais dolosas: {minimo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das Lesões corporais dolosas: {distancia_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das Lesões corporais dolosas: {coeficiente_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre os das Lesões corporais dolosas e das Lesões corporais culposas: {correlacao_culposa_dolosa:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()