soma = 0
media = 0
for i in range(5):
    idade = int(input("informe a idade: "))
    nome = input("informe o nome: ")
    soma = soma + idade
media = soma / (i + 1)
print(f"A soma é {soma}")
print(f"A média é {media:.0f}")