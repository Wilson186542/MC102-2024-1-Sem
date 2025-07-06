###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Em Busca de um Chuveiro
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

# Leitura da entrada
R = int(input())
V = int(input())
T = int(input())
C = float(input())
L = int(input())

# Cálculo do consumo e impressão da saída
P = (V**2)/R
Consumo = P * T/1000
Custo = Consumo * C
print(Custo <= L)