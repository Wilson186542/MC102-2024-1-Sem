###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Anonimizador de Texto
# Nome: Wilson Santos Neto
# RA: 186542
###################################################

ListaDeDados = []

def RetirarEspaco(palavra):
    return palavra.replace(" ", "")

#Função VerSeTemPontuaçãoNoFinal
def TemPontuaçãoNoFinal(palavra):
    if palavra[-1] == '.' or palavra[-1] == ',':
        return True
    else:
        return False

#Retirar toda a pontuação
def RetirarTodaPontuação(palavra):
    pontuacao = [".", ",", ":", ";", "!", "?", "-", "/"]
    for cadaum in pontuacao:
        palavra = palavra.replace(cadaum, "")
    return palavra

def RetirarTudoMenosTraco(palavra):
    pontuacao = [".", ",", ":", ";", "!", "?", "/"]
    for cadaum in pontuacao:
        palavra = palavra.replace(cadaum, "")
    return palavra

#Função VerQualAPontuaçãoNoFinal
def VerQualAPontuaçãoNoFinal(palavra):
    return RetirarAPontuaçãoDoFinalSeTiver(palavra), palavra[len(palavra)-1]

#Função RetirarAPontuaçãoDoFinalSeTiver
def RetirarAPontuaçãoDoFinalSeTiver (palavra):
    if TemPontuaçãoNoFinal(palavra):
        return palavra[:-1]
    else:
        return palavra

#Função EquivalenteCPF
def EquivalenteCPF (palavra):
#A forma padrão será o CPF sem "." ou "-"
    return RetirarTodaPontuação(palavra)

#Função EquivalenteCartao
def EquivalenteCartao (palavra):
#Juntando Tudo   
    espaço = " "     
    for cadaum in espaço:
        palavra = palavra.replace(cadaum, "")
    return palavra

#Função EhMaiuscula
def EhMaiuscula (palavra):
    palavra = RetirarAPontuaçãoDoFinalSeTiver(palavra)
    if ((palavra[0].upper() + palavra[1:].lower()) == palavra and palavra.isalpha() and palavra != ""):
        return True
    else:
        return False
# Anonimização do texto
#Função anonimizar (tipo, dado)
def anonimizar (tipo,dado):
    dado = RetirarAPontuaçãoDoFinalSeTiver(dado)
    #Passar para forma equivalente:
    if tipo == "cpf":
        dado = EquivalenteCPF(dado)

    if tipo == "cartao":
        dado = EquivalenteCartao(dado)

    if tipo == "nome":
        dado = RetirarEspaco(dado)

    #Conferir se já não está presente na lista
    if ((dado in ListaDeDados) == False):
    #Se não estiver, colocar
        ListaDeDados.append(dado)
        return (tipo + ":" + str(len(ListaDeDados)))
    #Se já estiver
    else:
    #Checar qual posição está:
        posicao = ListaDeDados.index(dado)
        return (tipo + ":" + str(posicao+1))
    
