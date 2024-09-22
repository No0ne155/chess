import pygame
import math
pygame.init()

# Pieces:
# 0 = pawn
# 1 = bishop
# 2 = horse
# 3 = rook
# 4 = queen
# 5 = king

white = (255,255,255)
lgray = (190,190,190)
dgray = (50,50,50)
black = (0,0,0)
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 600))
turn = True

board = [
    []
]

# Bilder laden 
bb = pygame.image.load('C:/code/chess/img/bb.png')
bk = pygame.image.load('C:/code/chess/img/bk.png')
bn = pygame.image.load('C:/code/chess/img/bn.png')
bp = pygame.image.load('C:/code/chess/img/bp.png')
bq = pygame.image.load('C:/code/chess/img/bq.png')
br = pygame.image.load('C:/code/chess/img/br.png')

wb = pygame.image.load('C:/code/chess/img/wb.png')
wk = pygame.image.load('C:/code/chess/img/wk.png')
wn = pygame.image.load('C:/code/chess/img/wn.png')
wp = pygame.image.load('C:/code/chess/img/wp.png')
wq = pygame.image.load('C:/code/chess/img/wq.png')
wr = pygame.image.load('C:/code/chess/img/wr.png')

pygame.display.set_caption('Chess')

# Funktion um das Brett anzuzeigen
def drawboard():
    for i in range(1,8,2):
        for j in range(0,7,2):
            pygame.draw.rect(window, dgray, ((i*60),(j*60),60,60))
    for i in range(0,7,2):
        for j in range(1,8,2):
            pygame.draw.rect(window, dgray, ((i*60),(j*60),60,60))
    for i in range(0,7,2):
        for j in range(0,7,2):
            pygame.draw.rect(window, lgray, ((i*60),(j*60),60,60))
    for i in range(1,8,2):
        for j in range(1,8,2):
            pygame.draw.rect(window, lgray, ((i*60),(j*60),60,60))
    pygame.draw.rect(window, black, (0,0,480 ,480),2)


class Pawn:
    def __init__(self, coords, team, img ) -> None:
        self.coords = coords
        self.team = team
        self.img = img
    
    def draw(self):
        window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
    
wpawnA = Pawn((0,6), 1, wp)
wpawnB = Pawn((1,6), 1, wp)
wpawnC = Pawn((2,6), 1, wp)
wpawnD = Pawn((3,6), 1, wp)
wpawnE = Pawn((4,6), 1, wp)
wpawnF = Pawn((5,6), 1, wp)
wpawnG = Pawn((6,6), 1, wp)
wpawnH = Pawn((7,6), 1, wp)


bpawnA = Pawn((0, 1), 1, bp)
bpawnB = Pawn((1, 1), 1, bp)
bpawnC = Pawn((2, 1), 1, bp)
bpawnD = Pawn((3, 1), 1, bp)
bpawnE = Pawn((4, 1), 1, bp)
bpawnF = Pawn((5, 1), 1, bp)
bpawnG = Pawn((6, 1), 1, bp)
bpawnH = Pawn((7, 1), 1, bp)


def drawall():
 wpawnA.draw()
 wpawnB.draw()
 wpawnC.draw()
 wpawnD.draw()
 wpawnE.draw()
 wpawnF.draw()
 wpawnG.draw()
 wpawnH.draw()

 bpawnA.draw()
 bpawnB.draw()
 bpawnC.draw()
 bpawnD.draw()
 bpawnE.draw()
 bpawnF.draw()
 bpawnG.draw()
 bpawnH.draw()




# Main Loop
running = True
while running == True:
    clock.tick(60)
    window.fill(white)

    drawboard()
    drawall()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickpos = event.pos
            #handle_mouse_click(clickpos)

    


    pygame.display.update()
