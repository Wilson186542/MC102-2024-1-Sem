###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Pac-Man I
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

def Direita(orientacao):
    if (orientacao == "direita"):
        return "baixo"
    if (orientacao == "esquerda"):
        return "cima"
    if (orientacao == "cima"):
        return "direita"
    if (orientacao == "baixo"):
        return "esquerda"

def Esquerda(orientacao):
    if (orientacao == "direita"):
        return "cima"
    if (orientacao == "esquerda"):
        return "baixo"
    if (orientacao == "cima"):
        return "esquerda"
    if (orientacao == "baixo"):
        return "direita"

def Direcao_Contraria(orientacao):
    if (orientacao == "direita"):
        return "esquerda"
    if (orientacao == "esquerda"):
        return "direita"
    if (orientacao == "cima"):
        return "baixo"
    if (orientacao == "baixo"):
        return "cima"

def Eh_Parede(x,y): 
    if (mapa[y][x] == "X"):
        return True
    return False

def Morreu_num_Fantasma (x_pacman, y_pacman, tempo_poder):
    if (mapa[y_pacman][x_pacman] == "X" and tempo_poder <= 0):
        return True
    return False

def Seta_Contraria (seta):
    if (seta == "→" and mapa[y_pacman][largura-1] != "#" and x_pacman <= 0):
        return "←←"
    elif (seta == "→"):
        return "←"
    elif (seta == "←" and mapa[y_pacman][0] != "#" and x_pacman >= largura):
        return "→→"
    elif (seta == "←"):
        return "→"
    elif (seta == "↓" and mapa[N-1][x_pacman] != "#" and y_pacman >= largura - 1):
        return "↑↑"
    elif (seta == "↓"):
        return "↑"
    elif (seta == "↑" and mapa[0][x_pacman] != "#" and y_pacman >= N - 1):
        return "↓↓"
    elif (seta == "↑"):
        return "↓"

def Não_Tem_Parede_Direita(x_pacman, y_pacman, largura, N, orientacao):
    if (orientacao == "cima"):
        if (x_pacman < largura):
            if (mapa[y_pacman][x_pacman + 1] != "#"):
                return True, "→"
            else:
                return False, "→"
        else:
            if (mapa[y_pacman][0] != "#"):
                return True, "→→"
            else:
                return False, "→"
    if (orientacao == "direita"):
        if (y_pacman < N - 1):
            if (mapa[y_pacman + 1][x_pacman] != "#"):
                return True, "↓"
            else:
                return False, "↓"
        else:
            if (mapa[0][x_pacman] != "#"):
                return True, "↓↓"
            else:
                return False, "↓"
    if (orientacao == "baixo"):
        if (x_pacman != 0):
            if (mapa[y_pacman][x_pacman - 1] != "#"):
                return True, "←"
            else:
                return False, "←"
        else:
            if (mapa[y_pacman][largura-1] != "#"):
                return True, "←←"
            else:
                return False, "←"
    if (orientacao == "esquerda"):
        if (y_pacman < largura - 1):
            if (mapa[y_pacman - 1][x_pacman] != "#"):
                return True, "↑"
            else:
                return False, "↑"
        else:
            if (mapa[N-1][x_pacman] != "#"):
                return True, "↑↑"
            else:
                return False, "↑"

def Não_Tem_Parede_Frente(x_pacman, y_pacman, largura, N, orientacao):
    return Não_Tem_Parede_Direita(x_pacman, y_pacman, largura, N, Esquerda(orientacao))

def Não_Tem_Parede_Esquerda(x_pacman, y_pacman, largura, N, orientacao):
    return Não_Tem_Parede_Direita(x_pacman, y_pacman, largura, N, Esquerda(Esquerda(orientacao)))

def Mover(x_pacman, y_pacman, orientacao, seta):
    if seta == "→":
        x_pacman = x_pacman + 1
    elif seta == "→→":
        x_pacman = 0
    elif seta == "↓":
        y_pacman = y_pacman + 1
    elif seta == "↓↓":
        y_pacman = 0
    elif seta == "←":
        x_pacman = x_pacman - 1
    elif seta == "←←":
        x_pacman = largura - 1
    elif seta == "↑":
        y_pacman = y_pacman - 1
    elif seta == "↑↑":
        y_pacman = N - 1    
    return x_pacman, y_pacman

# Leitura da entrada
N = int(input())
T = int(input())
#Criação do Mapa
mapa = []
for _ in range(N):
    mapa.append(list(input()))
# Simulação do jogo
for i in range(N):
    for largura in range(len(mapa[0])):
        if mapa[i][largura] == "C":
            x_pacman_inicial = largura
            y_pacman_inicial = i
x_pacman = x_pacman_inicial
y_pacman = y_pacman_inicial
coletado = 0
tempo_poder = 0
orientacao = "direita"

while 1 == 1:

    Não_Tem_Direita, seta_d = Não_Tem_Parede_Direita(x_pacman, y_pacman, largura, N, orientacao)
    Não_Tem_Frente, seta_f = Não_Tem_Parede_Frente(x_pacman, y_pacman, largura, N, orientacao)
    Não_Tem_Esquerda, seta_e = Não_Tem_Parede_Esquerda(x_pacman, y_pacman, largura, N, orientacao)

#Se não existir uma parede a sua direita, ele vira para a sua direita, e avança uma posição.
    if Não_Tem_Direita:
        x_pacman, y_pacman = Mover(x_pacman, y_pacman, orientacao, seta_d)
        orientacao = Direita(orientacao)
#Se não existir uma parede a sua frente, ele segue em frente. TUDO CERTO
    elif Não_Tem_Frente:
        x_pacman, y_pacman = Mover(x_pacman, y_pacman, orientacao, seta_f)
#Se não existir uma parede a sua esquerda, ele vira para a sua esquerda, e avança uma posição.
    elif Não_Tem_Esquerda:
        x_pacman, y_pacman = Mover(x_pacman, y_pacman, orientacao, seta_e)
        orientacao = Direita(Direita(Direita(orientacao)))
#Ele volta para a direção de onde ele veio, se as outras três direções tem paredes.    
    else:
        orientacao = Direcao_Contraria(orientacao)
        x_pacman, y_pacman = Mover(x_pacman, y_pacman, orientacao, Seta_Contraria(seta_f))

#Pegar poder
    if (mapa[y_pacman][x_pacman] == "*"):
        tempo_poder = tempo_poder + T + 1
        mapa[y_pacman][x_pacman] = " "
        coletado = coletado + 1
#Coletar pastilha TUDO CERTO
    if (mapa[y_pacman][x_pacman] == "."):
        mapa[y_pacman][x_pacman] = " "
        coletado = coletado + 1
#Checar se morreu num fantasma
    if Morreu_num_Fantasma (x_pacman, y_pacman, tempo_poder):
        #print ("Morreu de fantasma na posição x:", x_pacman, "y:", y_pacman)
        break
#Se não morreu:
    if (mapa[y_pacman][x_pacman] == "X"):
        mapa[y_pacman][x_pacman] = " "
#Se voltou a posição e orientação inicial, acaba
    if (x_pacman == x_pacman_inicial and y_pacman == y_pacman_inicial and orientacao == "direita"):
        #print ('Morreu de voltar')
        break
#Passar o tempo
    if (tempo_poder > 0):
        tempo_poder = tempo_poder - 1

# Impressão da saída
print (coletado)