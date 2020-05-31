class endereco():
    def __init__(self):
        self.logradouro=''
        self.numero=''
        self.comp=''
        self.cep=''
        self.bairro=''
        self.cidade=''
        self.uf=''
    def cadastrar_endereco(self):
        self.logradouro=input("Endereço: ")
        self.numero=input("Numero: ")
        self.cep=input("CEP: ")
        self.comp=input("Complemento: ")
        self.bairro=input("Bairro: ")
        self.cidade=input("Cidade: ")
        self.uf=input("UF: ")
    def exibir_endereco(self):
        print(self.logradouro)
        print(self.numero)
        print(self.comp)
        print(self.cep)
        print(self.bairro)
        print(self.cidade)
        print(self.Uf)