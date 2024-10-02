# CALCULO PRESTAÇÃO
prestacao = float(input(" Informe o valor da prestação: "))
taxa = float(input("Informe a taxa: "))
tempo = int(input("Informe os meses em atraso: "))
valor_final = prestacao+(prestacao*(taxa/100)*tempo)
print(f"O valor em atraso será de R${valor_final:.2f}")