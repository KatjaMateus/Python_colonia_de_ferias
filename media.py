soma = 0
for nota in range(3):
    soma += float(input("Digite a nota: "))
media = soma / 3

if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")



