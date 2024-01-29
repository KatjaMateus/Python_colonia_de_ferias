class Locadora:
    def __init__(self, nome, genero, ano) -> None:
        self.nome = nome
        self.genero = genero
        self.ano = ano
    
    def alugar_dia(self, dia):
        return f"O filme {self.nome} foi alugado no dia {dia}."

class Jogo(Locadora):
    def __init__(self, nome, genero, ano, preco, modalidade) -> None:
        super().__init__(nome, genero, ano)
        self.preco = preco
        self.modalidade = modalidade
    
    def finalizar(self):
        return f"O jogo {self.nome} foi finalizado."
    
    def alugar_dia(self, dia, preco):
        return f"O jogo {self.nome} foi alugado no {dia} e custou {preco} reais."

class Filme(Locadora):
    def __init__(self, nome, genero, ano, duracao, elenco) -> None:
        super().__init__(nome, genero, ano)
        self.duracao = duracao
        self.elenco = elenco
    
    def en_cartaz(self):
        return f"O filme {self.nome} está em cartaz."
    
    def alugar_dia(self,dia):
        return f"O filme {self.nome} foi alugado no dia {dia} de graça."

meu_filme = Filme(nome="Grease", genero="musical", ano=1980, duracao="90 minutos", elenco="Olivia Newton-John, John Travolta")
dia_de_aluguel = "28/01/2024"
preco = "25 reais"

print(meu_filme.en_cartaz())
print(meu_filme.alugar_dia(dia=dia_de_aluguel))
    