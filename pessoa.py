class Pessoa():
    def __init__(self,nome,idade,comer=False,falar=False):
        self.nome=nome
        self.idade= idade
        self.comendo=comendo
        self.falar= falar

    def comer(self,alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo{alimento}')
        self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo")
            return
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando =True
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando')
            return
        print(f'{self.nome} está falando')
        self.falando= False
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


