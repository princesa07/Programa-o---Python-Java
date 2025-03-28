a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite um último número: "))

media = (a+b+c)/3
media_ponderada = ((a*2)+(b*2)+(c*3))/7
media_ponderada2 = ((a*1)+(b*2)+(c*2))/5

print(f"A média aritmética simples e as média ponderadas dos números informados respectivamente são: {media}, {media_ponderada}, {media_ponderada2}")