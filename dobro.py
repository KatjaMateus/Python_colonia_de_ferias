numeros = []
for i in range(5):
    num = int(input(f"Digite o {i}º número: "))
    numeros.append(num)
for num in numeros:
    print(f"O dobro de {num} é {num*2}")