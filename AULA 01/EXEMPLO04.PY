# calular = idade de uma pessoa a partir do ano de nascimento
import datetime
data_atual = datetime.date.today()
nome = input("informe o seu nome: ")
ano_nasc = int(input("forneça o ano de nascimento: "))
idade = data_atual.year - ano_nasc
print("Sr(a) ", nome, "sua idade é: ",idade,"anos.")