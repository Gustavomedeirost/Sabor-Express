#1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

#2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao}"

Livro1 = Livro("Learn Python", "Alura", 2020)
Livro2 = Livro("Machine Learning", "Alura", 2024)

print(Livro1)
print(Livro2)

#3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def emprestar(self):
        self.disponivel = False

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

#4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livros.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

#5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

#6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

#7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico..

#8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

from biblioteca import Livro

livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)

print(livro_main1)
print(livro_main2)