
class Carro(object):
    def __init__(self, caminho):
        self.caminho=caminho

    def andar(self):
        print('Andando pela', self.caminho)

class fusca(Carro):
    def __init__(self, caminho):
        self.caminho=caminho

class ferrari(Carro):
    def __init__(self, caminho):
        self.caminho = caminho
    
    def andar(self):
        print("Correndo pela", self.caminho)