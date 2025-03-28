anos = int(input("Informe a quantos anos você trabalha na empresa: "))
salario_inicial = float(input("Digite o seu sálario inicial:"))

for i in range(anos):
    novo_salario = salario_inicial*2
    salario_final = novo_salario

print(f"O seu salário atual é de: R${salario_final}")    