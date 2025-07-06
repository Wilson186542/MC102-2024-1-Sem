###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Pedra, Papel e Tesoura 2.0
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

# Leitura dos valores de força de cada jogador
bonus_jogador_1 = int(input())
bonus_jogador_2 = int(input())
vitorias_jogador_1 = 0
vitorias_jogador_2 = 0
empate = 0

# Processamento dos dados
while (1==1):
    entrada = input().split()
    if entrada[0] == '0':
        break
    else:
        jogada_jogador_1, forca_jogador_1, jogada_jogador_2, forca_jogador_2, fator_rodada = entrada
        forca_jogador_1 = int(forca_jogador_1)
        forca_jogador_2 = int(forca_jogador_2)
        fator_rodada = int(fator_rodada)

#Conferindo se ninguem acabou com seus bonus ou tenta gastar mais
    if (bonus_jogador_1 >= (forca_jogador_1 -1)):
        bonus_jogador_1 = bonus_jogador_1 - forca_jogador_1 + 1
    else:
        forca_jogador_1 = 1 + bonus_jogador_1
        bonus_jogador_1 = 0

    if (bonus_jogador_2 >= (forca_jogador_2 -1)):
        bonus_jogador_2 = bonus_jogador_2 - forca_jogador_2 + 1
    else:
        forca_jogador_2 = 1 + bonus_jogador_2
        bonus_jogador_2 = 0

#Mecanismo de determinação:

    #Mesmo simbolo:
    if (jogada_jogador_1==jogada_jogador_2):
        #Empate
        if (forca_jogador_1 == forca_jogador_2):
            empate = empate + 1
        elif (forca_jogador_1 > forca_jogador_2):
            vitorias_jogador_1 = vitorias_jogador_1 + 1
        else:
            vitorias_jogador_2 = vitorias_jogador_2 + 1
             
    #Simbolos diferentes:
    else:
        #Se o primeiro jogar pedra
        if (jogada_jogador_1=="Pedra"):
            #Se o segundo jogar papel / Primeiro na Desvantagem
            if (jogada_jogador_2=="Papel"):
                #Mesma força
                if ((fator_rodada * forca_jogador_1) == forca_jogador_2):
                    vitorias_jogador_2 = vitorias_jogador_2 + 1
                #Se o primeiro jogador usar mais força
                else: 
                    if ((fator_rodada * forca_jogador_1) > forca_jogador_2):
                        vitorias_jogador_1 = vitorias_jogador_1 + 1
                    #Se o primeiro usar menos força
                    else:
                        vitorias_jogador_2 = vitorias_jogador_2 + 1

            #Se o segundo jogar tesoura / Primeiro na Vantagem
            else:
                #Mesma força
                if ((fator_rodada * forca_jogador_2) == forca_jogador_1):
                    vitorias_jogador_1 = vitorias_jogador_1 + 1
                #Se o primeiro jogador usar mais força
                else:
                    if ((fator_rodada * forca_jogador_2) < forca_jogador_1):
                        vitorias_jogador_1 = vitorias_jogador_1 + 1
                    #Se o primeiro usar menos força
                    else:
                        vitorias_jogador_2 = vitorias_jogador_2 + 1


        #Se o primeiro jogar papel
        elif (jogada_jogador_1=="Papel"):
            #Se o segundo jogar pedra / Primeiro na Vantagem
            if (jogada_jogador_2=="Pedra"):
                #Mesma força
                if ((fator_rodada * forca_jogador_2) == forca_jogador_1):
                    vitorias_jogador_1 = vitorias_jogador_1 + 1
                #Se o primeiro jogador usar mais força
                else:
                    if ((fator_rodada * forca_jogador_2) < forca_jogador_1):
                        vitorias_jogador_1 = vitorias_jogador_1 + 1
                    #Se o primeiro usar menos força
                    else:
                        vitorias_jogador_2 = vitorias_jogador_2 + 1

            #Se o segundo jogar tesoura / Primeiro na Desvantagem
            else:
                #Mesma força
                if ((fator_rodada * forca_jogador_1) == forca_jogador_2):
                    vitorias_jogador_2 = vitorias_jogador_2 + 1
                #Se o primeiro jogador usar mais força
                else: 
                    if ((fator_rodada * forca_jogador_1) > forca_jogador_2):
                        vitorias_jogador_1 = vitorias_jogador_1 + 1
                    #Se o primeiro usar menos força
                    else:
                        vitorias_jogador_2 = vitorias_jogador_2 + 1
        

        #Se o primeiro jogar tesoura
        else:
            #Se o segundo jogar pedra / Primeiro na Desvantagem
            if (jogada_jogador_2=="Pedra"):
                #Mesma força
                if ((fator_rodada * forca_jogador_1) == forca_jogador_2):
                    vitorias_jogador_2 = vitorias_jogador_2 + 1
                #Se o primeiro jogador usar mais força
                else: 
                    if ((fator_rodada * forca_jogador_1) > forca_jogador_2):
                        vitorias_jogador_1 = vitorias_jogador_1 + 1
                    #Se o primeiro usar menos força
                    else:
                        vitorias_jogador_2 = vitorias_jogador_2 + 1
            
            #Se o segundo jogar papel / Primeiro na Vantagem
            else:
                #Mesma força
                if ((fator_rodada * forca_jogador_2) == forca_jogador_1):
                    vitorias_jogador_1 = vitorias_jogador_1 + 1
                #Se o primeiro jogador usar mais força
                else:
                    if ((fator_rodada * forca_jogador_2) < forca_jogador_1):
                        vitorias_jogador_1 = vitorias_jogador_1 + 1
                    #Se o primeiro usar menos força
                    else:
                        vitorias_jogador_2 = vitorias_jogador_2 + 1

# Saída de dados
print('Vitórias do jogador 1:', vitorias_jogador_1)
print('Vitórias do jogador 2:', vitorias_jogador_2)
print('Empates:', empate)