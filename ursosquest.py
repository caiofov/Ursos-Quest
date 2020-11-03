import pygame
pygame.init()


win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Urso's Quest")
music= pygame.mixer.music.load('arquivos/musicas/indiana_jones.mp3')
mousesong= pygame.mixer.Sound('arquivos/musicas/mouse.wav')
pygame.mixer.music.play(-1, 6.0)

class button():
    def __init__(self,x,y,width,height,linha):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.linha=linha
    def draw(self,win): #outline
        pygame.draw.rect(win,(255,255,255),(self.x-2,self.y-2,self.width+4,self.height+4), self.linha)
        pygame.display.update()
    def sobre(self,pos):
        if pos[0]> self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1] < self.y + self.height:
                return True
        return False


def inicio():
    win.blit(pygame.image.load('arquivos/menus/menu.png'),(0,0))
    B_jogar.draw(win)
    B_comojogar.draw(win)
    B_intro.draw(win)
    pygame.display.update()
    
def jogar():
    win.blit(pygame.image.load('arquivos/menus/menu_jogarmodo.png'),(0,0))
    B_batalha.draw(win)
    B_voltar.draw(win)
    B_campanha.draw(win)
    pygame.display.update()

def desafios():
    win.blit(pygame.image.load('arquivos/menus/desafios.png'),(0,0))
    B_ingred.draw(win)
    B_voltar.draw(win)
    pygame.display.update()

def intro1():
    win.blit(pygame.image.load('arquivos/menus/intro1.png'),(0,0))
    B_voltar.draw(win)
    B_proxIntro.draw(win)
    pygame.display.update()
    
def intro2():
    win.blit(pygame.image.load('arquivos/menus/intro2.png'),(0,0))
    B_voltar.draw(win)
    B_anteriorIntro.draw(win)
    pygame.display.update()

def comoJogar1():
    win.blit(pygame.image.load('arquivos/menus/como_jogar1.png'),(0,0))
    B_proxComo.draw(win)
    B_voltar.draw(win)
    pygame.display.update()

def comoJogar2():
    win.blit(pygame.image.load('arquivos/menus/como_jogar2.png'),(0,0))
    B_anteriorComo.draw(win)
    B_voltar.draw(win)
    pygame.display.update()

linhaIni=3
linhaFim=7

B_voltar=button(10,550,330,40,linhaIni)

B_intro=button(30,165,230,40, linhaIni)
B_jogar=button(30, 320, 130, 45,linhaIni)
B_comojogar=button(20,470,235,45,linhaIni)

B_batalha=button(400,270,170,55,linhaIni)
B_campanha=button(20,275,240,50,linhaIni)
B_ingred=button(20,187,157,142,linhaIni)

B_proxIntro=button(445,525,122,30,linhaIni)
B_anteriorIntro=button(15,510,125,30,linhaIni)

B_proxComo=button(455,562,122,30,linhaIni)
B_anteriorComo=button(15,510,125,30,linhaIni)

menu_Jogar=False
menu_cenario=False
menu_desafios=False
menu_advers=False
game_batalha=False
run=True

menu_intro1=False
menu_intro2=False

menu_como1=False
menu_como2=False

while run==True:
    inicio()
    pygame.time.delay(100)
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()

        if event.type==pygame.QUIT:
            run=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if B_intro.sobre(pos):
                menu_intro1=True
            if B_jogar.sobre(pos):
                menu_Jogar=True
            if B_comojogar.sobre(pos):
                menu_como1=True
            
                
        if event.type==pygame.MOUSEMOTION:
            if B_intro.sobre(pos):
                B_intro.linha=linhaFim
                mousesong.play()
            else:
                B_intro.linha=linhaIni
            if B_jogar.sobre(pos):
                B_jogar.linha=linhaFim
                mousesong.play()
            else:
                B_jogar.linha=linhaIni
            if B_comojogar.sobre(pos):
                B_comojogar.linha=linhaFim
                mousesong.play()
            else:
                B_comojogar.linha=linhaIni
            pygame.display.update()
                
                
    while menu_intro1 and run:
        intro1()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    menu_intro1=False
                if B_proxIntro.sobre(pos):
                    menu_intro2=True
                    menu_intro1=False
                    
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                    mousesong.play()
                else:
                    B_voltar.linha=linhaIni
                if B_proxIntro.sobre(pos):
                    B_proxIntro.linha=linhaFim
                    mousesong.play()
                else:
                    B_proxIntro.linha=linhaIni
                pygame.display.update
                
    while menu_intro2 and run:
        intro2()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    menu_intro2=False
                if B_anteriorIntro.sobre(pos):
                    menu_intro2=False
                    menu_intro1=True
                    
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                    mousesong.play()
                else:
                    B_voltar.linha=linhaIni
                if B_anteriorIntro.sobre(pos):
                    B_anteriorIntro.linha=linhaFim
                    mousesong.play()
                else:
                    B_anteriorIntro.linha=linhaIni
                pygame.display.update
                
    while menu_Jogar==True and run==True:
        jogar()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    menu_Jogar=False
                if B_batalha.sobre(pos):
                    menu_Jogar=False
                    import batalha
                if B_campanha.sobre(pos):
                    menu_Jogar=False
                    menu_desafios=True

            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                    mousesong.play()
                else:
                    B_voltar.linha=linhaIni
                if B_batalha.sobre(pos):
                    B_batalha.linha=linhaFim
                    mousesong.play()
                else:
                    B_batalha.linha=linhaIni
                if B_campanha.sobre(pos):
                    B_campanha.linha=linhaFim
                    mousesong.play()
                else:
                    B_campanha.linha=linhaIni
                pygame.display.update

    
    while menu_desafios and run:
        desafios()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    menu_desafios=False
                if B_ingred.sobre(pos):
                    menu_desafios=False
                    run=False
                    import campanha
                    
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                    mousesong.play()
                else:
                    B_voltar.linha=linhaIni
                if B_ingred.sobre(pos):
                    B_ingred.linha=linhaFim
                    mousesong.play()
                else:
                    B_ingred.linha=linhaIni
                pygame.display.update

    while menu_como1 and run:
        comoJogar1()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    menu_como1=False
                if B_proxComo.sobre(pos):
                    menu_como2=True
                    menu_como1=False
                    
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                    mousesong.play()
                else:
                    B_voltar.linha=linhaIni
                if B_proxComo.sobre(pos):
                    B_proxComo.linha=linhaFim
                    mousesong.play()
                else:
                    B_proxComo.linha=linhaIni
                pygame.display.update

    while menu_como2 and run:
        comoJogar2()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    menu_como2=False
                if B_anteriorComo.sobre(pos):
                    menu_como2=False
                    menu_como1=True
                    
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                    mousesong.play()
                else:
                    B_voltar.linha=linhaIni
                if B_anteriorComo.sobre(pos):
                    B_anteriorComo.linha=linhaFim
                    mousesong.play()
                else:
                    B_anteriorComo.linha=linhaIni
                pygame.display.update
pygame.quit()



