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
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",],
    ["","","","","","","","",]]

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
        board[self.coords[1]][self.coords[0]] = 1
        board[self.coords[1]+8][self.coords[0]] = 'p'


    def legalmoves(self):
        pass

    def drawmoves(self):
        pygame.draw.circle(window, (255,0,0), (Pawn.coords[0]+25, Pawn.coords[1]-35), 25)

class Rook:
    def __init__(self, coords, team, img ) -> None:
        self.coords = coords
        self.team = team
        self.img = img
    
    def draw(self):
        window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
        board[self.coords[1]][self.coords[0]] = 1
        board[self.coords[1]+8][self.coords[0]] = 'r'


    def legalmoves(self):
        pass

    def drawmoves(self):
        pygame.draw.circle(window, (255,0,0), (Rook.coords[0]+25, Rook.coords[1]-35), 25)


class Knight:
    def __init__(self, coords, team, img ) -> None:
        self.coords = coords
        self.team = team
        self.img = img
    
    def draw(self):
        window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
        board[self.coords[1]][self.coords[0]] = 1
        board[self.coords[1]+8][self.coords[0]] = 'n'


    def legalmoves(self):
        pass

    def drawmoves(self):
        pygame.draw.circle(window, (255,0,0), (Knight.coords[0]+25, Knight.coords[1]-35), 25)
    

class Bishop:
    def __init__(self, coords, team, img ) -> None:
        self.coords = coords
        self.team = team
        self.img = img
    
    def draw(self):
        window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
        board[self.coords[1]][self.coords[0]] = 1
        board[self.coords[1]+8][self.coords[0]] = 'b'


    def legalmoves(self):
        pass

    def drawmoves(self):
        pygame.draw.circle(window, (255,0,0), (Bishop.coords[0]+25, Bishop.coords[1]-35), 25)

class Queen:
    def __init__(self, coords, team, img ) -> None:
        self.coords = coords
        self.team = team
        self.img = img
    
    def draw(self):
        window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
        board[self.coords[1]][self.coords[0]] = 1
        board[self.coords[1]+8][self.coords[0]] = 'q'


    def legalmoves(self):
        pass

    def drawmoves(self):
        pygame.draw.circle(window, (255,0,0), (Queen.coords[0]+25, Queen.coords[1]-35), 25)

class King:
    def __init__(self, coords, team, img ) -> None:
        self.coords = coords
        self.team = team
        self.img = img
    
    def draw(self):
        window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
        board[self.coords[1]][self.coords[0]] = 1
        board[self.coords[1]+8][self.coords[0]] = 'k'


    def legalmoves(self):
        pass

    def drawmoves(self):
        pygame.draw.circle(window, (255,0,0), (King.coords[0]+25, King.coords[1]-35), 25)



wpawnA = Pawn((0,6), 0, wp)
wpawnB = Pawn((1,6), 0, wp)
wpawnC = Pawn((2,6), 0, wp)
wpawnD = Pawn((3,6), 0, wp)
wpawnE = Pawn((4,6), 0, wp)
wpawnF = Pawn((5,6), 0, wp)
wpawnG = Pawn((6,6), 0, wp)
wpawnH = Pawn((7,6), 0, wp)
wrookA = Rook((0,7), 0, wr)
wrookH = Rook((7,7), 0, wr)
wknightB = Knight((1,7), 0, wn)
wknightG = Knight((6,7), 0, wn)
wbishopC = Bishop((2,7), 0, wb)
wbishopF = Bishop((5,7), 0, wb)
wqueenD = Queen((3,7), 0, wq)
wkingE = King((4,7), 0, wk)

bpawnA = Pawn((0, 1), 1, bp)
bpawnB = Pawn((1, 1), 1, bp)
bpawnC = Pawn((2, 1), 1, bp)
bpawnD = Pawn((3, 1), 1, bp)
bpawnE = Pawn((4, 1), 1, bp)
bpawnF = Pawn((5, 1), 1, bp)
bpawnG = Pawn((6, 1), 1, bp)
bpawnH = Pawn((7, 1), 1, bp)
brookA = Rook((0, 0), 1, br)
brookH = Rook((7, 0), 1, br)
bknightB = Knight((1,0), 1, bn)
bknightG = Knight((6,0), 1, bn)
bbishopC = Bishop((2,0), 1, bb)
bbishopF = Bishop((5,0), 1, bb)
bqueenD = Queen((3,0), 1, bq)
bkingE = King((4,0), 1, bk)

def drawall():
    wpawnA.draw()
    wpawnB.draw()
    wpawnC.draw()
    wpawnD.draw()
    wpawnE.draw()
    wpawnF.draw()
    wpawnG.draw()
    wpawnH.draw()
    wrookA.draw()
    wrookH.draw()
    wknightB.draw()
    wknightG.draw()
    wbishopC.draw()
    wbishopF.draw()
    wqueenD.draw()
    wkingE.draw()
    bpawnA.draw()
    bpawnB.draw()
    bpawnC.draw()
    bpawnD.draw()
    bpawnE.draw()
    bpawnF.draw()
    bpawnG.draw()
    bpawnH.draw()
    brookA.draw()
    brookH.draw()
    bknightB.draw()
    bknightG.draw()
    bbishopC.draw()
    bbishopF.draw()
    bqueenD.draw()
    bkingE.draw()




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
            elif event.key == pygame.K_b:
                for i in range(len(board)):
                    print(board[i])

        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickpos = event.pos
            #handle_mouse_click(clickpos)

    


    pygame.display.update()
