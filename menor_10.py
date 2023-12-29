menor = float("inf")
for i in range(1,11):
    num = int(input(f"Digite o {i}º número: "))
    if num < menor:
        menor = num
print(f"O menor número é {menor}")