import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_roubo_veiculos = df_ocorrencias[['cisp','roubo_veiculo']] #filtrar dados
df_roubo_veiculos = df_roubo_veiculos.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()
print('\n-------- OBTENDO DADOS GERAIS SOBRE OCORRÊNCIAS ---------')

print(df_roubo_veiculos.head())

# Criando o array dos roubos
array_roubo_veiculos = np.array(df_ocorrencias["roubo_veiculo"])

media_roubos = np.mean(array_roubo_veiculos)
mediana_roubos = np.median(array_roubo_veiculos)
distancia_roubos = abs((media_roubos - mediana_roubos) / mediana_roubos) * 100
maximo_roubos = np.max(array_roubo_veiculos)
minimo_roubos = np.min(array_roubo_veiculos)
amplitude_roubos = maximo_roubos - minimo_roubos

# Obtendo os Quartis do roubo - Método weibull
q1_roubo_veiculos = np.quantile(array_roubo_veiculos, 0.25, method='weibull')
q2_roubo_veiculos = np.quantile(array_roubo_veiculos, 0.50, method='weibull')
q3_roubo_veiculos = np.quantile(array_roubo_veiculos, 0.75, method='weibull')
iqr_roubo_veiculos = q3_roubo_veiculos - q1_roubo_veiculos

limite_superior_roubo_veiculos = q3_roubo_veiculos + (1.5 * iqr_roubo_veiculos)
limite_inferior_roubo_veiculos = q1_roubo_veiculos - (1.5 * iqr_roubo_veiculos)

df_roubo_veiculos_outliers_superiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] > limite_superior_roubo_veiculos]
df_roubo_veiculos_outliers_inferiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] < limite_inferior_roubo_veiculos]

variancia_roubo_veiculos = np.var(array_roubo_veiculos)
distancia_roubo_veiculos = variancia_roubo_veiculos / (media_roubos**2)
desvio_padrao_roubo_veiculos = np.std(array_roubo_veiculos)
coeficiente_var_roubo_veiculos = desvio_padrao_roubo_veiculos / media_roubos


# Exibindo os dados sobre os valores dos roubos
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS --")
print('------------------- Medidas de Tendência Central -------------------------------')
print(f"\nA média dos roubos são: {media_roubos:.2f}")
print(f"A mediana dos roubos são: {mediana_roubos:.2f}")
print(f"A distância entre a média e a mediana é: {distancia_roubos:.2f} %")
print(f"A menor taxa de roubos são: {minimo_roubos:.2f}")
print(f"A maior taxa de roubos são:  {maximo_roubos:.2f}")
print(f"A amplitude dos valores dos roubos são: {amplitude_roubos:.2f}")
print(f"O valor do q1 - 25% do valor dos roubos é: {q1_roubo_veiculos:.2f}")
print(f"O valor do q2 - 50% do valor dos roubos é: {q2_roubo_veiculos:.2f}")
print(f"O valor do q3 - 75% do valor dos roubos é: {q3_roubo_veiculos:.2f}")
print(f"O valor do iqr = q3 - q1 do valor dos roubos é: {iqr_roubo_veiculos:.2f}")
print(f"O limite inferior do valor dos roubos é: {limite_inferior_roubo_veiculos:.2f}")
print(f"O limite superior do valor dos roubos é: {limite_superior_roubo_veiculos:.2f}")
print(f"A Variância dos roubos é: {variancia_roubo_veiculos:.2F}")
print(f"A distância da Variância X média dos roubos é: {distancia_roubo_veiculos:.2f}")
print(f"O desvio padrão dos roubos é: {distancia_roubo_veiculos:.2f}")
print(f"O Coeficiente de variação dos roubos é: {coeficiente_var_roubo_veiculos:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_veiculos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculos_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_veiculos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculos_outliers_superiores)
    print('\nVISUALIZANDO OS DADOS...')

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Roubos de Veículos')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.xticks([])
plt.title('BoxPlot dos Roubos de Veículos')
plt.boxplot(df_roubo_veiculos_outliers_superiores,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.xticks([])
plt.title('Histograma dos Roubos de Veículos')
plt.hist(df_roubo_veiculos_outliers_superiores,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_roubo_veiculo_outliers_superiores_order = df_roubo_veiculos_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.title('Ranking das Delegacias com Outliers Superiores')
plt.barh(df_roubo_veiculo_outliers_superiores_order['cisp'].astype(str),df_roubo_veiculo_outliers_superiores_order['roubo_veiculo'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Roubos de Veículos {media_roubos:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Roubos de Veículos {mediana_roubos:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Roubos de Veículos {distancia_roubos:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Roubos de Veículos {maximo_roubos:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Roubos de Veículos {minimo_roubos:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos Roubos de Veículos {distancia_roubo_veiculos:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Roubos de Veículos {coeficiente_var_roubo_veiculos:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()