import endereco as edrc
class pessoa(edrc.endereco):
    def __init__(self):
        super().__init__()
        self.nomes=''
        self.telefone=''
        self.celular=''
        self.emails=''
        self.rg=''
        self.cpf=''
        self.endereco=edrc.endereco() #pessoa contem endereço# 
    def cadastrar(self):
        super().cadastrar_endereco()
        self.nomes=input("Nome: ")
        self.emails=input("Email: ")
        self.telefone=input("telefone: ")
        self.celular=input("Celular: ")
        self.rg=input("Rg: ")
        self.cpf=input("CPF: ")
    def exibir(self):
        super().exibir_endereco()
        print(self.nomes)
        print(self.emails)
        print(self.telefone)
        print(self.celular)
        print(self.rg)
        print(self.cpf)