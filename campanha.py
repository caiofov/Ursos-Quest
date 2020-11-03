import pygame
pygame.init()

#CONFIGURAÇÕES INICIAIS --------------------------------------------
music= pygame.mixer.music.load('arquivos/musicas/gravity_falls.mp3')
pygame.mixer.music.play(-1)

win_jogo= pygame.display.set_mode((1080,720))
pygame.display.set_caption("Campanha - Singleplayer")

    
clock=pygame.time.Clock()

#VARIAVEIS INICIAIS DOS PERSONAGENS---------------------------------
walkDir = [pygame.image.load('arquivos/sprites/urso/R1.png'), pygame.image.load('arquivos/sprites/urso/R2.png'), pygame.image.load('arquivos/sprites/urso/R3.png')]
walkEsq = [pygame.image.load('arquivos/sprites/urso/L1.png'), pygame.image.load('arquivos/sprites/urso/L2.png'), pygame.image.load('arquivos/sprites/urso/L3.png')]
stand = pygame.image.load('arquivos/sprites/urso/stand.png')
balaUrso= pygame.image.load('arquivos/sprites/urso/bala.png')

bulletSound= pygame.mixer.Sound('arquivos/musicas/bullet.wav')
hitSound= pygame.mixer.Sound('arquivos/musicas/hit.wav')
correctSound=pygame.mixer.Sound('arquivos/musicas/correct.wav')
curaSound=pygame.mixer.Sound('arquivos/musicas/vida.wav')
gameOverSound=pygame.mixer.Sound('arquivos/musicas/gameover.wav')


font= pygame.font.SysFont('comicsans',50,True)
dadosUrso= font.render('Urso',1,(255,255,255))

font2=pygame.font.SysFont('comicsans',50)
textPausar=font2.render('[P - Pausar]', 1, (255,255,255))

#CLASSES E FUNÇÕES ----------------------------------------
def vitoria():
    global run
    global pausar
    global fim
    fontGO=pygame.font.SysFont('comicsans',250,True)
    fontg2=pygame.font.SysFont('comicsans',30)
    textGO=fontGO.render('Vitória!',1,(128,0,0))
    textg2=fontg2.render('Pressione [backspace] para recomeçar ou [esc] para voltar ao menu principal', 1, (128,0,0))
    win_jogo.blit(textg2, (120, 600)) 
    win_jogo.blit(textGO, (10, 300))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
            pausar=False
            fim=False
    pygame.display.update()

def gameOver():
    global run
    global pausar
    global fim
    fontGO=pygame.font.SysFont('comicsans',250,True)
    fontg2=pygame.font.SysFont('comicsans',30)
    textGO=fontGO.render('GameOver',1,(128,0,0))
    textg2=fontg2.render('Pressione [backspace] para recomeçar ou [esc] para voltar ao menu principal', 1, (128,0,0))
    win_jogo.blit(textg2, (120, 600)) 
    win_jogo.blit(textGO, (10, 300))
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False
                pausar=False
                fim=False
            
    pygame.display.update()
    
    
class button():
    def __init__(self,x,y,width,height,linha):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.linha=linha
        self.color=(255,255,255)
    def draw(self,win_menu): #outline
        pygame.draw.rect(win_menu,self.color,(self.x-2,self.y-2,self.width+4,self.height+4), self.linha)
    def sobre(self,pos):
        if pos[0]> self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1] < self.y + self.height:
                return True
        return False

def pause():
        global pausar
        global pCount
        global run
        fontP=pygame.font.SysFont('comicsans',300,True)
        textP=fontP.render('Pausado',1,(128,0,0))
        
        win_jogo.blit(textP, (10, 200))
        
        
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
        self.rect=pygame.Rect(self.x, self.y,self.larg, self.alt)

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
            self.dano+=3
        
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

        
class cenario(object):
        def __init__(self, x,img):
                self.x=x
                self.img=img
        def draw(self,win):
                win.blit(self.img, (self.x,0))
                



def janela():
    for cenario in cenarios:
            cenario.draw(win_jogo)
    for botao in botoes:
            botao.draw(win_jogo)
    win_jogo.blit(textPausar,(470, 10))
    urso.draw(win_jogo)
    urso.vida(10,50)
    win_jogo.blit(dadosUrso, (10,10))
    if cura_visivel:
            win_jogo.blit(curaimg,(550,300))
    for bala in LT_urso:
        bala.draw(win_jogo)
    
    #pygame.draw.rect(win_jogo,(0,150,0),(0,620, 1080,100))
    pygame.display.update()


#MAIS VARIAVEIS--------------------------------

uva1=cenario(0, pygame.image.load('arquivos/campanha/1_uva.png'))
uva2=cenario(1080, pygame.image.load('arquivos/campanha/2_uva.png'))

urso= player (0, 600, 100, 100,walkEsq,walkDir)

Linha_inicio= 3
Linha_final= 8
B_uva=button(uva2.x+90,105, 87, 40, Linha_inicio)
B_ferm=button(uva2.x+335, 105, 183, 50, Linha_inicio)
B_sal=button(uva2.x+670,105,292,45,Linha_inicio)
B_farinha=button(uva2.x+140,217,302,46,Linha_inicio)
B_manteiga=button(uva2.x+580,220,185,40,Linha_inicio)
B_leite=button(uva2.x+905,220,88,44,Linha_inicio)
B_acucar=button(uva2.x+70,350,135,40,Linha_inicio)
B_choco=button(uva2.x+388,350,190,40,Linha_inicio)
B_limao=button(uva2.x+727,348,116,43,Linha_inicio)
B_chant=button(uva2.x+125,465,168,45,Linha_inicio)
B_leitecon=button(uva2.x+730,475,330,40,Linha_inicio)
B_creme=button(uva2.x+365,540,270,40,Linha_inicio)

