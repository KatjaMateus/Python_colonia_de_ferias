pares = 0
impares = 0
for i in range(1,11):
    numero = int(input(f"Digite o {i}º numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"A quantidade de números pares é {pares} e a quantidade de números impares é {impares}")
