letra = input("Digite uma letra: ")
if letra in "aeiouAEIOU":
    print(f"A letra {letra} é uma vogal.")
elif letra in "bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ":
    print(f"A letra {letra} é uma consoante")
else:
    print(f"A {letra} é outro caracter.")