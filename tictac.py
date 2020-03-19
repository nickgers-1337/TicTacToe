
import pygame
from time import sleep
pygame.init()
music = pygame.mixer.music.load('untitled.mp3')
pygame.mixer.music.play(-1)
winner = None
lis = []
p = True
player1 = 'X'
player2 = 'O'
curplayer = player1

win = pygame.display.set_mode((600, 600))
board = [['','',''],
         ['','',''],
         ['','','',]]

def makeboard():
    global win
    pygame.display.set_caption('TicTacToe')
    win.fill((255,255,255))
    pygame.draw.line(win,(0,0,0),(0,200),(600,200),1)
    pygame.draw.line(win,(0,0,0),(0,400),(600,400),1)
    pygame.draw.line(win,(0,0,0),(200,0),(200,600),1)
    pygame.draw.line(win,(0,0,0),(400,0),(400,600),1)
    pygame.display.update()


def rungame():
    global board
    global player1, player2, curplayer, p, winner,lis

   

    
    while p:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               p = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    pos = list(pygame.mouse.get_pos())
                    pos[0] //= 200
                    pos[1] //= 200
                    if not board[pos[1]][pos[0]]:

                        board[pos[1]][pos[0]] = curplayer
                        print(board)
                        updatescr(pos)
                        switch()
                        winmatch()
        if winner:
            finish(lis[0],lis[1],lis[2])
                        

def switch():
    global curplayer
    global player1
    global player2

    if curplayer == player1:
        curplayer = player2
    else:
        curplayer = player1



def updatescr(pos):
    global win
    global curplayer
    if curplayer == 'X':
        points = [(pos[0] * 200 + 30, pos[1] * 200 + 44), (pos[0] * 200 + 44, pos[1] * 200 + 30),
        (pos[0] * 200 + 170, pos[1] * 200 + 156), (pos[0] * 200 + 156, pos[1] * 200 + 170)]
        pygame.draw.polygon(win, (200,0,0), points, 0)
        points = [(pos[0] * 200 + 30, pos[1] * 200 + 156), (pos[0] * 200 + 44, pos[1] * 200 + 170),
        (pos[0] * 200 + 170, pos[1] * 200 + 44), (pos[0] * 200 + 156, pos[1] * 200 + 30)]
        pygame.draw.polygon(win, (200,0,0), points, 0)

 
    else:
        pygame.draw.circle(win,(200,0,0),(pos[0] * 200 + 100, pos[1] * 200 + 100),71,13)

    pygame.display.update()

   
    

def winmatch():
    global board, p, winner, win,lis
    # Check rows
    
    if (board[0][0] == board[0][1]) and (board[0][0] == board[0][2]) and board[0][0]:
        p = False
        lis.append((0,0))
        lis.append((1,0))
        lis.append((2,0))
      
        winner = board[0][0]
    if (board[1][0] == board[1][1]) and (board[1][0] == board[1][2]) and board[1][0]:
        p = False
        lis.append((0,1))
        lis.append((1,1))
        lis.append((2,1))

        

        winner = board[1][0]
    if (board[2][0] == board[2][1]) and (board[2][0] == board[2][2]) and board[2][0]:
        p = False
        lis.append((0,2))
        lis.append((1,2))
        lis.append((2,2))
        
        winner = board[2][0]

    # Check colums
    if (board[0][0] == board[1][0]) and (board[0][0] == board[2][0]) and board [0][0]:
        p = False
        lis.append((0,0))
        lis.append((0,1))
        lis.append((0,2))
        
        winner = board[0][0]

    if (board[0][1] == board[1][1]) and (board[0][1] == board[2][1]) and board [0][1]:
        p = False
        lis.append((1,0))
        lis.append((1,1))
        lis.append((1,2))
        
        winner = board[0][1]
    if (board[0][2] == board[1][2]) and (board[0][2] == board[2][2]) and board [0][2]:
        p = False
        lis.append((2,0))
        lis.append((2,1))
        lis.append((2,2))
     
        winner = board[0][2]

    # Check diagonals
    if (board[0][0] == board[1][1]) and (board[0][0] == board[2][2]) and board[0][0]:
        p = False
        lis.append((0,0))
        lis.append((1,1))
        lis.append((2,2))
       
        winner = board[0][0]
    if (board[2][0] == board[1][1]) and (board[2][0] == board[0][2]) and board[2][0]:
        p = False
        lis.append((0,2))
        lis.append((1,1))
        lis.append((2,0))
        
        winner = board[2][0]

    if board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2]:
        p = False


def finish(pos1,pos2,pos3):
    global win
    switch()
    for i in range(10):
        pygame.draw.rect(win, (255,255,255), (pos1[0] * 200 + 10, pos1[1] * 200 + 10, 180, 180))
        pygame.draw.rect(win, (255,255 , 255), (pos2[0] * 200 + 10, pos2[1] * 200 + 10, 180, 180))
        pygame.draw.rect(win, (255,255,255), (pos3[0] * 200 + 10, pos3[1] * 200 + 10, 180, 180))
        pygame.display.update()
        pygame.time.wait(100)
        updatescr(pos1)
        updatescr(pos2)
        updatescr(pos3)
        pygame.display.update()
        pygame.time.wait(100)



makeboard()
rungame()

print(winner)

