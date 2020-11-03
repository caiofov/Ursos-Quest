import pygame
from menu_batalha import adversEsq, adversDir, adversStand, cen, balaAdvers, nomeAdvers, adversAlt, adversLarg

pygame.init()

#CONFIGURAÇÕES INICIAIS --------------------------------------------
music= pygame.mixer.music.load('arquivos/musicas/gravity_falls.mp3')
pygame.mixer.music.play(-1)

win_jogo= pygame.display.set_mode((1080,720))
pygame.display.set_caption("Batalha - Multiplayer")

    
clock=pygame.time.Clock()

#VARIAVEIS INICIAIS DOS PERSONAGENS---------------------------------
walkDir = [pygame.image.load('arquivos/sprites/urso/R1.png'), pygame.image.load('arquivos/sprites/urso/R2.png'), pygame.image.load('arquivos/sprites/urso/R3.png')]
walkEsq = [pygame.image.load('arquivos/sprites/urso/L1.png'), pygame.image.load('arquivos/sprites/urso/L2.png'), pygame.image.load('arquivos/sprites/urso/L3.png')]
stand = pygame.image.load('arquivos/sprites/urso/stand.png')
balaUrso= pygame.image.load('arquivos/sprites/urso/bala.png')
bulletSound= pygame.mixer.Sound('arquivos/musicas/bullet.wav')
hitSound= pygame.mixer.Sound('arquivos/musicas/hit.wav')
font= pygame.font.SysFont('comicsans',50,True)
dadosUrso= font.render('Urso',1,(255,255,255))
dadosAdvers=font.render(str(nomeAdvers), 1, (255,255,255))

font2=pygame.font.SysFont('comicsans',50)
textPausar=font2.render('[P - Pausar]', 1, (255,255,255))

#CLASSES E FUNÇÕES ----------------------------------------
def pause():
        global pausar
        global pCount
        fontP=pygame.font.SysFont('comicsans',300,True)
        textP=fontP.render('Pausado',1,(255,255,255))
        
        win_jogo.blit(textP, (10, 200))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False
                pausar=False
        if pCount==10:
            pCount=0
        if pCount>0 and pCount<10:
            pCount+=1
        T=pygame.key.get_pressed()
        if T[pygame.K_p] and pCount==0:
            pausar = False
            pCount=1
        
def gameOver():
    global vitUrso, vitEmpate, vitAdvers
    pygame.draw.rect(win_jogo,(165,240,255),(280,140,585,310))
    fontGo=pygame.font.SysFont('comicsans',100,True)
    textGo=fontGo.render('Game Over',1,(255,255,255))
    win_jogo.blit(textGo, (350, 160))
    
    fontGo2=pygame.font.SysFont('comicsans',50, True)
    fontGo3=pygame.font.SysFont('comicsans',30)
    if vitEmpate:
        textGo2=fontGo2.render('Empate!',1,(255,255,255))
        win_jogo.blit(textGo2, (340, 330))
    elif vitUrso:
        textGo2=fontGo2.render('Vitória! Urso ganhou!',1,(255,255,255))
        win_jogo.blit(textGo2, (340, 330))
    elif vitAdvers:
        textGo2=fontGo2.render('Vitória! '+str(nomeAdvers)+' ganhou!',1,(255,255,255))
        win_jogo.blit(textGo2, (340, 330))
    textEsc= fontGo3.render('(Pressione [Esc] para voltar para o menu principal)', 1, (255,255,255))
    win_jogo.blit(textEsc, (320,390))
    
    pygame.display.update()
    T=pygame.key.get_pressed()
    if T[pygame.K_ESCAPE]:
        run=False
        pause=False
        import ursosquest

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
            pausar=False
            fim=False

        
