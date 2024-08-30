"""No Python, a criação de classes é uma parte essencial da programação orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:

class Musica:
    nome = ""
    artista = ""
    duracao = int 
"""

Class Musica:
    def __init__(self, nome="", artista="", duracao = 0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome = "Hollywood bleeding", artista = "Post Malone", duracao= 180)
musica2 = Musica(nome= "Yebba's heartbreak", artista = "Drake, Yebba", duracao= 230)
musica3 = Musica(nome = "You", artista = "Don toliver, Travis Scott", duracao = 300)

"""
utilizamos o método especial __init__ para inicializar os atributos da classe. A sintaxe do Python permite definir os atributos diretamente no construtor, tornando o código mais claro e legível.
"""

