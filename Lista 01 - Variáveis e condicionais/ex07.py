a = int(input("Digite um número ímpar: "))
n_anterior = a-2
n_impar_sucessor = a+2
diferenca = (n_impar_sucessor**2)-(n_anterior**2)
print(f"A diferença entre o quadrado do número sucessor e antecessor do informado é de: {diferenca}")
