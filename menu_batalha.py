import pygame
pygame.init()
win_menu=pygame.display.set_mode((600,600))
pygame.display.set_caption("Menu - Batalha")

class button():
    def __init__(self,x,y,width,height,linha):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.linha=linha
    def draw(self,win_menu): #outline
        pygame.draw.rect(win_menu,(255,255,255),(self.x-2,self.y-2,self.width+4,self.height+4), self.linha)
        pygame.display.update()
    def sobre(self,pos):
        if pos[0]> self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1] < self.y + self.height:
                return True
        return False

def advers():
    win_menu.blit(pygame.image.load('arquivos/menus/menu_adversario.png'),(0,0))
    B_voltar.draw(win_menu)
    B_joao.draw(win_menu)
    B_gengar.draw(win_menu)
    pygame.display.update()
    
def cenario():
    win_menu.blit(pygame.image.load('arquivos/menus/menu_cenario.png'),(0,0))
    B_voltar.draw(win_menu)
    B_Csitio.draw(win_menu)
    pygame.display.update()

linhaIni=3
linhaFim=7
B_Csitio=button(10,160, 260, 230,linhaIni)
B_joao=button(15,260,140,190,linhaIni)
B_voltar=button(10,550,330,40,linhaIni)
B_gengar= button(170,260,150,200,linhaIni)

menu=True
menu_cenario=False
menu_advers=True

while menu==True:
    pygame.time.delay(100)
    while menu_advers==True and menu==True:
        advers()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                menu=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    import ursosquest
                    menu=False
                if B_joao.sobre(pos):
                    menu_advers=False
                    menu_cenario=True
                    adversEsq=[pygame.image.load('arquivos/sprites/joao/JL1.png'),pygame.image.load('arquivos/sprites/joao/JL2.png'),pygame.image.load('arquivos/sprites/joao/JL3.png'),pygame.image.load('arquivos/sprites/joao/JL4.png')]
                    adversDir=[pygame.image.load('arquivos/sprites/joao/JR1.png'),pygame.image.load('arquivos/sprites/joao/JR2.png'),pygame.image.load('arquivos/sprites/joao/JR3.png'),pygame.image.load('arquivos/sprites/joao/JR4.png')]
                    adversStand=pygame.image.load('arquivos/sprites/joao/Jstand.png')
                    balaAdvers = pygame.image.load('arquivos/sprites/joao/Jbala.png')
                    nomeAdvers = "João"
                    adversLarg=50
                    adversAlt=100
                if B_gengar.sobre(pos):
                    menu_advers=False
                    menu_cenario=True
                    adversEsq=[pygame.image.load('arquivos/sprites/gengar/GL1.png'),pygame.image.load('arquivos/sprites/gengar/GL2.png'),pygame.image.load('arquivos/sprites/gengar/GL3.png')]
                    adversDir=[pygame.image.load('arquivos/sprites/gengar/GR1.png'),pygame.image.load('arquivos/sprites/gengar/GR2.png'),pygame.image.load('arquivos/sprites/gengar/GR3.png')]
                    adversStand=pygame.image.load('arquivos/sprites/gengar/Gstand.png')
                    balaAdvers = pygame.image.load('arquivos/sprites/gengar/Gbala.png')
                    nomeAdvers = "Gengar"
                    adversLarg=80
                    adversAlt=100
                    
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                else:
                    B_voltar.linha=linhaIni
                if B_joao.sobre(pos):
                    B_joao.linha=linhaFim
                else:
                    B_joao.linha=linhaIni
                if B_gengar.sobre(pos):
                    B_gengar.linha=linhaFim
                else:
                    B_gengar.linha=linhaIni
                pygame.display.update()
                
    while menu_cenario==True and menu==True:
        cenario()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                menu=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if B_voltar.sobre(pos):
                    import ursosquest
                    menu=False
                    menu_cenario=False
                if B_Csitio.sobre(pos):
                    cen=pygame.image.load('arquivos/cenarios/cenario_sitio.png')
                    menu_cenario=False
                    menu=False
            if event.type==pygame.MOUSEMOTION:
                if B_voltar.sobre(pos):
                    B_voltar.linha=linhaFim
                else:
                    B_voltar.linha=linhaIni
                if B_Csitio.sobre(pos):
                    B_Csitio.linha=linhaFim
                else:
                    B_Csitio.liha=linhaIni
                pygame.display.update()


pygame.quit()
