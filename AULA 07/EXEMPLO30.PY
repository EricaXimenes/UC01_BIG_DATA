# Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao IRRF.
# c) quanto pagou ao INSS.
# d) quanto pagou ao sindicato.
# e) o salário líquido.

horas = int(input("Informe as Horas Trabalhas no Mês: "))
valor = float(input("Informe o Valor da Hora Trabalhada: "))
bruto = horas * valor
inss = bruto * 0.08
irrf = bruto * 0.11
sindicato = bruto * 0.05
liquido = bruto - (inss + irrf + sindicato)
print(f"O salário bruto é R$ {bruto:.2f}")
print(f"O desconto do inss é R$ {inss:.2f}")
print(f"O desconto do irrf é R$ {irrf:.2f}")
print(f"O desconto do sindicato é R$ {sindicato:.2f}")
print(f"O salário a receber é R$ {liquido:.2f}")