import pygame
import random

pygame.init()

preto = (0,0,0)
laranja = (205,102,0)
verde = (0,255,0)
amarelo = (255,255,102)

dimensoes = (600,600)

x = 300  #define o lugar inicial da cobrinha
y = 300

d = 20  #dimensão do quadrado (20 pxl)

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20  #calculo para ter certeza que o quadrado da unidade da cobra fique alinhado com o quadrado da comida
y_comida = round(random.randrange(0, 600 - d) / 20) * 20

fonte = pygame.font.SysFont("hack",35)

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake da Kenzie')

tela.fill(preto)  #pintando a tela de azul

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):  #funcao para desenhar a cobra
    tela.fill(preto)  #toda vez que o desenha_cobra rodar ele vai "limpar a tela" preenchendo de azul
    for unidade in lista_cobra:
        pygame.draw.rect(tela,laranja,[unidade[0],unidade[1],d,d])  #desenha um retangulo para nós

def mover_cobra(dx,dy,lista_cobra):  #funcao para movimentar a cobra
    for event in pygame.event.get():  #esse ciclo serve para saber a direcao das teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0

            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra

def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]  #nos dar a coordenadas da cabeça da cobra

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:  #se o X da cabeça é igual ao X da comida e o Y da cabeca é igual ao Y da comida
        lista_cobra.append([x_novo, y_novo])  #nesse caso a cobra aumenta um quadrado a frente
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20

    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])

    return x_comida,y_comida,lista_cobra

def verifica_parede(lista_cobra):  #essa funcao nao precisa de retorno porque ela so verifica se estou nos limites da tela
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):  #se meu X ou Y ultrapassar esse limite o jogo fecha
        raise Exception

def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
         raise Exception

def atualizar_pontos(lista_cobra):  #usando funcoes do pygame para escrever coisas na tela
    pts = str(len(lista_cobra))
    escore = fonte.render("Pontuação: " + pts, True, amarelo)
    tela.blit(escore, [0,0])

while True:
    pygame.display.update()  
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)  #verifica se a cabeca da cobra encontoru comida
    print(lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos((lista_cobra))

    clock.tick(5)  #faz com que o jogo atualize a cada 10s. Isso vai dar a ideia de movimento