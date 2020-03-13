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
import time     # Biblioteca ussada para parar o código por um certo tempo
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
        self.primeira_jogada = True     # Variavel que indica se essa é a primeira jogana na partida
        self.bomba_clickada = False     # Variavel que indica se alguma bomba foi clickada
        self.acabou = False             # variavel que indica se acabou o jogo
        self.vencido = False            # Variavel que indica se o jogador venceu essa partida
        self.tam_x = num_blocos_x       # Variavel que indica o tamanho do tabuleiro no eixo x
        self.tam_y = num_blocos_y       # Variavel que indica o tamanho do tabuleiro no eixo x
        self.num_bandeiras_restantes = num_bombas   # Variavel que indica o número de bandeira que restam no jogo
        self.num_bombas = num_bombas                # Variavel que indica o número total de bombas
        self.matriz_backend = np.zeros([self.tam_y, self.tam_x])    # Matriz em que se passa o backend do tabuleiro
        self.matriz_frontend = np.zeros([self.tam_y, self.tam_x])   # matriz em que se passa o frontend do tabuleiro ou seja, o que o jogador vê

    # Função que inicia a matriz, ocultando todas as peças to jogo, embora na verdade não tenha nada por baixo
    def inicia_matriz(self):
        for y in range(0, self.tam_y):
            for x in range(0, self.tam_x):
                # Transforma todas as peças frontend em blocos ocultos cujo ID é 9
                self.matriz_frontend[y, x] = 9

    # Função que randomiza o lugar onde terá bombas
    # E depois a partir da posição das bombas se constroi o resto do tabuleiro
    # Nota-se que há condições que fazem com que a primeira peça clickada sempre seja 0
    # Ou seja, nela e ao redor não pode haver bombas
    # Por isso se criam as bombas apenas depois do primeiro click, que justamente o que se recebe nessa função:
    # A localização do primeiro click
    def randomiza_matriz(self, posy, posx):
        # Essa primeira parte da função serve para randomizar a posição das bombas
        # Porém não pode ter bomba nas proximidades do primeiro lugar a ser clickado
        # Pois ele é um bloco 0
        bombas_para_colocar = self.num_bombas
        terminou = False
        while not terminou:
            cont = 0
            random.seed()
            y = random.randrange(0, self.tam_y)
            x = random.randrange(0, self.tam_x)
            if self.matriz_backend[y, x] != 10:
                for aux01 in range(-1, 2):
                    for aux02 in range(-1, 2):
                        arredores = [posy + aux01, posx + aux02]
                        if not (arredores[0] == y and arredores[1] == x):
                            cont += 1
            if cont == 9:
                self.matriz_backend[y, x] = 10
                bombas_para_colocar -= 1
                if bombas_para_colocar == 0:
                    terminou = True

        # Essa segunda parte busca as bombas pela matriz e quando acha aumenta o número na proximidade da bomba
        # Indicando quantas bombas tem na proximidade do número
        for y in range(0, self.tam_y):
            for x in range(0, self.tam_x):
                if self.matriz_backend[y, x] == 10:
                    for aux01 in range(-1, 2):
                        for aux02 in range(-1, 2):
                            soma_y = y + aux01
                            soma_x = x + aux02
                            if 0 <= soma_y < self.tam_y and 0 <= soma_x < self.tam_x and self.matriz_backend[soma_y, soma_x] != 10:
                                self.matriz_backend[soma_y, soma_x] += 1

    # Essa função tem uma importância mais gráfica, ela faz com que ao clickar em um bloco zero
    # Todos os blocos adjacentes aparecem, além de que se tiver um bloco adjacente zero
    # Ele tambem revela ao redor, liberando assim toda uma área do tabuleiro
    # Embora não seja uma função central do jogo, sem ela o jogo acaba se tornando maçante e chato além
    # de possibilitar tempos menores para speedruns
    # Nela é usada de recursão
    def expansao(self, y, x):
        self.matriz_frontend[y, x] = 14
        for aux01 in range(-1, 2):
            for aux02 in range(-1, 2):
                soma_y = y + aux01
                soma_x = x + aux02
                if 0 <= soma_y < self.tam_y and 0 <= soma_x < self.tam_x:
                    if self.matriz_frontend[soma_y, soma_x] == 9 and self.matriz_backend[soma_y, soma_x] == 0:
                        self.expansao(soma_y, soma_x)
                    self.matriz_frontend[soma_y, soma_x] = self.matriz_backend[soma_y, soma_x]
                    if self.matriz_frontend[soma_y, soma_x] == 0:
                        self.matriz_frontend[soma_y, soma_x] = 14

    # Essa é a função responsável pela atualização contante entre o backend e o frontend
    # Tambem é o que imprime o frontend na tela
    def desenha_frontend(self, janela):
        for y in range(0, self.tam_y):
            for x in range(0, self.tam_x):
                for k in range(0, 15):
                    if self.matriz_frontend[y, x] == k:
                        janela.blit(IMAGENS_BLOCOS[k], (10 + y * 55, 105 + x * 55))
