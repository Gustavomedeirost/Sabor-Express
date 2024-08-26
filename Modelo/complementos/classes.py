"""Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Lembrando: A simplicidade do Python nos permite criar classes de maneira mais elegante e expressiva, facilitando a compreensão do código.

Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):"""

class Musica:
    nome = ''
    artista = ''
    duração = int

musica1 = Musica()
musica1.nome = "amanhacer"
musica1.artista = "BK"
musica1.duração = 230

musica2 = Musica()
musica2.nome = "Imagine"
musica2.artista = "John Lemnon"
musica2.duração = "339"

musica3 = Musica()
musica3.nome = "Shape of you"
musica3.artista = "Ed sheeran"
musica3.duração = 250