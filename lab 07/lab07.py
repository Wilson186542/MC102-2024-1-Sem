###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Montanha Russa
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

# Leitura de dados
N = int(input())
preco = []
for i in range(N):
    preco.append(float(input()))
Q = float(input())
# Cálculo dos dias de compra e venda
dc1 = dv1 = dc2 = dv2 = maiorAteAgora = montante1 = montante2 = quantiaCompra1 = quantiaCompra2 = saldo = compra1 = compra2 = venda1 = 0
#Se confere todas as possibilidades, comparando qual gera mais lucro
#Se inicia com dc1 o dia 1, e vai em cada loop externo aumentando até N-3
for a in range(0, N-3):
#Se inicia com dv1 o dia 2, e vai em cada loop externo aumentando até N-2
    for b in range (a+1, N-2):
#Se inicia com dc2 o dia 3, e vai em cada loop externo aumentando até N-1
        for c in range (b+1, N-1):
#Se inicia com dv2 o dia 4, e vai em cada loop externo aumentando até N
            for d in range (c+1, N-0):
                quantiaCompra1 = Q // preco[a]
                saldo = Q - quantiaCompra1 * preco[a]
                montante1 = quantiaCompra1 * preco[b]
                saldo = saldo + montante1
                quantiaCompra2 = saldo // preco[c]
                saldo = saldo - quantiaCompra2 * preco[c]
                montante2 = quantiaCompra2 * preco[d]
                saldo = saldo + montante2
                if (saldo > maiorAteAgora):
                    maiorAteAgora = saldo
                    dc1 = a+1
                    compra1 = preco[a]
                    dv1 = b+1
                    venda1 = preco[b]
                    dc2 = c+1
                    compra2 = preco[c]
                    dv2 = d+1
                    venda2 = preco[d]
# Impressão da saída
print("Dia da primeira compra:", dc1)
print("Valor de compra: R$ {:.2f}".format(compra1).replace(".", ","))
print("Dia da primeira venda:", dv1)
print("Valor de venda: R$ {:.2f}".format(venda1).replace(".", ","))
print("Dia da segunda compra:", dc2)
print("Valor de compra: R$ {:.2f}".format(compra2).replace(".", ","))
print("Dia da segunda venda:", dv2)
print("Valor de venda: R$ {:.2f}".format(venda2).replace(".", ","))
print("Valor final: R$ {:.2f}".format(maiorAteAgora).replace(".", ","))