#Polimorfismo
from ex_polimorfismo_Veiculo import Veiculo

class Carro(Veiculo):
    limit = 50      #varíavel da classe
    
    def __init__(self, cor, marca, modelo, tanque, ano):
        super().__init__(cor, marca, modelo, tanque)
        self.ano = ano     #atributo - variável da instância
        
        
    def abastecer(self, litros):
        print('Tentando abastecer: ' + str(litros) + " litros")
        if self.tanque + litros > self.limit:
            print('Capacidade máxima alcançada, foi possível abastecer: ' +
                  str(self.limit -self.tanque) + ' litros.')
            self.tanque = self.limit
        else:
            self.tanque += litros
    

    