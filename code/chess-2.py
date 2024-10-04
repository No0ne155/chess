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
red = (255,0,0)
green = (0,255,0)
clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 600))
turn = True
font_path = pygame.font.get_default_font()
myfont = pygame.font.Font(font_path, 26)
h_moves = []
turn = True
capture = False


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

def display_text(text,x,y):
    text_surface =myfont.render(text, True, black)
    window.blit(text_surface, (x,y))

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

def listboard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            display_text(f"{board[i][j]}¦", 500+(j*30), 10+(i*30))

def israngep(valuep):
    if valuep >= 1 and valuep <= 7:
        return True
    
def israngen(valuem):
    if valuem >= -7 and valuem <= -1:
        return True

class Chess:
    def __init__(self, coords, team, img, piece) -> None:
        self.coords = coords
        self.team = team
        self.img = img
        self.click = False
        self.lmoves = []
        self.capture = []
        self.piece = piece
        self.ex = True
    
    def draw(self):
        if self.ex == True:
            window.blit(self.img, (self.coords[0]*60+5, self.coords[1]*60+5))
            board[self.coords[1]][self.coords[0]] = 1
            board[self.coords[1]+8][self.coords[0]] = self.piece
    
    def legalmoves(self):
        pass

# Klasse für Bauern
class Pawn(Chess):
    def __init__(self, coords, team, img) -> None:
        super().__init__(coords, team, img, 'p')

    # Funktion um die legalen Züge in eine liste hinzuzufügen
    def legalmoves(self):
        if self.team == 0:
            if turn == True:
                if board[self.coords[1]-1][self.coords[0]] == 0:
                    self.lmoves.append((self.coords[1]-1,self.coords[0]))
                    if self.coords[1] == 6:
                        if board[self.coords[1]-2][self.coords[0]] == 0:
                            self.lmoves.append((self.coords[1]-2,self.coords[0]))
                if self.coords[0] <= 6:
                    if board[self.coords[1]-1][self.coords[0]+1] == 1:
                        if isenemy(self.coords[0]+1, self.coords[1]-1, self.team) == True:
                            self.capture.append((self.coords[1]-1,self.coords[0]+1))
                if self.coords[0] >= 1:
                    if board[self.coords[1]-1][self.coords[0]-1] == 1:
                        if isenemy(self.coords[0]-1, self.coords[1]-1, self.team) == True:
                            self.capture.append((self.coords[1]-1,self.coords[0]-1))
        elif self.team == 1:
            if turn == False:
                if board[self.coords[1]+1][self.coords[0]] == 0:
                    self.lmoves.append((self.coords[1]+1,self.coords[0]))
                    if self.coords[1] == 1:
                        if board[self.coords[1]+2][self.coords[0]] == 0:
                            self.lmoves.append((self.coords[1]+2,self.coords[0]))
                if self.coords[0] <= 6:
                    if board[self.coords[1]+1][self.coords[0]+1] == 1:
                        if isenemy(self.coords[0]+1, self.coords[1]+1, self.team) == True:
                            self.capture.append((self.coords[1]+1,self.coords[0]+1))
                if self.coords[0] >= 1:
                    if board[self.coords[1]+1][self.coords[0]-1] == 1:
                        if isenemy(self.coords[0]-1, self.coords[1]+1, self.team) == True:
                            self.capture.append((self.coords[1]+1,self.coords[0]-1))
    
