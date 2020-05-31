import pessoa as pe
class paciente(pe.pessoa):
    def __init__(self):
        self.data_nasc=''
        self.plano_saude=''
        self.cartaoSus=''
        super().__init__()

    def cadastrar_paciente(self):
        super().cadastrar()
        self.data_nasc= input("Data de nascimento: ")
        self.plano_saude=input("Plano de saúde: ")
        self.cartaoSus=input("Cartão SUS: ")


    def exibir_paciente(self):
        super().exibir()
        print(self.data_nasc)
        print(self.plano_saude)
        print(self.cartaoSus)



