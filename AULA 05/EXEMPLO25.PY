soma_m = 0
soma_f = 0
maior = 0
cont_m = 0
cont_f = 0
for i in range(5):
    idade = int(input("informe a idade: "))
    nome = input("informe o nome: ")
    sexo = input("informe o sexo: ")
    if idade > maior:
       maior = idade
    if sexo == "M" or sexo == "m":
        soma_m = soma_m + idade
        cont_m += 1
    if sexo == "F" or sexo == "f":
        soma_f = soma_f + idade
        cont_f +=1   
media_m = soma_m / cont_m
media_f = soma_f / cont_f
print(f"A soma da idades dos homens é  {soma_m}")
print(f"A soma da idades das mulheres é  {soma_f}")
print(f"A média das idades dos homens é  {media_m}")
print(f"A média das idades das mulheres é  {media_f}")
print(f"A maior idade é {maior}")