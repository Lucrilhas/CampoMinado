# Jogo do Campo Minado
# Criado por: Lucas Elias de Andrade Cruvinel
# Esta aplicação tem o unico objetivo de aprender sobre pygame.
# Versão 3.0
# Email para contato: LucrilhasBR@hotmail.com

# Esse arquivo contém os imports, e a classe em que se passa o jogo

# Bibliotecas utilizadas :
import os   # Biblioteca usada para pegar caminho das imagens
import pygame   # Biblioteca usada para parte gráfica
import random   # Biblioteca que randomiza as bombas
import numpy as np  # Biblioteca que implementa de modo mais facil matrizes para melhor organização

# Constantes que armazenam as imagens necessárias:
IMAGENS_BLOCOS = [
    pygame.image.load(os.path.join("imgs", "bloco_zero.png")),  # 0
    pygame.image.load(os.path.join("imgs", "bloco_um.png")),  # 1
    pygame.image.load(os.path.join("imgs", "bloco_dois.png")),  # 2
    pygame.image.load(os.path.join("imgs", "bloco_tres.png")),  # 3
    pygame.image.load(os.path.join("imgs", "bloco_quatro.png")),  # 4
    pygame.image.load(os.path.join("imgs", "bloco_cinco.png")),  # 5
    pygame.image.load(os.path.join("imgs", "bloco_seis.png")),  # 6
    pygame.image.load(os.path.join("imgs", "bloco_sete.png")),  # 7
    pygame.image.load(os.path.join("imgs", "bloco_oito.png")),  # 8
    pygame.image.load(os.path.join("imgs", "bloco_fechado.png")),  # 9
    pygame.image.load(os.path.join("imgs", "bloco_bomba.png")),  # 10
    pygame.image.load(os.path.join("imgs", "bloco_bandeira_normal.png")),  # 11
    pygame.image.load(os.path.join("imgs", "bloco_bandeira_certa.png")),  # 12
    pygame.image.load(os.path.join("imgs", "bloco_bandeira_errada.png")),  # 13
    pygame.image.load(os.path.join("imgs", "bloco_zero.png"))]  # 14
IMAGEM_MENU = pygame.image.load(os.path.join("imgs", "menu.png"))

# Classe Tabuleiro que é onde se passa o jogo basicamente
class Tabuleiro:
    # Atributos da Classe:
    # Recebe o tamanho do tabuleiro e o número de bombas
    def __init__(self, num_blocos_x, num_blocos_y, num_bombas):
        self.primeira_jogada = True
        self.bomba_clickada = False
        self.acabou = False
        self.vencido = False
        self.tam_x = num_blocos_x
        self.tam_y = num_blocos_y
        self.num_bandeiras_restantes = num_bombas
        self.num_bombas = num_bombas
        self.matriz_backend = np.zeros([self.tam_y, self.tam_x])
        self.matriz_frontend = np.zeros([self.tam_y, self.tam_x])

    def inicia_matriz(self):
        for y in range(0, self.tam_y):
            for x in range(0, self.tam_x):
                self.matriz_frontend[y, x] = 9

    def randomiza_matriz(self, posy, posx):
        falta_bomba = self.num_bombas
        terminou = False
        while not terminou:
            random.seed()
            i = random.randrange(0, self.tam_y)
            j = random.randrange(0, self.tam_x)
            if not ((i == posy and j == posx) or (i == posy and j == posx - 1) or (i == posy and j == posx + 1) or (
                    i == posy - 1 and j == posx) or (i == posy - 1 and j == posx - 1) or (
                            i == posy - 1 and j == posx + 1) or (i == posy + 1 and j == posx) or (
                            i == posy + 1 and j == posx - 1) or (i == posy + 1 and j == posx + 1)) and (
                    self.matriz_backend[i, j] != 10):
                self.matriz_backend[i][j] = 10
                falta_bomba -= 1
                if falta_bomba == 0:
                    terminou = True

        for i in range(0, self.tam_y):
            for j in range(0, self.tam_x):
                if self.matriz_backend[i, j] == 10:
                    for aux01 in ARREDOR:
                        for aux02 in ARREDOR:
                            soma_i = i + aux01
                            soma_j = j + aux02
                            if 0 <= soma_i < self.tam_y and 0 <= soma_j < self.tam_x and self.matriz_backend[soma_i, soma_j] != 10:
                                self.matriz_backend[soma_i, soma_j] += 1

    def expansao(self, y, x):
        self.matriz_frontend[y, x] = 14
        for aux01 in ARREDOR:
            for aux02 in ARREDOR:
                soma_y = y + aux01
                soma_x = x + aux02
                if 0 <= soma_y < self.tam_y and 0 <= soma_x < self.tam_x:
                    if self.matriz_frontend[soma_y, soma_x] == 9 and self.matriz_backend[soma_y, soma_x] == 0:
                        self.expansao(soma_y, soma_x)
                    self.matriz_frontend[soma_y, soma_x] = self.matriz_backend[soma_y, soma_x]
                    if self.matriz_frontend[soma_y, soma_x] == 0:
                        self.matriz_frontend[soma_y, soma_x] = 14

    def desenha_frontend(self, janela):
        for y in range(0, self.tam_y):
            for x in range(0, self.tam_x):
                for k in range(0, 15):
                    if self.matriz_frontend[y, x] == k:
                        janela.blit(IMAGENS_BLOCOS[k], (10 + y * 55, 105 + x * 55))