#Receber entrada, com loop "eterno"
while (1==1):
    n = 0
    #Dividir cada palavra da entrada em list
    # Leitura do texto
    texto = input().split()
    #Quebrar o loop quando se ter como entrada o "-"
    if (texto[0] == "-"):
        break
    while n < len(texto):
        #Identificar Nome
        #Fazer um loop olhando palavra por palavra, menos uma por precisar de ao menos 2 de tamanho
        if (n < len(texto) - 2):
            #Olhar se começa em maiuscula e sem pontuação
            if (EhMaiuscula(texto[n]) and texto[n] == RetirarTodaPontuação(texto[n])):
            #Olhar se a próxima começa em maiuscula, ver se tem pontuação no final:
                if (EhMaiuscula(texto[n+1])):
                    if (TemPontuaçãoNoFinal(texto[n+1])):
                    #Se tem pontuação no final, acabar o nome por aqui
                        pontuacao = texto[n+1][-1]
                        #Juntar todo o nome
                        TodoNome = texto[n] + " " + texto[n+1]
                        #Retirar do texto o nome (apenas dessa parte) todo e substituir pelo anomizado
                        texto.pop(n+1)
                        texto[n] = anonimizar("nome", TodoNome) + pontuacao
                    else:
                    #Se não tem pontuação, continuar olhando as próximas
                        #Juntar todas as seguidas que começam em maiscula
                        b=n+2
                        if (b < len(texto)):
                            pontuacao = ""
                            while (EhMaiuscula(texto[b]) and (TemPontuaçãoNoFinal(texto[b]) != 1)):
                                b = b + 1
                                QuebrouPorProximaTerPontuacao = TemPontuaçãoNoFinal(texto[b+1])
                            nome = 0
                            # Juntar palavras maiusculas a seguir
    
                            PartesDosNomes = []
    
                            if TemPontuaçãoNoFinal(texto[b]):
                                pontuacao = texto[b][-1]
                                for c in range (n, b+1):
                                    PartesDosNomes.append(texto[c])
                                for c in range (n, b):
                                    texto.pop(n+1)
                            else:
                                for c in range (n, b):
                                    PartesDosNomes.append(texto[c])
                                for c in range (n, b-1):
                                    texto.pop(n+1)
                            TodoNome = "".join(PartesDosNomes)
    
                            TodoNome = "".join(PartesDosNomes)
                            
                            #Anonimizar
                            texto[n] = anonimizar("nome", TodoNome) + pontuacao

    #Identificar CPF
        pontuacao = ""
        if TemPontuaçãoNoFinal(texto[n]):
            pontuacao = texto[n][-1]
        #Olhar se após retirada a pontuação tem 11 caracteres e são todos numéricos
        if (len(RetirarTodaPontuação(texto[n])) == 11 and RetirarTodaPontuação(texto[n]).isnumeric()):
            texto[n] = anonimizar("cpf", texto[n]) + pontuacao

    #Identificar Cartão com 16
        pontuacao = ""
        if TemPontuaçãoNoFinal(texto[n]):
            pontuacao = texto[n][-1]
        #Olhar se tem 16 caracteres todos numericos
        if (len(RetirarTodaPontuação(texto[n])) == 16 and RetirarTodaPontuação(texto[n]).isnumeric()):
            texto[n] = anonimizar("cartao", texto[n]) + pontuacao

    #Identificar Cartão 4 de 4 
        if (n < len(texto) - 3):
            pontuacao = ""
            if TemPontuaçãoNoFinal(texto[n+3]):
                pontuacao = texto[n+3][-1]
            #Olhar se essa e as proximas 3 tem 4 de tamanho e sua concatenação é toda numerica
            if (len(texto[n]) == 4 and len(texto[n+1]) == 4 and len(texto[n+2]) == 4 and len(texto[n+3]) == 4):
                if (texto[n].isnumeric() and texto[n+1].isnumeric() and texto[n+2].isnumeric() and texto[n+3].isnumeric()):
                    CartaoTudoJunto = texto[n] + texto[n+1] + texto[n+2] + texto[n+3]
                    texto[n] = anonimizar("cartao", CartaoTudoJunto) + pontuacao
            #Retirar resto do cartão
                    texto.pop(n+1)
                    texto.pop(n+1)
                    texto.pop(n+1)

    #Identificar Data
        pontuacao = ""
        if TemPontuaçãoNoFinal(texto[n]):
            pontuacao = texto[n][-1]
        #Olhar se ao se tirar toda a pontuação se tem 8 de tamanho e tudo numérico
        if (len(RetirarTudoMenosTraco(texto[n])) == 8 and RetirarTudoMenosTraco(texto[n]).isnumeric()):
            texto[n] = anonimizar("data", texto[n]) + pontuacao

    #Identificar Email
        pontuacao = ""
        if TemPontuaçãoNoFinal(texto[n]):
            pontuacao = texto[n][-1]
        #Olhar se tem apenas um @
        if (texto[n].find('@') != -1):
            if (texto[n].count("@") == 1):
                texto[n] = anonimizar("email", texto[n]) + pontuacao
        
        n = n + 1
        
    #Juntar todo o texto novamente numa string só 
    TodoTexto = " ".join(texto)
    #Printar o resultado final
    # Impressão da saída
    print (TodoTexto)