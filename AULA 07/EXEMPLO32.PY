# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados: 
# - sexo (masculino e feminino) 
# - cor dos olhos (azuis, verdes ou castanhos) 
# - cor dos cabelos (louros, castanhos, pretos) 
# - idade 
# Faça um programa que determine e escreva: 
# a) a maior e a menor idade dos habitantes, assim como a média das idades; 
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive; 
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros; 


sexo = []
olhos = []
cabelos = []
idade = []
resp = "S"
qtd_sexo_idade = 0
qtd_olhos_cabelos = 0
while resp =="S" or resp == "s":
    sexo.append(input("Informe o sexo M - Masculino ou F - Feminino "))
    olhos.append(input("Informe a cor dos olhos A - Azuis, V - Verdes ou C - Castanhos "))
    cabelos.append(input("Informe a cor dos cabelos L - Louros, P - Pretos ou C - Castanhos "))
    idade.append(int(input("Informe a idade: ")))
    resp = input("Deseja Continuar(S/N)? ")
for i in range(len(sexo)):
    if (sexo[i] == "F" or sexo[i] == "f") and (idade >= 18 and idade <= 35):
        qtd_sexo_idade += 1
    if (olhos[i] == "V" or olhos[i]  == "v") and (cabelos[i] == "L" or cabelos[i] == "l"):
        qtd_olhos_cabelos += 1
print(f"A maior idade é {max(idade)} anos.")
print(f"A menor idade é {min(idade)} anos.")
print(f"A média das idades é {(sum(idade)/len(idade)):.0f} anos.")
print(f"A quantidade de pessoas do sexo feminino com idades entre 18 e 35 anos é {qtd_sexo_idade}")
print(f"A quantidade de pessoas que possuem cabelos louros e olhos verdes é {qtd_olhos_cabelos}")