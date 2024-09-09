import pygame



pygame.init()

white = (255,255,255)
lgray = (190,190,190)
dgray = (50,50,50)
black = (0,0,0)
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 600))


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

def drawboard():
    for i in range(1,8,2):
        for j in range(0,7,2):
            pygame.draw.rect(window, dgray, ((i*60+10),(j*60+50),60,60))
    for i in range(0,7,2):
        for j in range(1,8,2):
            pygame.draw.rect(window, dgray, ((i*60+10),(j*60+50),60,60))
    for i in range(0,7,2):
        for j in range(0,7,2):
            pygame.draw.rect(window, lgray, ((i*60+10),(j*60+50),60,60))
    for i in range(1,8,2):
        for j in range(1,8,2):
            pygame.draw.rect(window, lgray, ((i*60+10),(j*60+50),60,60))
    pygame.draw.rect(window, black, (10,50,480 ,480),2)

def drawpieces():
    for i in range (8):
        window.blit(bp, (i*60+15, 115))
        window.blit(wp, (i*60+15, 415))
    window.blit(wr, (7*60+15, 475))
    window.blit(wn, (6*60+15, 475))
    window.blit(wb, (5*60+15, 475))
    window.blit(wk, (4*60+15, 475))
    window.blit(wq, (3*60+15, 475))
    window.blit(wb, (2*60+15, 475))
    window.blit(wn, (1*60+15, 475))
    window.blit(wr, (0*60+15, 475))

    window.blit(br, (7*60+15, 55))
    window.blit(bn, (6*60+15, 55))
    window.blit(bb, (5*60+15, 55))
    window.blit(bk, (4*60+15, 55))
    window.blit(bq, (3*60+15, 55))
    window.blit(bb, (2*60+15, 55))
    window.blit(bn, (1*60+15, 55))
    window.blit(br, (0*60+15, 55))

class Pieces:
    def __init__(self, coords, team) -> None:
        self.coords = coords
        self.team = team
    
    class Pawn:
        def __init__(self) -> None:
            pass



# Main Loop
running = True
while running == True:
    clock.tick(60)
    window.fill(white)

    drawboard()
    drawpieces()
    # Tastenabfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    


    pygame.display.update()
