###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Calculadora genômica
# Nome: Wilson Santos Neto 
# RA: 186542
###################################################

#Declarando funções

def reverter(i, j):
    if tipo == "c1":
        if i > j:
            partefinal = list(S[i:len(S)])
            parteinicial = list(S[0:j+1])
            junto = partefinal + parteinicial
            junto.reverse()
            revertido = junto
            letras = list(S)
            n = m = 0
            for a in range (i,len(S)):
                letras[a] = revertido [n]
                n = n + 1
            for b in range (0,j+1):
                letras[b] = revertido [m-j-1]
                m = m + 1
            return "".join(letras)
    else:
        if i > j:
            return S
    partenormal = S[i:j+1]
    partenormal = partenormal[::-1]
    return S[:i] + partenormal + S[j+1:]
    
def transpor(i,j,k):
    if tipo == "c0":
        min(i, len(S)-1)
        if (i == len(S) or j >= len(S)):
            return S
    else:
        if (i >= len(S) or j >= len(S) or k >= len(S)):
            i = i % len(S)
    letras = list(S)
    parte1 = letras[i:j+1]
    parte2 = letras[j+1:k+1]
    n = m = 0
    for a in range (i,j+1):
        letras[a] = parte2[n]
        n = n+1
    for b in range (j+1,k+1):
        letras[b] = parte1[m]
        m = m+1
    modificada = "".join(letras)
    return modificada

def inserir(g,i):
    if tipo == "c0":
        min(i, len(S))
    else:
        j = 1
    letras = list(S)
    letras.insert(i, g)
    modificada = "".join(letras)
    return modificada

def remover(i,j):
    if tipo == "c0":
        if (i >= (len(S)-1)):
            i = len(S)-2
            j = len(S)-1
        if (j >= len(S)):
            j = len(S)-1 
    else:
        if i >= len(S) or j >= len(S):
            j = min(j, len(S)-1)

    letras = list(S)
    for a in range (i,j+1):
        letras.pop(i)
    modificada = "".join(letras)
    return modificada

def fissao(i):
    letras = list(S)
    manejo = []
    for a in range(i, len(letras)):
        manejo.append(letras[a])
    for b in range(i):
        manejo.append(letras[b])
    modificada = "".join(manejo)
    return modificada

def mostrar():
    print (S,tipo)

def buscar(g,S):
    contador = 0
    a = posicao = removido = 0
    if (tipo == "c0"):
        while g in S:
            posicao = S.find(g)
            S = S[posicao + len(g):]
            removido = removido + (posicao + 1)
            contador = contador + 1
        print (contador)

    else:
        S = S + S
        while g in S:
            posicao = S.find(g)
            if a == -1:
                break
            S = S[posicao + 1:]
            removido = removido + (posicao + 1)
            contador = contador + 1
        contador = int(round((contador/2)+0.01,0))
        print (contador)

#Ler comandos

tipo = "c0"
S = str(input())
VerSeEhC1 = S.split()

if (len(VerSeEhC1) == 2):
        if (VerSeEhC1[1] == "c1" or "c0"):
            S = VerSeEhC1[0]
            tipo = VerSeEhC1[1]

while 1==1:
    EntradaLista = input().split()
    if (EntradaLista[0] == "sair"):
        break
    elif (EntradaLista[0] == "reverter"):
        S = reverter(int(EntradaLista[1]),int(EntradaLista[2]))
    elif (EntradaLista[0] == "transpor"):
        S = transpor(int(EntradaLista[1]),int(EntradaLista[2]),int(EntradaLista[3]))
    elif (EntradaLista[0] == "inserir"):
        S = inserir(str(EntradaLista[1]),int(EntradaLista[2]))
    elif (EntradaLista[0] == "remover"):
        S = remover(int(EntradaLista[1]),int(EntradaLista[2]))
    elif (EntradaLista[0] == "fissao"):
        tipo = "c0"        
        S = fissao(int(EntradaLista[1]))
    elif (EntradaLista[0] == "fusao"):
        tipo = "c1"
    elif (EntradaLista[0] == "mostrar"):
        mostrar()
    elif (EntradaLista[0] == "buscar"):
        buscar(str(EntradaLista[1]), S)
        