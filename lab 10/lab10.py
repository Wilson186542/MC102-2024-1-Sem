###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados à Obra
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

#Uma função True quando a posição indicada está livre
def Esta_Livre(posicao):
    if posicao == " ":
        return True
    else:
        return False

#Dá print no terreno após estar pronto
def printar (TerrenoPronto, M, N):
    Linha_Do_Terreno = ""
    for a in range(M):
        for b in range(N):
            Linha_Do_Terreno += TerrenoPronto[a][b]
        print(Linha_Do_Terreno)
        Linha_Do_Terreno = ""

def Colocar_Casa(terreno, Posicao_1, Posicao_2, tamanho):
    #COLOCAR OS * DA BORDA DA CASA
    #COLOCAR PRIMEIRA COLUNA
    for linhas in range (Posicao_1, Posicao_1+tamanho):
        terreno[linhas][Posicao_2] = "*"
    #COLOCAR SEGUNDA COLUNA
    for linhas in range (Posicao_1, Posicao_1+tamanho):
        terreno[linhas][Posicao_2+tamanho-1] = "*"
    #COLOCAR PRIMEIRA LINHA
    for colunas in range (Posicao_2, Posicao_2+tamanho):
        terreno[Posicao_1][colunas] = "*"
    #COLOCAR SEGUNDA LINHA
    for colunas in range (Posicao_2, Posicao_2+tamanho):
        terreno[Posicao_1+tamanho-1][colunas] = "*"
    return terreno

#APARENTEMENTE CERTA/COMPLETA AGORA
def Ver_Tamanho_Do_Quadrado (terreno, Posicao_1, Posicao_2, M,N):
    #Testar todos os tipos de quadrados
    De_Break = False
    Tamanho_Definido = 0
    for Tamanho_Do_Quadrado_Teste in range (1, min(M-Posicao_1+1, N-Posicao_2+1)):
        for linha in range (Posicao_1, Posicao_1+ Tamanho_Do_Quadrado_Teste):
            for coluna in range (Posicao_2, Posicao_2 + Tamanho_Do_Quadrado_Teste):
                if (Esta_Livre(terreno[linha][coluna]) != True):
                    Tamanho_Definido = Tamanho_Do_Quadrado_Teste - 1
                    De_Break = True 
                    break
            if De_Break:
                break
        if De_Break:
            break
    return Tamanho_Definido

#Acha a melhor para a casa quadrada, achando os mínimos agrupados da matriz calculada e guardando suas posições
def Achar_Melhor_Contorno (terreno, M,N):
    Melhor_Linha = Melhor_Coluna = 0
    Tamanho_Ate_Entao = 0
    #Rodar todas as possibilidades, vendo qual gera o maior quadrado
    for linha in range (1,M-1):
        for coluna in range (1,N-1):
            tamanho_tentativa = Ver_Tamanho_Do_Quadrado (terreno, linha, coluna, M,N)
            if (tamanho_tentativa > Tamanho_Ate_Entao):
                Tamanho_Ate_Entao = tamanho_tentativa
                Melhor_Linha = linha
                Melhor_Coluna = coluna
    return Melhor_Linha, Melhor_Coluna, Tamanho_Ate_Entao

def main():
    # Leitura do número de setores verticais e horizontais.
    M, N = map(int, input().split())
    terreno = []

    # Leitura do mapa do terreno do cliente.
    for i in range(M):
        linha_i = list(input())
        terreno += [linha_i]
    Posicao_1 , Posicao_2, Tamanho = Achar_Melhor_Contorno (terreno, M,N)
    terreno_Pronto = Colocar_Casa(terreno, Posicao_1, Posicao_2, Tamanho)
    printar(terreno_Pronto, M, N)


if __name__ == "__main__":
  main()