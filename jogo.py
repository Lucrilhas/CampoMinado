# Jogo do Campo Minado
# Criado por: Lucas Elias de Andrade Cruvinel
# Esta aplicação tem o unico objetivo de aprender sobre pygame.
# Versão 3.0
# Email para contato: LucrilhasBR@hotmail.com

# Este arquivo é o responsável pelo funcionamento e coordenação do jogo
# Caso o menu não seja do seu agrado, é possivel inicializar por aqui fazendo poucas
# modificações no código, como por exemplo fazer com que a função jogo seja a primeira a rodar
# trocar seu parametros para que já vá com quantas linhas, colunas e bombas voce quer
# Também é uma boa ideia tirar os returns já que não terá para onde retornar
# Talvez tenha que ainda fazer mais alguma alteração em alguma parte caso retire o menu
# Mas aí tu vê aí oque tu faz

# Algumas funções não estão documentadas aqui pois estão já no arquivo da classe

from class_tabuleiro import *  # Função que importa _todo o arquivo class_tabuleiro


# Função que aumenta a praticidade ao pegar um fonte com tamanho diferente
def pega_fonte(tam_fonte):
    pygame.font.init()  # Pega as fontes do pygame
    return pygame.font.Font("fonts/franklin-gothic-medium.ttf", tam_fonte)


# Função que desenha tudo na tela e detecta se o jogo acabou
def desenha_janela(janela, tabua, tam_janela_jogo, pontos):
    # Seta os textos e fundos para desenhar na tela
    texto_bandeira = pega_fonte(50).render("Bandeiras: " + str(tabua.num_bandeiras_restantes), 1, (150, 150, 150))
    texto_final_vitoria = pega_fonte(50).render("Ganhastes :)", 1, (255, 255, 0))
    texto_final_derrota = pega_fonte(50).render("Perdestes ;-;", 1, (255, 255, 0))
    texto_pontos = pega_fonte(30).render("Tempo: " + str(pontos), 1, (150, 150, 150))

    fundo_cinza = pygame.Rect((5, 100, tam_janela_jogo[0] - 10, tam_janela_jogo[1] - 105))
    fundo_bandeiras = pygame.Rect(5, 5, tam_janela_jogo[0] - 120, 90)
    fundo_return = pygame.Rect(tam_janela_jogo[0] - 110, 5, 105, 90)

    # Desenha na tela
    janela.fill((36, 36, 36))
    janela.fill((72, 72, 72), fundo_cinza)
    janela.fill((72, 72, 72), fundo_bandeiras)
    janela.fill((72, 72, 72), fundo_return)
    janela.blit(IMAGEM_MENU, (tam_janela_jogo[0] - 100, 10))
    janela.blit(texto_bandeira, (15, 40))
    janela.blit(texto_pontos, (15, 15))
    tabua.desenha_frontend(janela)

    # As condições a seguir são para detectar se clickaram na bomba
    # Se sim ele acaba o jogo e desenha na tela avisaando e mostrando as bandeiras erradas
    # as certas e as bombas que faltaram
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

    # As as condições a seguir são para verificar se o jogador colocou todas as bandeiras no lugar certo
    # Se sim, o jogador vence e é desenhado na tela para mostrar
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

    pygame.display.update()  # Função que atualiza a janela pelo pygame


# Função onde roda as engrenagens do jogo
# Ele começa recebendo do menu o num de blocos nas colunas e nas linhas assim como o numero de bombas
# tudo isso decidido pelo jogador
# Tambem recebe um valor booleano para mostrar se esse é um jogo que vale posição no highscore
# Apenas jogos que estiverem em uma das dificuldades pré-definidas podem ir para o highscore
def jogo(num_blocos_x, num_blocos_y, num_bombas, ranked):
    tam_janela_jogo = (15 + (55 * num_blocos_y), 110 + (55 * num_blocos_x))  # Muda o tamanho da janela de acordo
    janela = pygame.display.set_mode(tam_janela_jogo)
    pygame.display.set_caption('Minas')  # Muda o título da janela
    clock = pygame.time.Clock()
    tabua = Tabuleiro(num_blocos_x, num_blocos_y, num_bombas)  # Cria um objeto tabuleiro que é onde se passa ESSE jogo
    tabua.inicia_matriz()  # Seta o frontend do tabuleiro para iniciar o jogo

    cronometro = 0  # Começa o crnometro
    pontos = 0  # Começam os pontos

    # Loop em que se passa os jogos:
    while not tabua.acabou:
        clock.tick(60)  # Seta o clock
        # Cronometro e pontos rodano:
        cronometro += 1
        pontos = int(cronometro / 10)
        for event in pygame.event.get():  # Registra os eventos do jogo
            if event.type == pygame.QUIT:  # Caso tenha um registro de saída, ele sái
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Detecta o evento de click do mous, pode ser de qualquer botão
                # A seguir ele procura onde foi o clique e o discretiza em um uma das posições do bloco
                for y in range(0, tabua.tam_y):
                    for x in range(0, tabua.tam_x):
                        pos_mouse = pygame.mouse.get_pos()
                        # A seguir ele detecta se a pessoa clickou no botão de voltar ao menu
                        # Caso tenha clickado, ele volta ao menu
                        if tam_janela_jogo[0] - 110 <= pos_mouse[0] <= tam_janela_jogo[0] - 5 and \
                                5 <= pos_mouse[1] <= 95:
                            tabua.acabou = True

                        # Especificamente nessa condição a seguir é onde ele descobre em qual bloco foi clickado:
                        if (10 + y * 55 <= pos_mouse[0] < 60 + y * 55) and (
                                105 + x * 55 <= pos_mouse[1] < 155 + x * 55):
                            # Se foi clickado com botão esquerdo do mouse:
                            # Descobre o que tem por trás do botão coberto
                            if event.button == 1:
                                if tabua.primeira_jogada:  # Caso seja a primeira rodada, ele ainda vai criar a matriz
                                    tabua.matriz_frontend[y, x] = 0
                                    tabua.primeira_jogada = False
                                    tabua.randomiza_matriz(y, x)
                                else:
                                    if tabua.matriz_backend[y, x] == 10:
                                        tabua.bomba_clickada = True
                                    tabua.matriz_frontend[y, x] = tabua.matriz_backend[y, x]

                                if tabua.matriz_frontend[y, x] == 0:
                                    tabua.expansao(y, x)

                            # Se foi clickado com botão direito do mouse:
                            # Coloca uma bandeira por cima de um botão coberto
                            # para vencer é preciso colocar uma bandeira em cima de cada bomba
                            # Ele não é abilidado na primeira partida pois não tem por que colocar uma bandeira
                            # na primeira rodada
                            elif event.button == 3 and not tabua.primeira_jogada:
                                if tabua.matriz_frontend[y, x] == 9 and tabua.num_bandeiras_restantes > 0:
                                    tabua.matriz_frontend[y, x] = 11
                                    tabua.num_bandeiras_restantes -= 1
                                elif tabua.matriz_frontend[y, x] == 11:
                                    tabua.matriz_frontend[y, x] = 9
                                    tabua.num_bandeiras_restantes += 1

        # Começa a função que desenha e verifica se acabou o jogo
        desenha_janela(janela, tabua, tam_janela_jogo, pontos)

    # Retorna os valore para o ranking:
    if ranked:
        if tabua.vencido:
            return pontos
        else:
            return 1000000