# Klasse für Türme
class Rook(Chess):
    def __init__(self, coords, team, img) -> None:
        super().__init__(coords, team, img, 'r')

    # Funktion um die Legalen züge in eine liste hinzuzufügen
    def legalmoves(self):
        s = 1
        while israngep(s) == True:
            if 0 <= self.coords[1]+s <= 7:
                if board[self.coords[1]+s][self.coords[0]] == 0:
                    if self.team == 0 and turn == True:
                        self.lmoves.append((self.coords[1]+s, self.coords[0]))
                    if self.team == 1 and turn == False:
                        self.lmoves.append((self.coords[1]+s, self.coords[0]))
                if board[self.coords[1]+s][self.coords[0]] == 1:
                    if isenemy(self.coords[0], self.coords[1]+s, self.team) == True:
                        if self.team == 0 and turn == True:
                            self.capture.append((self.coords[1]+s, self.coords[0]))
                        if self.team == 1 and turn == False:
                            self.capture.append((self.coords[1]+s, self.coords[0]))
                    s = s+7
            s = s+1
        o = 1
        while israngep(o) == True:
            if 0 <= self.coords[0]+o <= 7:
                if board[self.coords[1]][self.coords[0]+o] == 0:
                    if self.team == 0 and turn == True:
                        self.lmoves.append((self.coords[1], self.coords[0]+o))
                    if self.team == 1 and turn == False:
                        self.lmoves.append((self.coords[1], self.coords[0]+o))
                if board[self.coords[1]][self.coords[0]+o] == 1:
                    if isenemy(self.coords[0]+o, self.coords[1], self.team) == True:
                        if self.team == 0 and turn == True:
                            self.capture.append((self.coords[1], self.coords[0]+o))
                        if self.team == 1 and turn == False:
                            self.capture.append((self.coords[1], self.coords[0]+o))
                    o = o+7
            o = o+1
        n = -1
        while israngen(n) == True:
            if 0 <= self.coords[1]+n <= 7:
                if board[self.coords[1]+n][self.coords[0]] == 0:
                    if self.team == 0 and turn == True:
                        self.lmoves.append((self.coords[1]+n, self.coords[0]))
                    if self.team == 1 and turn == False:
                        self.lmoves.append((self.coords[1]+n, self.coords[0]))
                if board[self.coords[1]+n][self.coords[0]] == 1:
                    if isenemy(self.coords[0], self.coords[1]+n, self.team) == True:
                        if self.team == 0 and turn == True:
                            self.capture.append((self.coords[1]+n, self.coords[0]))
                        if self.team == 1 and turn == False:
                            self.capture.append((self.coords[1]+n, self.coords[0]))
                    n = n-7
            n = n-1
        w = -1
        while israngen(w) == True:
            if 0 <= self.coords[0]+w <= 7:
                if board[self.coords[1]][self.coords[0]+w] == 0:
                    if self.team == 0 and turn == True:
                        self.lmoves.append((self.coords[1], self.coords[0]+w))
                    if self.team == 1 and turn == False:
                        self.lmoves.append((self.coords[1], self.coords[0]+w))
                if board[self.coords[1]][self.coords[0]+w] == 1:
                    if isenemy(self.coords[0]+w, self.coords[1], self.team) == True:
                        if self.team == 0 and turn == True:
                            self.capture.append((self.coords[1], self.coords[0]+w))
                        if self.team == 1 and turn == False:
                            self.capture.append((self.coords[1], self.coords[0]+w))
                    w = w-7
            w = w-1

# Klasse für Pferde
class Knight(Chess):
    def __init__(self, coords, team, img) -> None:
        super().__init__(coords, team, img, 'n')

    # Funktion um die Legalen züge in eine liste hinzuzufügen
    def legalmoves(self):
        k_moves = [(-2,-1), (-2,+1), (-1,-2), (-1,+2), (+1,-2), (+1,+2), (+2,-1), (+2,+1)]
        for i in range(len(k_moves)):
            if 0 <= self.coords[0]+k_moves[i][0] <= 7 and 0 <= self.coords[1]+k_moves[i][1] <= 7:
                if board[self.coords[1]+k_moves[i][1]][self.coords[0]+k_moves[i][0]] == 0:
                    if self.team == 0 and turn == True:                           
                        self.lmoves.append((self.coords[1]+k_moves[i][1], self.coords[0]+k_moves[i][0]))
                    if self.team == 1 and turn == False:
                        self.lmoves.append((self.coords[1]+k_moves[i][1], self.coords[0]+k_moves[i][0]))
                if board[self.coords[1]+k_moves[i][1]][self.coords[0]+k_moves[i][0]] == 1:
                    if isenemy(self.coords[0]+k_moves[i][0], self.coords[1]+k_moves[i][1], self.team) == True:
                        if self.team == 0 and turn == True:
                            self.capture.append((self.coords[1]+k_moves[i][1], self.coords[0]+k_moves[i][0]))
                        if self.team == 1 and turn == False:
                            self.capture.append((self.coords[1]+k_moves[i][1], self.coords[0]+k_moves[i][0]))

