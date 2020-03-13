# Jogo do Campo Minado
# Criado por: Lucas Elias de Andrade Cruvinel
# Esta aplicação tem o unico objetivo de aprender sobre pygame.
# Versão 3.0
# Email para contato: LucrilhasBR@hotmail.com

from class_tabuleiro import *


def pega_fonte(tam_fonte):
    pygame.font.init()  # Pega as fontes do pygame
    return pygame.font.Font("fonts/franklin-gothic-medium.ttf", tam_fonte)


def desenha_janela(janela, tabua, tam_janela_jogo, pontos):
    texto_bandeira = pega_fonte(50).render("Bandeiras: " + str(tabua.num_bandeiras_restantes), 1, (150, 150, 150))
    texto_final_vitoria = pega_fonte(50).render("Ganhastes :)", 1, (255, 255, 0))
    texto_final_derrota = pega_fonte(50).render("Perdestes ;-;", 1, (255, 255, 0))
    texto_pontos = pega_fonte(30).render("Tempo: " + str(pontos), 1, (150, 150, 150))

    fundo_cinza = pygame.Rect((5, 100, tam_janela_jogo[0] - 10, tam_janela_jogo[1] - 105))
    fundo_bandeiras = pygame.Rect(5, 5, tam_janela_jogo[0] - 120, 90)
    fundo_return = pygame.Rect(tam_janela_jogo[0] - 110, 5, 105, 90)

    janela.fill((36, 36, 36))
    janela.fill((72, 72, 72), fundo_cinza)
    janela.fill((72, 72, 72), fundo_bandeiras)
    janela.fill((72, 72, 72), fundo_return)
    janela.blit(IMAGEM_MENU, (tam_janela_jogo[0] - 100, 10))
    janela.blit(texto_bandeira, (15, 40))
    janela.blit(texto_pontos, (15, 15))
    tabua.desenha_frontend(janela)

    if tabua.bomba_clickada:
        for y in range(0, tabua.tam_y):
            for x in range(0, tabua.tam_x):
                if (tabua.matriz_backend[y, x] == 10 and tabua.matriz_frontend[y, x] == 9) or (
                        tabua.matriz_backend[y, x] == 10 and tabua.matriz_frontend[y, x] == 10):
                    tabua.matriz_frontend[y, x] = 10
                elif tabua.matriz_backend[y, x] == 10 and tabua.matriz_frontend[y, x] == 11:
                    tabua.matriz_frontend[y, x] = 12
                elif tabua.matriz_backend[y, x] != 10 and tabua.matriz_frontend[y, x] == 11:
                    tabua.matriz_frontend[y, x] = 13

        tabua.desenha_frontend(janela)
        janela.fill((72, 72, 72), fundo_bandeiras)
        janela.blit(texto_final_derrota, (15, 40))
        pygame.display.update()
        time.sleep(3)
        tabua.acabou = True

    if tabua.num_bandeiras_restantes == 0:
        acertos = 0
        for y in range(0, tabua.tam_y):
            for x in range(0, tabua.tam_x):
                if tabua.matriz_frontend[y, x] == 11 and tabua.matriz_backend[y, x] == 10:
                    acertos += 1
                    if acertos == tabua.num_bombas:
                        for aux01 in range(0, tabua.tam_y):
                            for aux02 in range(0, tabua.tam_x):
                                if tabua.matriz_frontend[y, x] == 11:
                                    tabua.matriz_frontend[y, x] = 12

                        janela.fill((72, 72, 72), fundo_bandeiras)
                        janela.blit(texto_final_vitoria, (15, 40))
                        pygame.display.update()
                        time.sleep(3)
                        tabua.acabou = True
                        tabua.vencido = True

    pygame.display.update()


def jogo(num_blocos_x, num_blocos_y, num_bombas, ranked):
    tam_janela_jogo = (15 + (55 * num_blocos_y), 110 + (55 * num_blocos_x))
    janela = pygame.display.set_mode(tam_janela_jogo)
    pygame.display.set_caption('Minas')
    clock = pygame.time.Clock()
    tabua = Tabuleiro(num_blocos_x, num_blocos_y, num_bombas)
    tabua.inicia_matriz()

    cronometro = 0
    pontos = 0

    while not tabua.acabou:
        clock.tick(60)
        cronometro += 1
        pontos = int(cronometro / 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for y in range(0, tabua.tam_y):
                    for x in range(0, tabua.tam_x):
                        pos_mouse = pygame.mouse.get_pos()
                        if tam_janela_jogo[0] - 110 <= pos_mouse[0] <= tam_janela_jogo[0] - 5 and\
                                5 <= pos_mouse[1] <= 95:
                            tabua.acabou = True

                        if (10 + y * 55 <= pos_mouse[0] < 60 + y * 55) and (105 + x * 55 <= pos_mouse[1] < 155 + x * 55):
                            if event.button == 1:
                                if tabua.primeira_jogada:
                                    tabua.matriz_frontend[y, x] = 0
                                    tabua.primeira_jogada = False
                                    tabua.randomiza_matriz(y, x)
                                else:
                                    if tabua.matriz_backend[y, x] == 10:
                                        tabua.bomba_clickada = True
                                    tabua.matriz_frontend[y, x] = tabua.matriz_backend[y, x]

                                if tabua.matriz_frontend[y, x] == 0:
                                    tabua.expansao(y, x)

                            elif event.button == 3 and not tabua.primeira_jogada:
                                if tabua.matriz_frontend[y, x] == 9 and tabua.num_bandeiras_restantes > 0:
                                    tabua.matriz_frontend[y, x] = 11
                                    tabua.num_bandeiras_restantes -= 1
                                elif tabua.matriz_frontend[y, x] == 11:
                                    tabua.matriz_frontend[y, x] = 9
                                    tabua.num_bandeiras_restantes += 1

        desenha_janela(janela, tabua, tam_janela_jogo, pontos)

    if ranked:
        if tabua.vencido:
            return pontos
        else:
            return 1000000
