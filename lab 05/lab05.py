###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Dados da Sorte
# Nome: Wilson Santos Neto
# RA: 186542
###################################################
# Leitura da entrada de dados
dado_1 = int(input())
limite_inferior = int(input())
limite_superior = int(input())
# Processamento dos casos de ativação do bônus
a = 1
numero = 0
while(a<7):
    dado_2 = a
    b = 1
    while(b<7):
        dado_3 = b
        c = 1
        while(c<7):
            dado_4 = c
            soma = dado_1 + dado_2 + dado_3 + dado_4
            if (dado_1 != dado_2 and dado_1 != dado_3 and dado_1 != dado_4 and dado_2 != dado_3 and dado_2 != dado_4 and dado_3 != dado_4 and soma <= limite_superior and soma >= limite_inferior):
                numero = numero + 1
            c = c+1
        b= b+1
    a= a+1
# Saída de dados
print(numero, "de 216 combinações podem ativar o bônus")