# Klasse für Läufer
class Bishop(Chess):
    def __init__(self, coords, team, img) -> None:
        super().__init__(coords, team, img, 'b')

    # Funktion um die Legalen züge in eine liste hinzuzufügen
    def legalmoves(self):
        pass
    
# Klasse für Damen
class Queen(Chess):
    def __init__(self, coords, team, img) -> None:
        super().__init__(coords, team, img, 'q')

    # Funktion um die Legalen züge in eine liste hinzuzufügen
    def legalmoves(self):
        Rook.legalmoves(self)

# Klasse für den König
class King(Chess):
    def __init__(self, coords, team, img) -> None:
        super().__init__(coords, team, img, 'k')

    # Funktion um die Legalen züge in eine liste hinzuzufügen
    def legalmoves(self):
        pass


# Mouse-Click Handeling
def handle_mouse_click(c_x, c_y):
    global turn
    global capture
    for piece in all_pieces:
        if piece.click == True:
            if (c_y,c_x) in piece.lmoves:
                board[piece.coords[1]][piece.coords[0]] = 0
                board[piece.coords[1]+8][piece.coords[0]] = ''
                piece.coords = (c_x, c_y)
                board[piece.coords[1]][piece.coords[0]] = 1
                board[piece.coords[1]+8][piece.coords[0]] = piece.piece
                turn = not turn
            if (c_y, c_x) in piece.capture:
                for rem in all_pieces:
                    if rem.coords == (c_x, c_y):
                        board[rem.coords[1]][rem.coords[0]] = 0
                        board[rem.coords[1]+8][rem.coords[0]] = ''
                        rem.coords = (10,10)
                        rem.ex = False
                board[piece.coords[1]][piece.coords[0]] = 0
                board[piece.coords[1]+8][piece.coords[0]] = ''
                piece.coords = (c_x, c_y)
                board[piece.coords[1]][piece.coords[0]] = 1
                board[piece.coords[1]+8][piece.coords[0]] = piece.piece
                turn = not turn
        piece.click=False
        piece.lmoves=[]
        piece.capture=[]
        if piece.coords == (c_x, c_y):
            piece.click=not piece.click
            piece.legalmoves()

def highlight_moves():
    for piece in all_pieces:
        if piece.click == True:
            for i in range(len(piece.lmoves)):
                pygame.draw.rect(window, green, (piece.lmoves[i][1]*60, piece.lmoves[i][0]*60, 60 ,60), 3)
            for i in range(len(piece.capture)):
                pygame.draw.rect(window, red, (piece.capture[i][1]*60, piece.capture[i][0]*60, 60 ,60), 3)

def isenemy(x,y,ownteam):
    for piece in all_pieces:
        if piece.coords == (x, y):
            if piece.team != ownteam:
                return True
            else:
                return False

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

all_pieces = [wpawnA, wpawnB, wpawnC, wpawnD, wpawnE, wpawnF, wpawnG, wpawnH, 
              wrookA, wrookH, wknightB, wknightG, wbishopC, wbishopF, wqueenD, wkingE, 
              bpawnA, bpawnB, bpawnC, bpawnD, bpawnE, bpawnF, bpawnG, bpawnH, 
              brookA, brookH, bknightB, bknightG, bbishopC, bbishopF, bqueenD, bkingE]

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
listb = False
# Main Loop
running = True
while running == True:
    clock.tick(60)
    window.fill(white)

    drawboard()
    drawall()
    highlight_moves()
    if listb == True:
        listboard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_b:
                for i in range(len(board)):
                    print(board[i])
                listb = not listb
            elif event.key == pygame.K_l:
                print(wpawnE.lmoves)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickpos = event.pos
            click_x = math.floor(clickpos[0]/60)
            click_y = math.floor(clickpos[1]/60)
            print('click at: ', click_x, click_y)
            handle_mouse_click(click_x, click_y)


    


    pygame.display.update()
