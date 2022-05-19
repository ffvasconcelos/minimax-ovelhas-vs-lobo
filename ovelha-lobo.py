#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMANO = -1
COMP = +1
localizacao_lobo = [7,4]
tabuleiro = [
    [0, 'V', 0, 'V', 0, 'V', 0, 'V',],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 'L', 0, 0, 0,],
    
]

"""
Funcao para avaliacao heuristica do estado.
:parametro (estado): o estado atual do tabuleiro
:returna: +1 se o computador vence; -1 se o HUMANOo vence; 0 empate
 """
def avaliacao(estado):
    
    if vitoria(estado, COMP):
        placar = +1
    elif vitoria(estado, HUMANO):
        placar = -1
    else:
        placar = 0

    return placar
""" fim avaliacao (estado)------------------------------------- """

def vitoria(estado, jogador):
    """
    Esta funcao testa se um jogador especifico vence. Possibilidades:
    * Se jogador = lobo:    
                        - se lobo esta na linha 0 -> lobo venceu, retorna true
                        - else, lobo nao venceu -> retorna false
    * Se jogador = ovelha:
                        - se lobo não tem nenhum movimento valido -> ovelha venceu, retorna true
                        - else, ovelha não venceu ->retona false
    * Duas diagonais  [X X X] or [O O O]
    :param. (estado): o estado atual do tabuleiro
    :param. (jogador): um HUMANO ou um Computador
    :return: True se jogador vence
    """
    if (jogador == 'L'):
        for i in estado[0]:
            if estado[0][i] == 'L': return True
        return False
    if (jogador == 'V'):
        """ se lobo não tem nenhum movimento valido -> ovelha venceu, retorna true
            else -> return false
         """
        return True
""" ---------------------------------------------------------- """
"""
Testa fim de jogo para ambos jogadores de acordo com estado atual
return: será fim de jogo caso ocorra vitória de um dos jogadores.
"""
def fim_jogo(estado):
    return vitoria(estado, HUMANO) or vitoria(estado, COMP)
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
"""
Verifica celular vazias e insere na lista para informar posições
ainda permitidas para próximas jogadas.
"""
def celulas_vazias(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 0: celulas.append([x, y])
    return celulas
""" ---------------------------------------------------------- """
"""
Um movimento é valido se a célula escolhida está vazia.
:param (x): coordenada X
:param (y): coordenada Y
:return: True se o tabuleiro[x][y] está vazio
"""
def movimento_valido(x, y):
    if [x, y] in celulas_vazias(tabuleiro):
        return True
    else:
        return False
""" ---------------------------------------------------------- """
"""
Executa o movimento no tabuleiro se as coordenadas são válidas
:param (x): coordenadas X
:param (y): coordenadas Y
:param (jogador): o jogador da vez
"""
def exec_movimento(x, y, jogador):
    if movimento_valido(x, y):
        tabuleiro[x][y] = jogador
        return True
    else:
        return False
""" ---------------------------------------------------------- """
def limpar_posicao(x,y):
    tabuleiro[x][y] = 0
""" ---------------------------------------------------------- """
def HUMANO_vez():
    limpa_console()
    print('Vez do HUMANO: ')
    exibe_tabuleiro(tabuleiro)
    l = int(input('Escolha a linha [0-7]'))  # l= linha
    c = int(input('Escolha a coluna [0-7]')) # c = coluna
            # Dicionário de movimentos válidos
    movimentos = {
        1: [localizacao_lobo[0]+1, localizacao_lobo[1]+1], 
        2: [localizacao_lobo[0]+1, localizacao_lobo[1]-1],
        3: [localizacao_lobo[0]-1, localizacao_lobo[1]+1], 
        4: [localizacao_lobo[0]-1, localizacao_lobo[1]-1]
    }
    if movimento_valido(l, c):
        for i in movimentos:
            cord = movimentos[i]
            if cord[0] == l and cord[1] == c:
                limpar_posicao(localizacao_lobo[0],localizacao_lobo[1])
                localizacao_lobo[0] = l
                localizacao_lobo[1] = c
                exec_movimento(l, c,'L')
                exibe_tabuleiro(tabuleiro)
                movimento = True
                break
    else:
        print('movimento invalido!\n')
        time.sleep(2)
    print('legal legal')
       
        
        


        

        

    

"""
Funcao Principal que chama todas funcoes
"""
def main():
    for i in range(4):
        HUMANO_vez()
   
    
    

if __name__ == '__main__':
    main()