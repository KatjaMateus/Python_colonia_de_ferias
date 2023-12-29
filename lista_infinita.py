palavras = []

while True:
    palavra = str(input("Digite uma palavra: "))
    palavras.append(palavra)
    if palavra.lower() == "sair":
        break

if palavras:
    maior_palavra = palavras[0]
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    print(f"A maior palavra na lista é {maior_palavra}")
else:
    print("Não foi digitada nenhuma palavra ainda.")

    
