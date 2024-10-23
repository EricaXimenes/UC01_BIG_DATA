import pandas as pd
#IMPORTANDO A BASE DE DADOS
endereco_dados = 'BASES\Financeira.csv'
#CRIANDO DATAFRAME
df_financeira = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')
#EXIBINDO OS DADOS DO DATAFRAME
print('---------- DADOS FINANCEIROS ----------')
print(df_financeira.head())