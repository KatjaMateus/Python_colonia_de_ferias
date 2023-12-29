numeros = []

for i in range(1,6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)
menor = numeros[0]
for num in numeros:
    if num < menor:
        menor = num
print(f"O menor número da lista é {menor}.")
