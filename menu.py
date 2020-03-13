# Jogo do Campo Minado
# Criado por: Lucas Elias de Andrade Cruvinel
# Esta aplicação tem o unico objetivo de aprender sobre pygame.
# Versão 3.0
# Email para contato: LucrilhasBR@hotmail.com

from jogo import *

IMAGENS_MENU = [
    pygame.image.load(os.path.join("imgs", "fundo_menu_principal.png")),  # 0
    pygame.image.load(os.path.join("imgs", "fundo_menu_jogo.png")),  # 1
    pygame.image.load(os.path.join("imgs", "fundo_menu_highscore.png")),  # 2
    pygame.image.load(os.path.join("imgs", "fundo_menu_tutorial.png")),  # 3
    pygame.image.load(os.path.join("imgs", "fundo_menu_creditos.png"))]  # 4
IMAGEM_TECLADO = pygame.image.load(os.path.join("imgs", "digita.png"))
TECLADO = (
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '_', 'Z', 'X', 'C',
    'V', 'B', 'N', 'M', 'DEL')
TAM_JANELA = (400, 500)


def pega_nome(janela):
    nome = ''
    num_letras = 0
    terminou = False
    while not terminou:
        janela = pygame.display.set_mode((TAM_JANELA[0], TAM_JANELA[1]))
        pygame.display.set_caption('MENU')
        janela.blit(IMAGEM_TECLADO, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if 373 <= pos_mouse[1] <= 405:
                    for aux in range(0, 10):
                        if 17 + (aux * 37) <= pos_mouse[0] <= 48 + (aux * 37) and num_letras < 5:
                            nome = nome + TECLADO[aux]
                            num_letras += 1
                elif 414 <= pos_mouse[1] <= 447:
                    for aux in range(0, 9):
                        if 34 + (aux * 37) <= pos_mouse[0] <= 68 + (aux * 37) and num_letras < 5:
                            nome = nome + TECLADO[aux + 10]
                            num_letras += 1
                elif 454 <= pos_mouse[1] <= 487:
                    for aux in range(0, 9):
                        if 34 + (aux * 37) <= pos_mouse[0] <= 68 + (aux * 37):
                            if num_letras < 5:
                                nome = nome + TECLADO[aux + 19]
                                num_letras += 1
                            if aux + 19 == 27:
                                nome = ''
                                num_letras = 0
                elif 5 <= pos_mouse[0] <= 145 and 230 <= pos_mouse[1] <= 245:
                    return nome

        if num_letras == 5:
            texto_finalizar = pega_fonte(10).render("CLIQUE AQUI PARA TERMINAR", 1, (255, 255, 255))
            janela.blit(texto_finalizar, (8, 230))
        texto_nome = pega_fonte(20).render(nome, 1, (255, 255, 255))
        janela.blit(texto_nome, (25, 200))
        pygame.display.update()


def main():
    pygame.display.init()
    qual_janela_menu = 0
    pygame.display.init()

    custom_linhas = 10
    custom_colunas = 10
    custom_bombas = 10

    while True:
        janela = pygame.display.set_mode((TAM_JANELA[0], TAM_JANELA[1]))
        pygame.display.set_caption('MENU')

        for aux in range(5):
            if qual_janela_menu == aux:
                janela.blit(IMAGENS_MENU[qual_janela_menu], (0, 0))
            if qual_janela_menu == 1:
                custom_text_lin = pega_fonte(30).render(str(custom_linhas), 1, (0, 0, 0))
                custom_text_col = pega_fonte(30).render(str(custom_colunas), 1, (0, 0, 0))
                custom_text_bom = pega_fonte(30).render(str(custom_bombas), 1, (0, 0, 0))

                janela.blit(custom_text_lin, (270, 235))
                janela.blit(custom_text_col, (270, 295))
                janela.blit(custom_text_bom, (270, 355))
            elif qual_janela_menu == 2:
                top_nome = np.empty(3).tolist()
                top_pontos = np.empty(3).tolist()
                facil = open("highscore_facil.txt")
                for aux02 in range(0, 3):
                    top_nome[aux02] = facil.readline().strip()
                    top_pontos[aux02] = facil.readline().strip()
                    melhores_nomes = pega_fonte(20).render(str(top_nome[aux02]), 1, (0, 0, 0))
                    melhores_pontos = pega_fonte(20).render(str(top_pontos[aux02]), 1, (0, 0, 0))
                    if aux02 == 0:
                        janela.blit(melhores_nomes, (20, 90))
                        janela.blit(melhores_pontos, (20, 110))
                    if aux02 == 1:
                        janela.blit(melhores_nomes, (20, 200))
                        janela.blit(melhores_pontos, (20, 220))
                    if aux02 == 2:
                        janela.blit(melhores_nomes, (20, 330))
                        janela.blit(melhores_pontos, (20, 350))
                facil.close()

                medio = open("highscore_medio.txt")
                for aux02 in range(0, 3):
                    top_nome[aux02] = medio.readline().strip()
                    top_pontos[aux02] = medio.readline().strip()
                    melhores_nomes = pega_fonte(20).render(str(top_nome[aux02]), 1, (0, 0, 0))
                    melhores_pontos = pega_fonte(20).render(str(top_pontos[aux02]), 1, (0, 0, 0))
                    if aux02 == 0:
                        janela.blit(melhores_nomes, (150, 90))
                        janela.blit(melhores_pontos, (150, 110))
                    if aux02 == 1:
                        janela.blit(melhores_nomes, (150, 200))
                        janela.blit(melhores_pontos, (150, 220))
                    if aux02 == 2:
                        janela.blit(melhores_nomes, (150, 330))
                        janela.blit(melhores_pontos, (150, 350))
                medio.close()

                dificil = open("highscore_dificil.txt")
                for aux02 in range(0, 3):
                    top_nome[aux02] = dificil.readline().strip()
                    top_pontos[aux02] = dificil.readline().strip()
                    melhores_nomes = pega_fonte(20).render(str(top_nome[aux02]), 1, (0, 0, 0))
                    melhores_pontos = pega_fonte(20).render(str(top_pontos[aux02]), 1, (0, 0, 0))
                    if aux02 == 0:
                        janela.blit(melhores_nomes, (300, 90))
                        janela.blit(melhores_pontos, (300, 110))
                    if aux02 == 1:
                        janela.blit(melhores_nomes, (300, 200))
                        janela.blit(melhores_pontos, (300, 220))
                    if aux02 == 2:
                        janela.blit(melhores_nomes, (300, 330))
                        janela.blit(melhores_pontos, (300, 350))
                dificil.close()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                if qual_janela_menu == 0:
                    if 310 <= pos_mouse[0] <= 385 and 445 <= pos_mouse[1] <= 485:
                        quit()
                    elif 70 <= pos_mouse[0] <= 325:
                        if 110 <= pos_mouse[1] <= 170:
                            qual_janela_menu = 1
                        elif 200 <= pos_mouse[1] <= 265:
                            qual_janela_menu = 2
                        elif 285 <= pos_mouse[1] <= 345:
                            qual_janela_menu = 3
                        elif 375 <= pos_mouse[1] <= 430:
                            qual_janela_menu = 4

                elif qual_janela_menu == 2:
                    if 159 <= pos_mouse[0] <= 229 and 434 <= pos_mouse[1] <= 455:
                        qual_janela_menu = 0

                elif qual_janela_menu == 3:
                    if 5 <= pos_mouse[0] <= 395 and 405 <= pos_mouse[1] <= 495:
                        qual_janela_menu = 0

                elif qual_janela_menu == 4:
                    if 310 <= pos_mouse[0] <= 385 and 445 <= pos_mouse[1] <= 485:
                        qual_janela_menu = 0

                elif qual_janela_menu == 1:
                    if custom_bombas > (custom_colunas * custom_linhas) - 9:
                        custom_bombas = (custom_colunas * custom_linhas) - 9

                    if 275 <= pos_mouse[0] <= 399 and 425 <= pos_mouse[1] <= 499:
                        qual_janela_menu = 0

                    elif 350 <= pos_mouse[0] <= 373 and 240 <= pos_mouse[1] <= 263 and custom_linhas <= 30:
                        custom_linhas += 1
                    elif 348 <= pos_mouse[0] <= 370 and 302 <= pos_mouse[1] <= 325 and custom_colunas <= 30:
                        custom_colunas += 1
                    elif 349 <= pos_mouse[0] <= 371 and 364 <= pos_mouse[1] <= 387 and custom_bombas <= (
                            custom_colunas * custom_linhas) - 9:
                        custom_bombas += 1
                    elif 202 <= pos_mouse[0] <= 228 and 249 <= pos_mouse[1] <= 256 and custom_linhas > 5:
                        custom_linhas -= 1
                    elif 200 <= pos_mouse[0] <= 226 and 307 <= pos_mouse[1] <= 314 and custom_colunas > 5:
                        custom_colunas -= 1
                    elif 198 <= pos_mouse[0] <= 224 and 372 <= pos_mouse[1] <= 379 and custom_bombas > 1:
                        custom_bombas -= 1

                    elif 16 <= pos_mouse[0] <= 194 and 115 <= pos_mouse[1] <= 207:
                        ponto_valor = jogo(9, 9, 10, True)
                        top_nome = np.empty(3).tolist()
                        top_pontos = np.empty(3).tolist()
                        pontuacoes = open('highscore_facil.txt')
                        for aux in range(0, 3):
                            top_nome[aux] = pontuacoes.readline().strip()
                            top_pontos[aux] = pontuacoes.readline().strip()
                            top_pontos[aux] = int(top_pontos[aux])
                        pontuacoes.close()
                        if ponto_valor < top_pontos[0]:
                            top_pontos[2] = top_pontos[1]
                            top_pontos[1] = top_pontos[0]
                            top_pontos[0] = ponto_valor
                            top_nome[2] = top_nome[1]
                            top_nome[1] = top_nome[0]
                            top_nome[0] = pega_nome(janela)
                        elif ponto_valor < top_pontos[1]:
                            top_pontos[2] = top_pontos[1]
                            top_pontos[1] = ponto_valor
                            top_nome[2] = top_nome[1]
                            top_nome = pega_nome(janela)
                        elif ponto_valor < top_pontos[2]:
                            top_pontos[2] = ponto_valor
                            top_nome[2] = pega_nome(janela)

                        pontuacoes = open('highscore_facil.txt', 'w')
                        for aux in range(0, 3):
                            pontuacoes.write(top_nome[aux])
                            pontuacoes.write('\n')
                            pontuacoes.write(str(top_pontos[aux]))
                            pontuacoes.write('\n')
                        pontuacoes.close()

                    elif 15 <= pos_mouse[0] <= 193 and 224 <= pos_mouse[1] <= 316:
                        ponto_valor = jogo(16, 16, 40, True)
                        top_nome = np.empty(3).tolist()
                        top_pontos = np.empty(3).tolist()
                        pontuacoes = open('highscore_medio.txt')
                        for aux in range(0, 3):
                            top_nome[aux] = pontuacoes.readline().strip()
                            top_pontos[aux] = pontuacoes.readline().strip()
                            top_pontos[aux] = int(top_pontos[aux])
                        pontuacoes.close()
                        if ponto_valor < top_pontos[0]:
                            top_pontos[2] = top_pontos[1]
                            top_pontos[1] = top_pontos[0]
                            top_pontos[0] = ponto_valor
                            top_nome[2] = top_nome[1]
                            top_nome[1] = top_nome[0]
                            top_nome[0] = pega_nome(janela)
                        elif ponto_valor < top_pontos[1]:
                            top_pontos[2] = top_pontos[1]
                            top_pontos[1] = ponto_valor
                            top_nome[2] = top_nome[1]
                            top_nome = pega_nome(janela)
                        elif ponto_valor < top_pontos[2]:
                            top_pontos[2] = ponto_valor
                            top_nome[2] = pega_nome(janela)

                        pontuacoes = open('highscore_medio.txt', 'w')
                        for aux in range(0, 3):
                            pontuacoes.write(top_nome[aux])
                            pontuacoes.write('\n')
                            pontuacoes.write(str(top_pontos[aux]))
                            pontuacoes.write('\n')
                        pontuacoes.close()

                    elif 12 <= pos_mouse[0] <= 190 and 333 <= pos_mouse[1] <= 425:
                        ponto_valor = jogo(24, 24, 99, True)
                        top_nome = np.empty(3).tolist()
                        top_pontos = np.empty(3).tolist()
                        pontuacoes = open('highscore_dificil.txt')
                        for aux in range(0, 3):
                            top_nome[aux] = pontuacoes.readline().strip()
                            top_pontos[aux] = pontuacoes.readline().strip()
                            top_pontos[aux] = int(top_pontos[aux])
                        pontuacoes.close()
                        if ponto_valor < top_pontos[0]:
                            top_pontos[2] = top_pontos[1]
                            top_pontos[1] = top_pontos[0]
                            top_pontos[0] = ponto_valor
                            top_nome[2] = top_nome[1]
                            top_nome[1] = top_nome[0]
                            top_nome[0] = pega_nome(janela)
                        elif ponto_valor < top_pontos[1]:
                            top_pontos[2] = top_pontos[1]
                            top_pontos[1] = ponto_valor
                            top_nome[2] = top_nome[1]
                            top_nome = pega_nome(janela)
                        elif ponto_valor < top_pontos[2]:
                            top_pontos[2] = ponto_valor
                            top_nome[2] = pega_nome(janela)

                        pontuacoes = open('highscore_dificil.txt', 'w')
                        for aux in range(0, 3):
                            pontuacoes.write(top_nome[aux])
                            pontuacoes.write('\n')
                            pontuacoes.write(str(top_pontos[aux]))
                            pontuacoes.write('\n')
                        pontuacoes.close()

                    elif 211 <= pos_mouse[0] <= 389 and 115 <= pos_mouse[1] <= 207:
                        jogo(custom_linhas, custom_colunas, custom_bombas, False)

        pygame.display.update()


if __name__ == '__main__':
    main()
