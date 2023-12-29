numeros = []

for i in range(1,6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)
maior = numeros[0]
for num in numeros:
    if num > maior:
        maior = num
print(f"O maior número da lista é {maior}.")
