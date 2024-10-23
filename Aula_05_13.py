import pandas as pd

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

print('\n-------- OBTENDO DADOS GERAIS SOBRE OCORRÊNCIAS ---------')
print(df_ocorrencias.head())

#Criando o Dataframe Roubo de Veículos por Município
df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
print('\n-------- OBTENDO DADOS SOBRE ROUBOS DE VEÍCULOS ---------')
print(df_roubo_veiculo.head())

#Criando o Data frame homicidio doloso por ano
df_ano_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
df_ano_hom_doloso = df_ano_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
print('\n-------- OBTENDO DADOS SOBRE HOMICIDIO DOLOSO ---------')
print(df_ano_hom_doloso.head())

df_cisp_dol_culp = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_cisp_dol_culp = df_cisp_dol_culp.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()
print('\n-------- OBTENDO DADOS SOBRE HOMICIDIO DOLOSO E CULPOSO ---------')
print(df_cisp_dol_culp.head())