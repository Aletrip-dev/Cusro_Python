class Pessoa(object): #sempre informar a classes/informar objetct para a classe pai
                        #pass #informa que a classe está vazia - vale para função o método
    nome = None
    def salvar(self, x):
        self.nome = x
        print("Salvando", self.nome)
        
