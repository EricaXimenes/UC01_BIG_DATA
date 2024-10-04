import datetime
data_atual = datetime.date.today()
try:
   nome = input("informe seu nome: ")
   nasc = int(input("informe o ano de nascimento: "))
   ano = int(input("forneça o ano que entrou na empresa : "))
except ValueError:
   print("verifique os dados informados")
else:
    nasc = data_atual.year - nasc
    tempo = data_atual.year - ano
    if nasc >= 65:
        print(f"{nome}, está apto para a aposentadoria")
    elif tempo >= 30:
        print(f"{nome}, você está apto para aposentadoria")
    elif nasc >= 60 and tempo >= 25:
        print(f"{nome}, você está apto para aposentadoria")
    else:
        print(f"{nome}, você está inapto a aposentadoria")