a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite um último número: "))

if (a > b) and (a > c):
    print(f"o número maior é {a}")
elif (b > a) and (b > c):
    print(f"o número maior é {b}")
elif (c > a) and (c > b):
    print(f"o número maior é {c}")

if (a < b) and (a < c):
    print(f"o número menor é {a}")
elif (b < a) and (b < c): 
    print(f"o número menor é {b}") 
else:
    print(f"o número menor é {c}")
