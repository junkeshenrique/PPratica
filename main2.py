salario = float(input("Informe o salário fixo recebido:"))
prazo = float(input("Informe o valor total de suas vendas a prazo:"))
avista = float(input("Informe o valor total de suas vendas a vista:"))
porcentoprazo = prazo/100
valorprazo = prazo + porcentoprazo
porcentoavista = avista/100
porcentoavist = porcentoavista * 2
valortotal = salario + porcentoprazo + porcentoavist
print(f"O valor recebido foi de: {valortotal:.2f} reais.")