botoes=[B_uva,B_ferm,B_sal,B_farinha,B_manteiga,B_leite,B_acucar,B_choco,B_limao,B_chant,B_leitecon,B_creme]
botoes_certo=[B_uva,B_manteiga,B_choco,B_leitecon,B_creme]
botoes_errado= [item for item in botoes if item not in botoes_certo]

acertos=[]
erros=[]
certos=0

curaimg= pygame.image.load('arquivos/health.png')
curarect= pygame.Rect(550,520, curaimg.get_width(), curaimg.get_height())
cura_visivel= False
pode_visivel=True

cenarios=[uva1,uva2]
LT_urso=[]
tiroLoopUrso= 0
maxTiro=20

run=True
pausar = False
sair= False
pCount=0
fim=False
fimSound=True
fimvitoria=False



# JOGO ======================================================================
#============================================================================
#============================================================================
while run:
    clock.tick(15)
    K=pygame.key.get_pressed()
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        if event.type==pygame.QUIT:
            run= False
            pausar= False

        if event.type==pygame.MOUSEBUTTONDOWN:
            for be in botoes_errado:
                    if be.sobre(pos) and not be in erros:
                            be.color=(255,0,0)
                            be.linha=Linha_final
                            urso.hit()
                            erros.append(be)
            for bc in botoes_certo:
                    if bc.sobre(pos) and not bc in acertos:
                            bc.color=(0,128,0)
                            bc.linha=Linha_final
                            correctSound.play()
                            acertos.append(bc)
        
        
        if event.type==pygame.MOUSEMOTION:
            for botao in botoes:
                    if botao.sobre(pos):
                            botao.linha=Linha_final
                    else:
                            botao.linha=Linha_inicio

    if urso.dano>10:
        fim=True

    while fim==True:
        if fimSound:
            gameOverSound.play()
            fimSound=False
            
        gameOver()
        pygame.mixer.music.stop()
        K=pygame.key.get_pressed()
        if K[pygame.K_BACKSPACE]:
            pygame.mixer.music.play(-1)
            acertos=[]
            erros=[]
            certos=0
            urso.dano=0
            urso.x = 0
            urso.y = 600
            fimSound = True
            gameOverSound.stop()
            for botao in botoes:
                botao.color=(255,255,255)
            fim = False
            run = True
        if K[pygame.K_ESCAPE]:
            run=False
            import ursosquest
        
        
    if len(acertos)==len(botoes_certo):
        if pode_visivel:
            cura_visivel=True
            pode_visivel=False
    if cura_visivel:
        if urso.hitbox[1]<curarect.y + curarect.height and urso.hitbox[1] + urso.hitbox[3] > curarect.y:
            if urso.hitbox[0]+urso.hitbox[2] > curarect.x and urso.hitbox[0] < curarect.x+curarect.width:
                urso.dano=0
                curaSound.play()
                cura_visivel=False
                fimvitoria=True
                
    while fimvitoria and run:
        vitoria()
        K=pygame.key.get_pressed()
        if K[pygame.K_BACKSPACE]:
            pygame.mixer.music.play(-1)
            acertos=[]
            erros=[]
            certos=0
            urso.dano=0
            urso.x = 0
            urso.y = 600
            fimSound = True
            gameOverSound.stop()
            for botao in botoes:
                botao.color=(255,255,255)
            fim = False
            fimvitoria=False
            run = True
        if K[pygame.K_ESCAPE]:
            run=False
            import ursosquest   
    

#botoes posiçoes ----
    B_uva.x = uva2.x+ 90
    B_ferm.x=uva2.x+335
    B_sal.x=uva2.x+670
    B_farinha.x=uva2.x+140
    B_manteiga.x=uva2.x+580
    B_leite.x=uva2.x+905
    B_acucar.x=uva2.x+70
    B_choco.x=uva2.x+388
    B_limao.x=uva2.x+727
    B_chant.x=uva2.x+125
    B_leitecon.x=uva2.x+730
    B_creme.x=uva2.x+365

#botoes mouse
    
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
#tiro
    for bala in LT_urso:
        if bala.x<1080 and bala.x>0:
            bala.x+=bala.vel
        else:
            LT_urso.pop(LT_urso.index(bala))


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
        if urso.x<540 - urso.larg or cenarios[-1].x==0:
            urso.x = urso.x + urso.vel
        if cenarios[-1].x>0:
                for cenario in cenarios:
                        cenario.x-=urso.vel
        urso.esq= False
        urso.dir= True
        urso.pe= False
    
    elif K[pygame.K_a] and urso.x>0:
        if urso.x>100 or cenarios[0].x==0:
            urso.x = urso.x - urso.vel
        if cenarios[0].x<0:
                for cenario in cenarios:
                        cenario.x+=urso.vel
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
            urso.y -=((urso.jumpCount ** 2)* 3 * neg)
            urso.jumpCount -= 1
        else:
            urso.isJump = False
            urso.jumpCount = 7
    janela()


pygame.quit()

            
