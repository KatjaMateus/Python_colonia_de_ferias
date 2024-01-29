class Livro:
    def __init__(self, nome, autor, paginas, genero) -> None:
        self.nome = nome
        self.autor = autor
        self.paginas = paginas
        self.genero = genero

    def ver_informacoes(self):
        return f"""
        Informações:
        Nome do livro: {self.nome}
        Autor: {self.autor}
        Número de páginas: {self.paginas}
        Gênero: {self.genero}
"""
biblioteca = []

def adicionar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    paginas = int(input("Digite o número de páginas: "))
    genero = input("Digite o gênero do livro: ")
    novo_livro = Livro(nome,autor,paginas,genero)
    biblioteca.append(novo_livro)
    print(f"O livro {nome} foi adicionado a biblioteca.")

def ver_todos_os_livros():
    if not biblioteca:
        print("A biblioteca está vazia!")
        return
    print(f"Todos os livros na biblioteca:")
    for livro in biblioteca:
        print(livro.ver_informacoes())

def editar_livro():
    ver_todos_os_livros()
    if not biblioteca:
        return
    try:
        indice = int(input("Digite o número do livro que quer editar: "))
        livro_para_editar = biblioteca[indice]

        escolha = int(input("""Escolha o campo que deseja editar:
                            1 - nome do livro
                            2 - autor
                            3 - paginas
                            4 - genero
                            """))
        if escolha == 1:
            novo_nome = input("Digite o novo nome do livro: ")
            livro_para_editar.nome = novo_nome
        elif escolha == 2:
            novo_autor = input("Digite o novo nome de autor: ")
            livro_para_editar.autor = novo_autor
        elif escolha == 3:
            nova_pagina = int(input("Digite o novo número de páginas: "))
            livro_para_editar.paginas = nova_pagina
        elif escolha == 4:
            novo_genero = input("Digite o novo genero: ")
            livro_para_editar.genero = novo_genero
        else:
            print("Opção inválida")
            return
        print(f"O livro {livro_para_editar.nome} foi editado com sucesso!")

    except IndexError:
        print("Indice inválido. Escolha um número válido.")

def excluir_livro():
    ver_todos_os_livros()
    if not biblioteca:
        return
    try:
        indice = int(input("Digite o número do livro que quer excluir: ")) - 1
        livro_excluir = biblioteca.pop(indice)
        print(f"Livro {livro_excluir.nome} excluído da biblioteca.")
    
    except IndexError:
        print("Indice inválido. Por favor, escolha um número válido.")




while True:
    menu = int(input("""Eslcolhe uma opção:
            1 - Adicionar livro
            2 - Ver todos os livros
            3 - Editar livro
            4 - Excluir livro
            0 - Sair
            """))
    
    if menu == 1:
        adicionar_livro()
    elif menu == 2:
        ver_todos_os_livros()
    elif menu == 3:
        editar_livro()
    elif menu == 4:
        excluir_livro()
    elif menu == 0:
        print("Programa encerrado")
        break
    else:
        print("Opção inválida")
        break
    
    input("Pressione Enter para continuar...")

        