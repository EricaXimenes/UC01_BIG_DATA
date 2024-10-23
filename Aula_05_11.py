# pip install xlrd - Biblioteca para manipular arquivos do Excel
# pip install openpyxl - Biblioteca para manipular arquivos do Excel
import pandas as pd
# Importando a Base de Dados
endereco_dados = 'BASES\ENEM_2020_2023.xlsx'
# Criando o DataFrame 
df_enem = pd.read_excel(endereco_dados)
# Exibindo os Dados do DataFrame
print('-- QUANTIDADE DE INSCRITOS NO ENEM 2020 A 2023 --')
print(df_enem.head())