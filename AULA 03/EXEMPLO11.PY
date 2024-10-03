idade = int(input("Informe a idade: "))
if idade < 18:
    print("Você é Menor de idade")
elif idade ==18:
    print("Quase lá")
elif idade > 18 and idade < 65:
    print("acesso liberaddo - Aprecie com moderação")
else:
    print("Acesso Liberado")