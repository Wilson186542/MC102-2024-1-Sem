###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cupons de Desconto
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

# leitura de dados
X1 = int(input())
Z1 = int(input())
X2 = int(input())
Z2 = int(input())
X3 = int(input())
Z3 = int(input())
Valor = int(input())
# cálculo dos descontos

if Valor >= Z1:
    Desconto1 = X1
else:
    Desconto1 = 0

if (Valor*X2/100) >= Z2:
    Desconto2 = Z2
else:
    Desconto2 = Valor*X2/100

if Valor >= Z3:
    Desconto3 = Valor*X3/100
else:
    Desconto3 = 0

# Impressão da saída

if (Desconto1 == Desconto2 and Desconto2 == Desconto3):
    print("Maior desconto: Cupons 1, 2, 3")
    desconto = Desconto1
else:
    if (Desconto1 == Desconto2 and Desconto2 > Desconto3):
        print("Maior desconto: Cupons 1, 2")
        desconto = Desconto1
    else:
        if (Desconto1 == Desconto3 and Desconto3 > Desconto2):
            print("Maior desconto: Cupons 1, 3")
            desconto = Desconto1
        else:
            if (Desconto2 == Desconto3 and Desconto3 > Desconto1):
                print("Maior desconto: Cupons 2, 3")
                desconto = Desconto2
            else:
                if (Desconto1 > Desconto2 and Desconto1 > Desconto3):
                    print("Maior desconto: Cupom 1")
                    desconto = Desconto1
                else:
                    if (Desconto2 > Desconto1 and Desconto2 > Desconto3):
                        print("Maior desconto: Cupom 2")
                        desconto = Desconto2
                    else:
                        if (Desconto3 > Desconto1 and Desconto3 > Desconto1):
                            print("Maior desconto: Cupom 3")
                            desconto = Desconto3

print("Valor do desconto: R$ {:.2f}".format(desconto).replace(".", ","))