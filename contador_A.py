contador_a = 0
texto = str(input("Digite uma frase: "))
for letra in texto:
    if letra.lower() == "a":
        contador_a += 1
print(f"O texto contem {contador_a} letras a")