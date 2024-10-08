soma = 0
maior = 0
for i in range(5):
    idade = int(input("informe a idade: "))
    nome = input("informe o nome: ")
    if idade > maior:
        maior = idade
    soma = soma + idade
media = soma / (i + 1)
print(f"A soma é {soma}")
print(f"A média é {media:.0f}")
print(f"A maior idade é {maior}")
