
#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMANO = -1
COMP = +1

tabuleiro = [
    [0, 'V', 0, 'V', 0, 'V', 0, 'V',],
    [0,   0, 0,  0,  0,  0,  0,  0, ],
    [0,   0, 0,  0,  0,  0,  0,  0, ],
    [0,   0, 0,  0,  0,  0,  0,  0, ],
    [0,   0, 0,  0,  0,  0,  0,  0, ],
    [0,   0, 0,  0,  0,  0,  0,  0, ],
    [0,   0, 0,  0,  0,  0,  0,  0, ],
    [0,   0, 0,  0, 'L', 0,  0,  0, ],   
]
L_ovelha = [[0,1],[0,3],[0,5],[0,7]]
localizacao_lobo = [7,4]
jogada_inicial = 1


"""
Funcao para avaliacao heuristica do estado.
:parametro (estado): o estado atual do tabuleiro
:returna: +1 se o computador vence; -1 se o HUMANOo vence; 0 empate
 """
def avaliacao(estado):
   
    for i in range(len(estado[0])):
        if estado[0][i] == 'L': return -1 #COMP PERDEU
    if len(lista_de_possibilidadesMIN(estado)) == 0:
        return +1 # COMP GANHOU
    return 0 #estado não é terminal
""" ---------------------------------------------------------- """



"""
Limpa o console para SO Windows
"""
def limpa_console():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')
""" ---------------------------------------------------------- """

"""
Imprime o tabuleiro no console
:param. (estado): estado atual do tabuleiro
"""
def exibe_tabuleiro(estado):
    print('----------------')
    for row in estado:
        print('\n----------------------------------------')
        for cell in row:
            if cell == 'V':
                print('| V |', end='')
            elif cell == 'L':
                print('| L |', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------------------------------')
""" ---------------------------------------------------------- """


def HUMANO_vez():

    jogada_invalida = False
    primeira_jogada = True

    while jogada_invalida == False:
        limpa_console()
        if(primeira_jogada == False) :
            print("Movimento inválido, jogue de novo")
        else:
            primeira_jogada = False
        print('Vez do HUMANO: ')
        exibe_tabuleiro(tabuleiro)

        l = int(input('Escolha a linha [0-7]'))  # l= linha
        c = int(input('Escolha a coluna [0-7]')) # c = coluna
        mov_escolhido = [l,c]

        array = lista_de_possibilidadesMIN(tabuleiro)
        for mov in array:
            if mov == mov_escolhido:
                exec_jogadaMIN(mov_escolhido, tabuleiro)
                return
        print('movimento invalido!')
    

def movimento_valido(pm,estado):
    try:
        if estado[pm[0]][pm[1]] == 0:
            return True
        return False
    except:
        return False
       

def lista_de_possibilidadesMAX(estado): #possibilidades de jogadas para MAX (ovelhas)
    array_possib = []
    for item in L_ovelha:

        pm = [item[0]+1,item[1]-1] #pm = possibilidade de movimento  
        
        if movimento_valido(pm,estado):
            array_possib.append([item,pm])
        pm = [item[0]+1,item[1]+1]
        
        if movimento_valido(pm,estado):
            array_possib.append([item,pm]) 
    return array_possib


def lista_de_possibilidadesMIN(estado):
    array_possib = []
    pm = [localizacao_lobo[0]-1, localizacao_lobo[1]-1]#pm = possibilidade de movimento
    if movimento_valido(pm, estado):
        array_possib.append(pm)
    pm = [localizacao_lobo[0]-1, localizacao_lobo[1]+1]
    if movimento_valido(pm, estado):
        array_possib.append(pm)
    pm = [localizacao_lobo[0]+1, localizacao_lobo[1]-1]
    if movimento_valido(pm, estado):
        array_possib.append(pm)
    pm = [localizacao_lobo[0]+1, localizacao_lobo[1]+1]
    if movimento_valido(pm, estado):
        array_possib.append(pm)
    return array_possib



def exec_jogadaMAX(jogada,estado): #executa jogada para ovelhas
    aux = estado[jogada[0][0]][jogada[0][1]]
    estado[jogada[0][0]][jogada[0][1]] = estado[jogada[1][0]][jogada[1][1]]
    estado[jogada[1][0]][jogada[1][1]] = aux
    L_ovelha
    for i in range(len(L_ovelha)): 
        if L_ovelha[i] == jogada[0]:
            L_ovelha[i] = jogada[1]
            break
    return estado

def exec_jogadaMIN(jogada, estado): #atualliza posição do lobo
    #localizacao_lobo = [7,4]
    x,y = localizacao_lobo[0], localizacao_lobo[1]
    estado[jogada[0]][jogada[1]] = 'L'
    estado[x][y] = 0
    localizacao_lobo[0], localizacao_lobo[1] = jogada[0], jogada[1]
    return estado

    

def minimax(estado,jogador):
    
    # valor-minimax(estado) = avaliacao(estado)
    #caso base:
    if avaliacao(estado)!=0:
        placar = avaliacao(estado)
        return [-1, -1, placar]

    if jogador == COMP:
        melhor = [-1, -1, -infinity]
        listPMax = lista_de_possibilidadesMAX(estado)
        jogada_escolhida = null
        for jogada in listPMax:
            estad = exec_jogadaMAX(jogada, estado)
            placar = minimax(estad, HUMANO)
            placar[0],placar[1] = jogada[1][0],jogada[1][1]
            estad = exec_jogadaMAX(jogada, estado)

            if placar[2]>melhor[2]:
                melhor = placar
                jogada_escolhida = jogada
        return jogada_escolhida
    else:
        melhor = [-1, -1, +infinity]
        listPMin = lista_de_possibilidadesMIN(estado)
        jogada_escolhida = null
        casa_lobo = localizacao_lobo
        for jogada in listPMin:
            estad = exec_jogadaMIN(jogada, estado)
            placar = minimax(estad, COMP)
            placar[0],placar[1] = jogada[0],jogada[1]
            estad = exec_jogadaMIN(casa_lobo, estado)
            if placar[2]<melhor[2]:
                melhor = placar
                jogada_escolhida = jogada
        return jogada_escolhida







def IA_vez(jogada_inicial,estado):
    jini = jogada_inicial
    if jini ==True:
        jogada = choice(lista_de_possibilidadesMAX(tabuleiro))
        jini = False 
        exec_jogadaMAX(jogada,estado)
        return
    
    
    jogada = minimax(estado,COMP)
    exec_jogadaMAX(jogada, estado)
    return
    

    
    

    
    

"""
Funcao Principal que chama todas funcoes
"""
def main():
    while avaliacao(tabuleiro)==0:
        IA_vez(jogada_inicial, tabuleiro)
        limpa_console()
        time.sleep(1)
        exibe_tabuleiro(tabuleiro)
        HUMANO_vez()
    if avaliacao(tabuleiro) == 1:
        print('ovelha venceu!')
    else:
        print('ovelha perdeu!') 
    
    
    
   
    
    

if __name__ == '__main__':
    main()