class player(object):
    def __init__(self, x, y, larg, alt, LE, LD):
        self.x=x
        self.y=y
        self.larg=larg
        self.alt=alt
        self.vel=30
        self.isJump= False
        self.jumpCount= 7
        self.esq=False
        self.dir= False
        self.walkCount=0
        self.LE=LE
        self.LD=LD
        self.pe=True
        self.dano = 0
        self.hitbox=(self.x, self.y, self.x + self.larg, self.y + self.alt)

    def draw(self,win_jogo):
        if self.walkCount + 1>= 3 * len(self.LE):
            self.walkCount=0
            
        if not self.pe:
            if self.esq:
                win_jogo.blit(self.LE[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.dir:
                win_jogo.blit(self.LD[self.walkCount//3], (self.x, self.y))
                self.walkCount +=1
        else:
            if self.dir:
                win_jogo.blit(self.LD[0], (self.x, self.y))
            else:
                win_jogo.blit(self.LE[0], (self.x,self.y))
                
        self.hitbox=(self.x, self.y, self.larg, self.alt)   
        #pygame.draw.rect(win_jogo,(255,0,0), self.hitbox, 2)

    def hit(self):
        hitSound.play()
        if self.dano<10:
            self.dano+=1
        print(self.dano)
    def vida(self, x, y):
        pygame.draw.rect(win_jogo, (255,0,0), (x, y, 250, 30))
        pygame.draw.rect(win_jogo, (0,200,0), (x, y, 250 - self.dano * 25, 30))
        
    
class projetil(object):
    def __init__(self, x, y, larg, alt, lado, bala):
        self.x=x
        self.y=y
        self.larg=larg
        self.alt=alt
        self.lado=lado
        self.vel=50*lado
        self.bala=bala
    def draw(self, win_jogo):
        win_jogo.blit(self.bala, (self.x, self.y))
        
def janela():
    win_jogo.blit(cen, (0,0))
    win_jogo.blit(textPausar,(470, 10))
    urso.draw(win_jogo)
    urso.vida(10,50)
    win_jogo.blit(dadosUrso, (10,10))
    for bala in LT_urso:
        bala.draw(win_jogo)
        
    advers.draw(win_jogo)
    advers.vida(820,50)
    win_jogo.blit(dadosAdvers,((1070 - dadosAdvers.get_width()), 10))
    for bala in LT_advers:
        bala.draw(win_jogo)
    
    pygame.draw.rect(win_jogo,(0,150,0),(0,620, 1080,100))
    pygame.display.update()


#MAIS VARIAVEIS--------------------------------

urso= player (0, 520, 100, 100,walkEsq,walkDir)
advers= player((1080 - adversLarg), 520, adversLarg, adversAlt, adversEsq, adversDir)

LT_urso=[]
LT_advers=[]
tiroLoopUrso= 0
tiroLoopAdvers= 0
maxTiro=20

run=True
pausar = False
sair= False
pCount=0
fim=False
vitUrso= False
vitAdvers=False
vitEmpate=False

#--#3----#--##----##-----#------##---JOGO-----#---#-----#-----#------#---##-----------

while run==True:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
            pausar= False
    K=pygame.key.get_pressed()

    #pause - - - -
    if pCount==10:
        pCount==0
    elif pCount>0 and pCount<10:
        pCount+=1

    while pausar==True and run==True:
        pause()
            
    if K[pygame.K_p] and pCount==0:
        pausar=True
        pCount=1

    #game over
    if advers.dano==10 or urso.dano==10:
        fim=True
    if advers.dano==10 and urso.dano==10:
        vitEmpate=True
        vitAdvers=False
        vitUrso=False
        
    elif advers.dano==10:
        vitUrso= True
        vitAdvers=False
        vitEmpate=False
    elif urso.dano==10:
        vitUrso= False
        vitAdvers=True
        vitEmpate=False

    while fim:
        gameOver()

        
    #colisões - - - - -  - - -
    for bala in LT_urso:
        if bala.x+bala.larg>advers.hitbox[0] and bala.x < advers.hitbox[0] + advers.hitbox[2]:
            if bala.y+bala.alt>advers.hitbox[1] and bala.y < advers.hitbox[1] + advers.hitbox[3]:
                LT_urso.pop(LT_urso.index(bala))
                advers.hit()
        if bala.x<1080 and bala.x>0:
            bala.x+=bala.vel
        else:
            LT_urso.pop(LT_urso.index(bala))
        for bAd in LT_advers:
            if bala.x+bala.larg>bAd.x and bala.x< bAd.x +bAd.larg:
                if bala.y+bala.alt> bAd.y and bala.y<bAd.y + bAd.alt:
                    LT_urso.pop(LT_urso.index(bala))
                    LT_advers.pop(LT_advers.index(bAd))
            
    for bAd in LT_advers:
        if bAd.x+bAd.larg>urso.hitbox[0] and bAd.x < urso.hitbox[0] + urso.hitbox[2]:
            if bAd.y+bAd.alt>urso.hitbox[1] and bAd.y < urso.hitbox[1] + urso.hitbox[3]:
                LT_advers.pop(LT_advers.index(bAd))
                urso.hit()
        if bAd.x<1080 and bAd.x>0:
            bAd.x+=bAd.vel
        else:
            LT_advers.pop(LT_advers.index(bAd))

    #movimentos URSO - - - - -
    
    if tiroLoopUrso>0:
        tiroLoopUrso +=1
    if tiroLoopUrso>3:
        tiroLoopUrso=0
        
    if K[pygame.K_SPACE] and tiroLoopUrso==0:
        bulletSound.play()
        if urso.esq:
            lado=-1
        else:
            lado=1
        if len(LT_urso)<maxTiro:
            LT_urso.append(projetil((urso.x + urso.larg//2), (urso.y + urso.alt//2), 25, 25, lado, balaUrso))
        tiroLoopUrso=1
                          
    if K[pygame.K_d] and urso.x < 1080 - urso.larg:
        urso.x = urso.x + urso.vel
        urso.esq= False
        urso.dir= True
        urso.pe= False
    elif K[pygame.K_a] and urso.x>0:
        urso.x = urso.x - urso.vel
        urso.esq= True
        urso.dir= False
        urso.pe= False
    else:
        urso.pe= True
        urso.walkCount=0
        
    if not(urso.isJump):
        if K[pygame.K_w]:
            urso.isJump = True
            urso.walkCount=0
            urso.pe=False

    else:
        if urso.jumpCount >=-7:
            neg = 1
            if urso.jumpCount < 0:
                neg = -1
            urso.y = urso.y - (urso.jumpCount ** 2)* 3 * neg
            urso.jumpCount = urso.jumpCount - 1
        else:
            urso.isJump = False
            urso.jumpCount = 7

    #movimentos ADVERSÁRIO - - - - - - 

    if tiroLoopAdvers>0:
        tiroLoopAdvers+=1
    if tiroLoopAdvers>3:
        tiroLoopAdvers=0
        
    if K[pygame.K_RSHIFT] and tiroLoopAdvers==0:
        bulletSound.play()
        if advers.esq:
            lado=-1
        else:
            lado=1
        if len(LT_advers)<maxTiro:
            LT_advers.append(projetil((advers.x+advers.larg//2), (advers.y + advers.alt //2), 25, 25, lado, balaAdvers))
        tiroLoopAdvers=1
        
    if K[pygame.K_RIGHT] and advers.x < 1080 - advers.larg:
        advers.x = advers.x + advers.vel
        advers.esq= False
        advers.dir= True
        advers.pe=False
    elif K[pygame.K_LEFT] and advers.x>0:
        advers.x = advers.x - advers.vel
        advers.esq= True
        advers.dir= False
        advers.pe=False
    else:
        advers.pe=True
        advers.walkCount=0
        
    if not(advers.isJump):
        if K[pygame.K_UP]:
            advers.isJump = True
            advers.walkCount=0
            advers.pe=False

    else:
        if advers.jumpCount >=-7:
            neg = 1
            if advers.jumpCount < 0:
                neg = -1
            advers.y = advers.y - ((advers.jumpCount**2) * 3 * neg)
            advers.jumpCount = advers.jumpCount - 1
        else:
            advers.isJump = False
            advers.jumpCount = 7
    janela()

    
        
    


pygame.quit()
