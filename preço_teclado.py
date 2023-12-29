qtd = int(input("Quantos teclados quer comprar? "))
if qtd < 12:
    preco = qtd * 30
    print(F"O total da sua compra é R$ {preco}")
else:
    preco = qtd * 25
    print(f"O total da sua compra é R$ {preco}")