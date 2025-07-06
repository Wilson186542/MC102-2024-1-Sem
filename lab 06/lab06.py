###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Espectativa de Vendas Mensais
# Nome: Wilson Santos Neto
# RA: 186542
###################################################
# Leitura da quantidade de meses e os valores de vendas mensais
N = int(input())
vendas = []
for i in range(N):
    vendas.append(float(input()))
# Verificação das expectativas de mensais de vendas
i = 0

for i in range(3, N+1):
    somaxivi = 0
    somaxi = 0
    somavi = 0
    somaxiquad = 0
#Soma(xi . vi)
    for a in range(i-1):
        somaxivi = somaxivi + (a+1) * vendas[a]
#Soma(xi)
    for b in range(i-1):
        somaxi = somaxi + (b+1)
#Soma(vi)
    for c in range(i-1):
        somavi = somavi + vendas[(c)]
#Soma(xi^2)
    for d in range(i-1):
        somaxiquad = somaxiquad + (d+1)**2
#Calculando os coeficientes
    coefAng = ((i-1)*somaxivi-somaxi*somavi) / ((i-1)*somaxiquad-(somaxi)**2)
    coefLin = (somavi-coefAng*somaxi) / (i-1)
#Estimando e printando:
    estimativa = round(coefAng*(i) + coefLin,1)
    if (estimativa == vendas[i-1]):
        print(vendas[i-1],estimativa,"ESPERADO")
    elif (estimativa > vendas[i-1]):
        print(vendas[i-1],estimativa,"INFERIOR")
    else:
        print(vendas[i-1],estimativa,"SUPERIOR")