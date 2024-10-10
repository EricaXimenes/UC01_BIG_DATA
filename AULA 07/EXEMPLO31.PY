# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que armazene em um vetor um conjunto indeterminado de temperaturas, ao final informe a menor, a maior e a média das temperaturas.

temp = []
resp = "S"
while resp == "S" or resp == "s":
    temp.append(float(input("Informe a temperatura: ")))
    resp = input("Deseja Continuar(S/N)? ")
print(f"A menor temperatura registrada foi {min(temp)} ºC")
print(f"A maior temperatura registrada foi {max(temp)} ºC")
print(f"A temperatura média registrada foi {(sum(temp)/len(temp)):.1f} ºC")