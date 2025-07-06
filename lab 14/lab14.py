###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Montanha Russa II
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

# Recebe lista de preços, dia que se está checando, quantas ações se tem na mão, qual empresa e lista
def simula_compra_acoes(precos, dia, dinheiro, acoes_compradas, empresa_comprada, lista_de_transacoes_ideais):

# Caso base: No último dia, retorna o que obteve, como está
    if dia == len(precos):
        return lista_de_transacoes_ideais, dinheiro

# O que se tem na vez
    melhor_transacao = lista_de_transacoes_ideais[:]
    dinheiro_atual = dinheiro

# Só vender se tiver comprado
    if acoes_compradas > 0:
        valor_venda = precos[dia][empresa_comprada] * acoes_compradas
# Copia a lista de transações e adiciona a transação de venda
        lista_de_transacoes_ideais_venda = lista_de_transacoes_ideais[:]
        lista_de_transacoes_ideais_venda.append(("venda", empresa_comprada, dia, precos[dia][empresa_comprada]))
# Chama para o próximo dia com o dinheiro atualizado, tudo vendido
        transacoes_venda, dinheiro_venda = simula_compra_acoes(precos, dia + 1, dinheiro + valor_venda, 0, 0, lista_de_transacoes_ideais_venda)
        
# Atualiza o melhor caso (se for melhor)
        if dinheiro_venda > dinheiro_atual:
            dinheiro_atual = dinheiro_venda
            melhor_transacao = transacoes_venda[:]

# Comprar, se não ter nada
    if acoes_compradas == 0:
# Testa com todas as empresas
        for empresa in range(len(precos[dia])):
# Só compra se amanhã não está mais barato
            if dia < len(precos) - 1 and precos[dia][empresa] < precos[dia + 1][empresa]:
# Quanto pode comprar
                quantidade_acoes = dinheiro // precos[dia][empresa]
                if quantidade_acoes > 0:
# Copia a lista de transações e adiciona a transação de compra
                    lista_de_transacoes_ideais_compra = lista_de_transacoes_ideais[:]
                    lista_de_transacoes_ideais_compra.append(("compra", empresa, dia, precos[dia][empresa]))
# Chama para o próximo dia com o dinheiro atualizado, tudo comprado
                    transacoes_compra, dinheiro_compra = simula_compra_acoes(precos, dia + 1, dinheiro - quantidade_acoes * precos[dia][empresa], quantidade_acoes, empresa, lista_de_transacoes_ideais_compra)
                  
# Atualiza o melhor caso (se for melhor)
                    if dinheiro_compra > dinheiro_atual:
                        dinheiro_atual = dinheiro_compra
                        melhor_transacao = transacoes_compra[:]

# Se não dá para vender, e nem comprar, passar o dia
    transacoes_nada, dinheiro_nada = simula_compra_acoes(precos, dia + 1, dinheiro, acoes_compradas, empresa_comprada, lista_de_transacoes_ideais)
    if dinheiro_nada > dinheiro_atual:
        dinheiro_atual = dinheiro_nada
        melhor_transacao = transacoes_nada[:]
    
# Chegando ao final, retorna        
    return melhor_transacao, dinheiro_atual

# Leitura de dados
num_dias, num_empresas = map(int, input().split())
precos = []
for i in range(num_dias):
    precos.append(list(map(int, input().split())))
dinheiro_inicial = int(input())
dia = 0
acoes_compradas = 0
empresa_comprada = 0
lista_de_transacoes_ideais = []

# Chamada da função que vai achar a melhor combinação
lista_de_transacoes_ideais, total_final = simula_compra_acoes(precos, dia, dinheiro_inicial, acoes_compradas, empresa_comprada, lista_de_transacoes_ideais)

# Impressão da saída
for transacao in lista_de_transacoes_ideais:
    tipo, empresa, dia, preco = transacao
    if (tipo == "compra"):
        print(f"Acoes da empresa {empresa + 1} compradas no dia {dia + 1} por R$ {preco}")
    else:
        print(f"Acoes da empresa {empresa + 1} vendidas no dia {dia + 1} por R$ {preco}")

# Imprime o dinheiro final obtido após todas as transações
print(f"Dinheiro final: R$ {total_final}")