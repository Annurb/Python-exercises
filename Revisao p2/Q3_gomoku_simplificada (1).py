import random

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(str(celula) for celula in linha))

def preencher_manual(n):
    tabuleiro = []
    
    print("Digite os valores do tabuleiro (números 0, 1 ou 2):")
    for i in range(n):
        while True:
            linha_input = input(f"linha {i+1}: ").split()
            if len(linha_input) != n:
                print(f"Por favor, insira exatamente {n} números.")
                continue
            linha = [int(x) for x in linha_input]
            
            if all(c in [0,1,2] for c in linha):
                tabuleiro.append(linha)
                break
            else:
                print("Valores inválidos. Insira apenas números 0, 1 ou 2.")
                continue
    return tabuleiro

def preencher_aleatorio(n):
    tabuleiro = []
    for _ in range(n):
        linha = [random.randint(0,2) for _ in range(n)]
        tabuleiro.append(linha)
    return tabuleiro

def verificar_vencedor(tabuleiro,n):
    saida=0
    # Verifica linhas, colunas para cinco consecutivos do mesmo jogador
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] != 0:
                jogador = tabuleiro[i][j]
                # Verifica linha
                if j + 4 < n:
                    if all(tabuleiro[i][j + k] == jogador for k in range(5)):
                        jogador = jogador
                        saida +=1
                
    for i in range(n):
        for j in range(n):
            if tabuleiro[i][j] != 0:
                jogador = tabuleiro[i][j]
                # Verifica coluna
                if i + 4 < n:
                    if all(tabuleiro[i + k][j] == jogador for k in range(5)):
                        jogador = jogador
                        saida +=1
                        #break
                        
    if saida != 1:
        return 0 # Ainda não há vencedor ou empate
    else:
        return jogador
    


def main():
    tabuleiro = []
    n = int(input("Digite o tamanho do tabuleiro: "))
    while True:
        print("\nMenu de opções:")
        print("1) Preencher o tabuleiro manualmente")
        print("2) Preencher o tabuleiro aleatoriamente")
        print("3) Encerrar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tabuleiro = preencher_manual(n)
        elif opcao == '2':
            tabuleiro = preencher_aleatorio(n)
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        # Exibir o tabuleiro
        print("\nTabuleiro gerado:")
        imprimir_tabuleiro(tabuleiro)

        # Verificar vencedor
        vencedor = verificar_vencedor(tabuleiro,n)
        if vencedor == 1:
            print("O jogador com pedras pretas venceu.")
        elif vencedor == 2:
            print("O jogador com pedras brancas venceu.")
        else:
            print("Ainda não há vencedor.")


main()

