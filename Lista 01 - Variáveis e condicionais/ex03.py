valor_total = float(input("Digite o valor total das mercadorias compradas: "))

if valor_total < 500:
  imposto = 0
else:
  excedente = valor_total - 500
  imposto = excedente*0.50

print(f"A taxa sobre o valor excedente é de: R${imposto}")