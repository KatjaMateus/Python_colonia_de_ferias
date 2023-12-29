maior = float("-inf")
for i in range(1,11):
    num = int(input(f"Digite o {i}º número: "))
    if num > maior:
        maior = num
print(f"O maior número é {maior}")