numeros = []
pares = []
soma = 0
for i in range(1,6):
    num = int(input(f"Digite o {i}º número: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
for i in pares:
    soma += i
print(soma)