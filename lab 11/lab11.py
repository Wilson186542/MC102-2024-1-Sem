###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Níveis de Radiação
# Nome: Wilson Santos Neto
# RA: 186542
###################################################
def Propagar_Focos(potencia, x,y, matriz):
    for i in range(n):
        for j in range(m):
            # Calcular (distancia) de cada um
            distancia = int(potencia[0]) - max(abs(i-int(x[0])),abs(j-int(y[0])))
            if (distancia > 0 and distancia < int(potencia[0])):
                matriz [i][j] = int(matriz [i][j]) + distancia
    return matriz
# Leitura de dados
n = int(input())
#Criando a matriz base:
matriz = []
for i in range(n):
    entrada = input()
    linha = list(entrada)
    m = len(entrada)
    matriz.append(linha)
# Processamento
# Achar_Focos
Focos = []
for i in range(n):
    for j in range(m):
        if (matriz[i][j] != "0"):
            Focos.append([[matriz[i][j]],[i],[j]])
#Propagar_Focos
for i in range(len(Focos)):
    matriz = Propagar_Focos(Focos[i][0], Focos[i][1], Focos[i][2], matriz)
#Substituir maior que 9 por +
for i in range(n):
    for j in range(m):
        if (int(matriz[i][j]) > 9):
            matriz[i][j] = "+"
# Impressão da saída
Linha = ""
for i in range(n):
    for j in range(m):
        Linha += str(matriz[i][j])
    print(Linha)
    Linha = ""