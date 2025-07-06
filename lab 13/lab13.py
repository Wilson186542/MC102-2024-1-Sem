###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Transporte de Itens
# Nome: Wilson Santos Neto
# RA: 186542
###################################################
def ordem_decrescente (listagem):
    for i in range(n):
        indice_maximo = i
        for j in range(i+1,n):
            #Lembrando de que também troca se for igual, mas de indice menor
            if listagem[j][1] > listagem[indice_maximo][1] or (listagem[j][1] == listagem[indice_maximo][1] and listagem[j][0] < listagem[indice_maximo][0]):
                indice_maximo = j
        #Troca de ordem
        listagem[i], listagem[indice_maximo] = listagem[indice_maximo], listagem[i]
    ordem_indices = []
    for k in listagem:
        ordem_indices.append(k[0])
    return ordem_indices

# Leitura da capacidade e quantidade de itens
capacidade = int(input())
n = int(input())

# Leitura dos itens, pesos e valores
valor_por_peso, valor_por_valor, valor_por_razao = 0, 0, 0
carregado_por_peso, carregado_por_valor, carregado_por_razao = 0, 0, 0
produtos, peso, valor, razao = [], [], [], []

for i in range (n):
    entrada = input().split()
    produtos.append(entrada[0])
    peso.append(int(entrada[1]))
    valor.append(int(entrada[2]))
    razao.append(valor[i]/peso[i])

# Ordenação por peso
ordem_peso = ordem_decrescente(list(enumerate(peso)))
for i in range (n):
    if (carregado_por_peso + peso[ordem_peso[i]] <= capacidade):
        carregado_por_peso += peso[ordem_peso[i]]
        valor_por_peso += valor[ordem_peso[i]]

# Ordenação por valor
ordem_valor = ordem_decrescente(list(enumerate(valor)))
for i in range (n):
    if (carregado_por_valor + peso[ordem_valor[i]] <= capacidade):
        carregado_por_valor += peso[ordem_valor[i]]
        valor_por_valor += valor[ordem_valor[i]]

# Ordenação pela razão de valor por peso
ordem_razao = ordem_decrescente(list(enumerate(razao)))
for i in range (n):
    if (carregado_por_razao + peso[ordem_razao[i]] <= capacidade):
        carregado_por_razao += peso[ordem_razao[i]]
        valor_por_razao += valor[ordem_razao[i]]

# Impressão da resposta
print('Valor carregado considerando o peso dos itens: R$', valor_por_peso)
print('Peso carregado considerando o peso dos itens:', carregado_por_peso, 'Kg\n')
print('Valor carregado considerando o valor dos itens: R$', valor_por_valor)
print('Peso carregado considerando o valor dos itens:', carregado_por_valor, 'Kg\n')
print('Valor carregado considerando a razão de valor por peso: R$', valor_por_razao)
print('Peso carregado considerando a razão de valor por peso:', carregado_por_razao, 'Kg')