import pandas as pd
def formatar(valor):
  return "{:.2f}%".format(valor)
vacinas = pd.Series([30000000, 25000000, 10000000, 5000000])
populacao = pd.Series([213317639, 214477744, 215574303, 216687971])
soma1 = vacinas.sum()
media_pop_vac = vacinas.mean()
soma2 = populacao.sum()
media_pop_br = populacao.mean()
taxa_vac = ((vacinas/populacao) * 100).apply(formatar)
print("-------------- Dados da Vacinação -------------")
print(f"Total de Vacinados {vacinas.sum()}")
print(f"Média de Vacinados {vacinas.mean():.0f}")

print("--------------- Dados da População --------------")
print(f"Total da População {populacao.sum()}")
print(f"Média da População {populacao.mean():.0f}")

print("\n---- Taxa de Vacinação ----")
print(f"{taxa_vac}")
