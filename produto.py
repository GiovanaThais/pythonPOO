class Produto:
    def __init__(self, nome,preco):
        self.nome= nome
        self.preco= preco
    def descont(self, percentual):
        self.preco= self.preco - (self.preco*(percentual/100))

p1= Produto('Camiseta',50)
p1.descont(10)
print(p1.preco)

p2= Produto('Caneca',15)
p2.descont(10)
print(p2.preco)
