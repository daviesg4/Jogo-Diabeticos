import pygame
import random
c = 0
glicose = 120
pygame.init()
#tamanho tela:
comprimento = 800
largura = 600
tela = pygame.display.set_mode((comprimento,largura))
#player
playerImg = pygame.image.load('medidor.png')
playerX = 365
playerY = 330
playerX_change = 0
playerY_change = 0
def player(x,y):
    tela.blit(playerImg, (x, y))
#DOCES E INSULINAS:
pizzaImg = pygame.image.load('001-pizza.png')
insulinaImg = pygame.image.load('002-insulin.png')
doceumImg = pygame.image.load('003-sweets.png')
docedoisImg = pygame.image.load('004-candy.png')
docetresImg = pygame.image.load('005-candy-1.png')
corridaImg = pygame.image.load('006-exercise.png')
bombadeinsuImg = pygame.image.load('insuline (1).png')
starImg = pygame.image.load('001-star.png')
lista = [pizzaImg, insulinaImg, doceumImg, docedoisImg, docetresImg, corridaImg,]
#IMAGEM DE FUNDO
'''fundoIMG = pygame.image.load('fundogamedois.jpg')
fundo = pygame.transform.scale(fundoIMG, (comprimento,largura))
def imagemfundo(x,y):
    tela.blit(fundo, (x,y))'''
#RANDOMS X & Y:
randomum = random.choice(lista)
randomumX = random.randint(64,200)
randomumY = - random.randint(240,500)
randomumY_change = 0
randomdois = random.choice(lista)
randomdoisX = random.randint(200,440)
randomdoisY = - random.randint(240,500)
randomdoisY_change = 0
randomtres = random.choice(lista)
randomtresX = random.randint(440,736)
randomtresY = - random.randint(240,500)
randomtresY_change = 0
bombadeinsuX = 360
bombadeinsuY = 490
star = starImg
starY = 360
starx = 310
stary_change = 0
def starum(x,y):
    tela.blit(star,(x,y))
def docesum(x,y):
    tela.blit(randomum, (x,y))
def docesdois(x,y):
    tela.blit(randomdois,(x,y))
def docestres(x,y):
    tela.blit(randomtres,(x,y))
def bomba_insulina(x,y):
    tela.blit(bombadeinsuImg,(x,y))
def exibirmensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg:.0f}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

