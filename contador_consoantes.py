contador = 0
texto = str(input("Digite uma frase: "))
for letra in texto:
    if letra.lower() in "bcdfghjklmnpqrstvxz":
        contador += 1
print(f"A frase contem {contador} consoantes.")