km = float(input("Digite quantos quilômetros você rodou: "))
dias = int(input("Informe por quantos dias você pode rodou: "))

custo_diario = 90

if km > 100:
    km_amais = km-100
    custo_adicional = km_amais*12
else:
    custo_adicional = 0

total = (custo_diario*dias) + custo_adicional

print(f"O valor total a ser pago é de: R${total}")
