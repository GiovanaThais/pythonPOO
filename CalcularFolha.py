import atendente as atend

class FolhaPagamento():
    def __init__(self):
        super().__init__()
        self.salario=0.0
        self.inss=0.0
        self.irrf=0.0
        self.salarioL=0.0

    def cadastrar_salario(self,salario_bruto=0.0):
        self.salario = salario_bruto 

    def calcular_inss(self):
        inss = 0
        if self.salario < 1751.82:
            inss = self.salario * 0.08
        elif self.salario > 1751.81 and self.salario < 2919.73:
            inss = self.salario * 0.09
        elif self.salario > 2919.72 and self.salario < 5839.46:
            inss = self.salario * 0.11
        elif self.salario > 5839.45:
            inss = 817.66
        return inss

    def calcular_irrf(self, salariosinss):
        irrf = 0
        if salariosinss > 1903.98 and salariosinss < 2826.66:
            irrf = salariosinss * 0.075 - 142.80
        elif salariosinss > 2826.65 and salariosinss < 3751.06:
            irrf = salariosinss * 0.15 - 354.8
        elif salariosinss > 3751.05 and salariosinss < 4664.69:
            irrf = salariosinss * 0.225 - 636.13
        elif salariosinss > 4664.68:
            irrf = salariosinss * 0.275 - 869.36
        return irrf

    def exibir_folha_pagamento(self, salario_bruto):
        inss = self.calcular_inss(salario_bruto)
        irrf = self.calcular_irrf(salario_bruto - inss)
        salariol = salario_bruto - (inss + irrf)
        print("----------------------------------------")
        print("Salario Bruto: R$", salario_bruto)
        print("----------------------------------------")
        print("Descontos:")
        print("INSS: R$ ", self.inss)
        print("IRRF: R$ ", self.irrf)
        print("----------------------------------------")
        print("Salario liquido: R$", salariol)
        print("----------------------------------------")