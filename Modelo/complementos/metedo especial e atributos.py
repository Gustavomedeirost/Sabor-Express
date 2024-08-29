"""1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos."""

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro(modelo = "Cactus", cor = "Branco", ano = 2019)


"""
2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
"""

class Restaurante:
    def __init__(self, nome, categoria, preco, sobremesa,ativo)
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.sobremesa = sobremesa
        self.ativo =  ativo

    restaurantes = Restaurante(nome = "ifood", categoria = "Japonesa", preco = 20.9, sobremesa = "Tiramisu", ativo = True )

"""
3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
"""

class Restaurante:
    def __init__(self, nome, categoria, preco, sobremesa,ativo):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.sobremesa = sobremesa
        self.ativo =  ativo

    restaurantes = Restaurante(nome = "LaPlata", categoria = "Rupreste", ativo = False )

"""
4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
"""
class Restaurante:
    def __init__(self, nome, categoria, preco, sobremesa,ativo):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.sobremesa = sobremesa
        self.ativo =  ativo

    restaurantes = Restaurante(nome = "LaPlata", categoria = "Rupreste", ativo = False )

    def __str__(self):
        return f"{self.nome | self.categoria}"

"""
5. Crie uma classe chamada Cliente e pense em 3 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor
"""

class Cliente:
    def __init__(self, nome="", idade=0, cidade="", setor=""):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.setor = setor

cliente1 = Cliente(nome="Tuyo", idade=20, cidade="Belo Horizonte", setor="Industrial")
cliente2 = Cliente(nome="Roberto", idade=40, cidade="Porto Alegre", setor="Alimenticio")
cliente3 = Cliente(nome="Renzo", idade=30, cidade="Rio de Janeiro", setor="Influencer")

    