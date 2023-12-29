nome = input("Digite seu nome: ")
hora = float(input("Digite a hora (ex. 16.45): "))
if hora > 12 and hora < 18:
    print(f"Boa tarde, {nome}!")
elif hora >= 18 and hora <= 24:
    print(f"Boa noite, {nome}!")
else:
    print(f"Bom dia, {nome}!")