import pessoa as pe
import CalcularFolha as cf

class atendente(pe.pessoa):
    def __init__(self):
        super().__init__()
        self.CalcularFolha= cf.CalcularFolha()
        self.matricul=''
        self.salario=''
        self.setor=''

    def cadastrar_atendente(self):
        super().cadastrar()
        self.matricul=input("matricula: ")
        self.salario=input("Salario: ")
        self.setor=input("Setor: ")

    def exibir_atendente(self):
        super().exibir()
        print(self.matricul)
        print(self.endereco.exibir_endereco())
        print(self.salario)
        print(self.setor)
        print(self.CalcularFolha.exibir_folha_pagamento(self.salario))