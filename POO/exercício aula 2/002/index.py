from veiculo import Veiculo
from caminhao import Caminhao

lista = []
while True:
    continua = input("Deseja continuar? ").upper()
    if continua[0] == "N":
        break

    marca, modelo, ano = input("Digite a marca, modelo e ano: ").split()
    ecaminhao = input("É um caminhão? ").upper()
    if ecaminhao[0] == "S":
        carga = float(input("Capacidade de carga: "))
        veiculo = Caminhao(marca, modelo, ano, carga)
        veiculo.capacidade_carga(carga)

        verifica = float(input("Digite a carga: "))

        veiculo.verificar_carga(verifica)
        veiculo = Caminhao(marca, modelo, ano, carga)
    else: 
        veiculo = Veiculo(marca, modelo, ano)
    lista.append(veiculo)
    for c in range(len(lista)):
        lista[c].exibir_dados()