import pessoa as pe
import funcionario as fu
class medico(fu.pessoa):
    def __init__(self):
        super().__init__()
        self.matricula=''
        self.crm=''
        self.especialidade=''
        self.plus_salario=''
    def cadastrar_medico(self):
        super().cadastrar()
        self.matricula=input("Matricula: ")
        self.crm=input("CRM: ")
        self.especialidade=input("Especialidade: ")
        self.plus_salario=float(input("Salario:"))
    def exibir_medico(self):
        super().exibir()
        print(self.matricula)
        print(self.cartSus)
        print(self.crm)
        