#rodando o jogo:
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    nome = pygame.display.set_caption('GLAICO: 0 GAME')
    tela.fill((192,192,192))

    #MOVIMENTAÇAO DO PLAYER(KEYDOWN)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.6
            playerY_change = 0
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.6
            playerY_change = 0


        #if event.key == pygame.K_UP:
            #playerY_change = -0.5
            #playerX_change = 0
        #if event.key == pygame.K_DOWN:
            #playerY_change = 0.5
            #playerX_change = 0


        #desbugando o movimento.
        if event.key == pygame.K_RIGHT:
            rai = 1
        else:
            rai = 0
        if event.key == pygame.K_LEFT:
            lef = 1
        else:
            lef = 0
        if event.key == pygame.K_UP:
            upi = 1
        else:
            upi = 0
        if event.key == pygame.K_DOWN:
            dow = 1
        else:
            dow = 0
    #MOVIMENTAÇAO DO PLAYER(KEYUP)
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and rai == 0 or event.key == pygame.K_RIGHT and lef == 0:
                playerX_change = 0
            if event.key == pygame.K_UP and dow == 0 or event.key == pygame.K_DOWN and upi == 0:
                playerY_change = 0
    #MOVIMENTAÇAO DOS DOCES E INSULINAS:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            randomumY_change = 0.70
            randomdoisY_change = 0.70
            randomtresY_change = 0.70
            stary_change = 0.70
        #-----------------------------------
    if 360 >= randomumY >= 315 and playerX + 64 > randomumX > (playerX - 64):
        randomumY = -200
        p = -35
        randomumY -= p
        if randomumY <= -290:
            randomumY = -190
        #PONTUAÇAOUM:
        if randomum == pizzaImg:
            glicose += 100

        if randomum == insulinaImg:
            glicose -= 75

        if randomum == doceumImg:
            glicose += 75

        if randomum == docedoisImg:
            glicose += 50

        if randomum == docetresImg:
            glicose += 25

        if randomum == corridaImg:
            glicose -= 75

        #RANDOMIZAÇAO NA APARIÇAO DOS DOÇES:
        if c == 6:
            c = 0
        randomum = lista[c]
        if randomum == lista[c]:
            c += 1
        if randomumX == randomumX:
            randomumX += 150
        #-----------------------------------
    if 360 >= randomdoisY >= 315 and playerX + 64 > randomdoisX > (playerX - 64):
        randomdoisY = -220
        p = -40
        randomdoisY -= p
        if randomdoisY == -300:
            randomdoisY = -200
        #PONTUAÇAODOIS:
        if randomdois == pizzaImg:
            glicose += 100

        if randomdois == insulinaImg:
            glicose -= 75

        if randomdois == doceumImg:
            glicose += 75

        if randomdois == docedoisImg:
            glicose += 50

        if randomdois == docetresImg:
            glicose += 25

        if randomdois == corridaImg:
            glicose -= 75

        #RANDOMIZAÇAO NA APARIÇAO DOS DOÇES:
        if c == 6:
            c = 0
        randomdois = lista[c]
        if randomdois == lista[c]:
            c += 1
        if randomdoisX == randomdoisX:
            randomdoisX += 250
        #-------------------------------------
    if 360 >= randomtresY >= 315 and playerX + 64 > randomtresX > (playerX - 64):
        randomtresY = -240
        p = -30
        randomtresY -= p
        if randomtresY > -300:
            randomtresY = -240
        #PONTUAÇAOTRES:
        if randomtres == pizzaImg:
            glicose += 100

        if randomtres == insulinaImg:
            glicose -= 75

        if randomtres == doceumImg:
            glicose += 75

        if randomtres == docedoisImg:
            glicose += 50

        if randomtres == docetresImg:
            glicose += 25

        if randomtres == corridaImg:
            glicose -= 75

        #RANDOMIZAÇAO NA APARIÇAO DOS DOCES:
        if c == 6:
            c = 0
        randomtres = lista[c]
        if randomtres == lista[c]:
            c += 1
        if randomtresX == randomtresX:
            randomtresX += 200
        #-------------------------------------
    #LIMITAÇAO DA BORDA DO JOGO
    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    #RANDOMUM
    if randomumY >= 864 and randomumX >= 550:
        randomumY = -250
        randomumX = 64
        if c == 6:
            c = 0
        randomum = lista[c]
        if randomum == lista[c]:
            c += 1
        if randomumX == randomumX:
            randomumX += 150
    if randomumY >= 864:
        randomumY = -250
        randomumX += 150
        if c == 6:
            c = 0
        randomum = lista[c]
        if randomum == lista[c]:
            c += 1
        if randomumX == randomumX:
            randomumX += 150
    #RANDOMDOIS
    if randomdoisY >= 864 and randomdoisX >= 510:
        randomdoisX = 64
        randomdoisY = -330
        if c == 6:
            c = 0
        randomdois = lista[c]
        if randomdois == lista[c]:
            c += 1
        if randomdoisX == randomdoisX:
            randomdoisX += 250
    if randomdoisY >= 864:
        randomdoisY = -330
        randomdoisX = 200
        if c == 6:
            c = 0
        randomdois = lista[c]
        if randomdois == lista[c]:
            c += 1
        if randomdoisX == randomdoisX:
            randomdoisX += 250
    #RANDOMTRES
    if randomtresY >= 864 and randomtresX >= 510:
        randomtresY = -210
        randomtresX = 200
        if c == 6:
            c = 0
        randomtres = lista[c]
        if randomtres == lista[c]:
            c += 1
        if randomtresX == randomtresX:
            randomtresX += 200
    if randomtresY >= 864:
        randomtresY = -210
        randomtresX = 250
        if c == 6:
            c = 0
        randomtres = lista[c]
        if randomtres == lista[c]:
            c += 1
        if randomtresX == randomtresX:
            randomtresX += 200
    #ESTRELA / STAR
    if starY >= 664:
        starY = -12000
        starx += 230

    if starx >= 746:
        starx = 64 - (starx - 746)

    if (playerX + 64) >= starx >= (playerX - 64) and 360 >= starY >= 315:
        starY = -12000
        starx += 230

    #SISTEMA DE MOSTRAGEM DA GLAICO:
    if glicose != 0:
        glicose_mostragem = exibirmensagem(glicose, 40, (0, 0, 0))
    def glicoseadd():
        tela.blit(glicose_mostragem, (365, 500))
    if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
        glicose -= 0.018
    # CIRCULOS DE COR DA GLICOSE:
    if 150 >= glicose >= 100:
        circuloIMG = pygame.image.load('003-rec-2.png')
    if 75 <= glicose < 100 or glicose >= 150:
        circuloIMG = pygame.image.load('002-rec-1.png')
    if glicose < 75 or glicose >= 180:
        circuloIMG = pygame.image.load('001-rec.png')
    def circuloadd():
        tela.blit(circuloIMG, (263.5, 527))
    #ADICIONANDO AS DEFS AO JOGO:
    #imagemfundo(0, 0)
    glicoseadd()
    circuloadd()
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    docesum(randomumX, randomumY)
    docesdois(randomdoisX, randomdoisY)
    docestres(randomtresX, randomtresY)
    bomba_insulina(bombadeinsuX, bombadeinsuY)
    starum(starx, starY)
    randomumY += randomumY_change
    randomdoisY += randomdoisY_change
    randomtresY += randomtresY_change
    starY += stary_change
    if glicose <= 0:
        print('voce perdeu')
        break

    pygame.display.update()