try:
   idade = int(input("forneça a sua idade: "))
   ano_empresa_year = int(input(" forneça os anos trabalhados: "))
except ValueError:
   print("verifique os dados informados")
else:
    if idade >=65:
        print("está apto para a aposentadoria")
    elif ano_empresa_year >=30:
        print("está apto para aposentadoria")
    elif idade >=60 and ano_empresa_year >=25:
        print("está apto para aposentadoria")
    else:
        print("está inapto a aposentadoria")
    