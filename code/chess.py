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


class Pieces:
    def __init__(self, coords, team, piece, img) -> None:
        self.coords = coords
        self.team = team
        self.piece = piece
        self.img = img
        self.rect = img.get_rect(topleft=coords)
        self.click = False
        self.circ=[]
    
    def draw(self):
        window.blit(self.img, self.coords)
    
    def contains_point(self, point):
        return self.rect.collidepoint(point)




def handle_mouse_click(click_pos):
    for piece in all_pieces:  # all_pieces is a list of all piece instances
        if piece.click == True:
            distance = math.sqrt((click_pos[0] - piece.circ[0])**2 + (click_pos[1] - piece.circ[1])**2)
            if distance <= 27:
                piece.coords = piece.coords[0], piece.coords[1]-60
            piece.click= False
            piece.circ=[]
        elif piece.contains_point(click_pos):
            print(f"Clicked on {piece.piece} of team {piece.team}")
            piece.click=not piece.click

def drawmoves():
    for piece in all_pieces:
        if piece.click == True:
            if piece.team == 0:
                if piece.piece == 0:
                    pygame.draw.circle(window, (255,0,0), (piece.coords[0]+25, piece.coords[1]-35), 25)
                    piece.circ=[piece.coords[0]+25, piece.coords[1]-35]
                    pygame.draw.circle(window, (255,0,0), (piece.coords[0]+25, piece.coords[1]-95), 25)
                
                elif piece.piece == 2:  
                    pygame.draw.circle(window, (255,0,0), (piece.coords[0]+85, piece.coords[1]-95), 25)
                    pygame.draw.circle(window, (255,0,0), (piece.coords[0]-35, piece.coords[1]-95), 25)

            
            elif piece.team == 1:
                if piece.piece == 0:
                    pygame.draw.circle(window, (255,255,0), (piece.coords[0]+25, piece.coords[1]+85), 25)
                    pygame.draw.circle(window, (255,255,0), (piece.coords[0]+25, piece.coords[1]+145), 25)

                if piece.piece == 2:
                    pygame.draw.circle(window, (255,255,0), (piece.coords[0]+85, piece.coords[1]+145), 25)
                    pygame.draw.circle(window, (255,255,0), (piece.coords[0]-35, piece.coords[1]+145), 25)

wpA = Pieces(( 15, 415), 0, 0, wp)
wpB = Pieces(( 75, 415), 0, 0, wp)
wpC = Pieces((135, 415), 0, 0, wp)
wpD = Pieces((195, 415), 0, 0, wp)
wpE = Pieces((255, 415), 0, 0, wp)
wpF = Pieces((315, 415), 0, 0, wp)
wpG = Pieces((375, 415), 0, 0, wp)
wpH = Pieces((435, 415), 0, 0, wp)
wbC = Pieces((135, 475), 0, 1, wb)
wbF = Pieces((315, 475), 0, 1, wb)
wnB = Pieces(( 75, 475), 0, 2, wn)
wnG = Pieces((375, 475), 0, 2, wn)
wrA = Pieces(( 15, 475), 0, 3, wr)
wrH = Pieces((435, 475), 0, 3, wr)
wqD = Pieces((195, 475), 0, 4, wq)
wkE = Pieces((255, 475), 0, 5, wk)

bpA = Pieces(( 15, 115), 1, 0, bp)
bpB = Pieces(( 75, 115), 1, 0, bp)
bpC = Pieces((135, 115), 1, 0, bp)
bpD = Pieces((195, 115), 1, 0, bp)
bpE = Pieces((255, 115), 1, 0, bp)
bpF = Pieces((315, 115), 1, 0, bp)
bpG = Pieces((375, 115), 1, 0, bp)
bpH = Pieces((435, 115), 1, 0, bp)
bbC = Pieces((135, 55), 1, 1, bb)
bbF = Pieces((315, 55), 1, 1, bb)
bnB = Pieces(( 75, 55), 1, 2, bn)
bnG = Pieces((375, 55), 1, 2, bn)
brA = Pieces(( 15, 55), 1, 3, br)
brH = Pieces((435, 55), 1, 3, br)
bqD = Pieces((195, 55), 1, 4, bq)
bkE = Pieces((255, 55), 1, 5, bk)

all_pieces = [wpA, wpB, wpC, wpD, wpE, wpF, wpG, wpH, wbC, wbF, wnB, wnG, wrA, wrH, wqD, wkE, 
              bpA, bpB, bpC, bpD, bpE, bpF, bpG, bpH, bbC, bbF, bnB, bnG, brA, brH, bqD, bkE]


def drawstart():
    wpA.draw()
    wpB.draw()
    wpC.draw()
    wpD.draw()
    wpE.draw()
    wpF.draw()
    wpG.draw()
    wpH.draw()
    wrA.draw()
    wnB.draw()
    wbC.draw()
    wqD.draw()
    wkE.draw()
    wbF.draw()
    wnG.draw()
    wrH.draw()

    bpA.draw()
    bpB.draw()
    bpC.draw()
    bpD.draw()
    bpE.draw()
    bpF.draw()
    bpG.draw()
    bpH.draw()
    brA.draw()
    bnB.draw()
    bbC.draw()
    bqD.draw()
    bkE.draw()
    bbF.draw()
    bnG.draw()
    brH.draw()

window.blit(bp, (75, 175))

# Main Loop
running = True
while running == True:
    clock.tick(60)
    window.fill(white)

    drawboard()
    drawstart()
    drawmoves()

    # Tastenabfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickpos = event.pos
            handle_mouse_click(clickpos)

    


    pygame.display.update()
