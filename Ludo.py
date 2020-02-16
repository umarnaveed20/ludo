import pygame
import random
from abc import ABCMeta,abstractmethod
pygame.init()


###############################     VARIABLES      ###############################################################################
boardWidth = 800
boardHeight = 700
win = pygame.display.set_mode((boardWidth,boardHeight))
pygame.display.set_caption("Ludo Star by Esha & Umar")
music = pygame.mixer.music.load('music.mp3')
killSound = pygame.mixer.Sound('kill.wav')
buttonSound = pygame.mixer.Sound('button.wav')
errorSound = pygame.mixer.Sound('error.wav')
moveSound = pygame.mixer.Sound('move.wav')
diceSound = pygame.mixer.Sound('dice.wav')
typeSound = pygame.mixer.Sound('type.wav')
pygame.mixer.music.play(-1)
bg = pygame.image.load('bg7.jpg')
bgY = 0
abc = {pygame.K_q:'Q',pygame.K_w:'W',pygame.K_e:'E',pygame.K_r:'R',pygame.K_t:'T',pygame.K_y:'Y',pygame.K_u:'U',pygame.K_i:'I',pygame.K_o:'O',pygame.K_p:'P',pygame.K_a:'A',pygame.K_s:'S',pygame.K_d:'D',pygame.K_f:'F',pygame.K_g:'G',pygame.K_h:'H',pygame.K_j:'J',pygame.K_k:'K',pygame.K_l:'L',pygame.K_z:'Z',pygame.K_x:'X',pygame.K_c:'C',pygame.K_v:'V',pygame.K_b:'B',pygame.K_n:'N',pygame.K_m:'M'}
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
lightYellow = (255,255,102)
white = (255,255,255)
black = (0,0,0)
purple = (153,0,153)
redName = ''
yellowName = ''
greenName = ''
blueName = ''
cd = 7
enter = 'red'
name = redName
Turn = 'Red'
Dice = True
tsCD = 10
nmCD = 10
run = True
play = False
start = True
inst = False
end = False
guide = False
game = False
diceChoice = True
diceCD = 0
moveCD = 0
allow = True
arrow = 350
pieceChoice = 1
redDone = False
greenDone = False
yellowDone = False
blueDone = False


#####################################################      FONTS AND TEXTS     ########################################################################

font = pygame.font.SysFont('comicsans', 50, True)
text = font.render('LUDO STAR', 1, white)
font1 = pygame.font.SysFont('comicsans', 80, True)
text1 = font1.render('LUDO STAR', 1, yellow)
font2 = pygame.font.SysFont('comicsans', 35)
font3 = pygame.font.SysFont('comicsans', 25)
font4 = pygame.font.SysFont('comicsans', 20)
text2 = font2.render('By: Esha & Umar', 1, yellow)
text3 = font.render('PLAY', 1, white)
text4 = font.render('PLAY', 1, black)
text5 = font.render('INSTRUCTIONS', 1, white)
text6 = font.render('INSTRUCTIONS', 1, black)
text7 = font.render('QUIT', 1, white)
text8 = font.render('QUIT', 1, black)
text9 = font2.render('1) Press "SPACE" key to roll dice on your turn.', 1, purple)
text10 = font2.render('(Three consecutive sixes will make you lose your turn)', 1, purple)
text11 = font2.render('2) Use UP and DOWN arrow keys to highlight', 1, purple)
text12 = font2.render('the number you want to use.', 1, purple)
text13 = font2.render('3) Press "ENTER" key to select the highlighted number.', 1, purple)
text14 = font2.render('4) Use UP and DOWN arrow keys to highlight', 1, purple)
text15 = font2.render('the piece you want to move.', 1, purple)
text016 = font2.render('5) Press "ENTER" key to move the highlighted piece.', 1, purple)
text16 = font.render('Enter Player 1 Name:', 1, white)
text17 = font.render('Enter Player 2 Name:', 1, white)
text18 = font.render('Enter Player 3 Name:', 1, white)
text19 = font.render('Enter Player 4 Name:', 1, white)
textOne = font2.render('1', 1, black)
textTwo = font2.render('2', 1, black)
textThree = font2.render('3', 1, black)
textFour = font2.render('4', 1, black)
textOne_w = font2.render('1', 1, white)
textTwo_w = font2.render('2', 1, white)
textThree_w = font2.render('3', 1, white)
textFour_w = font2.render('4', 1, white)
threeS = font3.render('You got 3 consecutive sixes!',1,black)
noMove = font3.render('You cannot make a move!',1,black)
roll = font4.render('Press SPACE key to roll dice',1,black)
selectNo = font4.render('Use arrow keys to select a number',1,black)
useNo = font4.render('Press ENTER key to use the number',1,black)
selectPiece = font4.render('Use arrow keys to select a piece',1,black)
usePiece = font4.render('Press ENTER key to move the piece',1,black)
won = font.render('WON!!', 1, black)
first = font1.render('1st',1, black)
second = font1.render('2nd',1, black)
third = font1.render('3rd',1, black)
position = first


###########################################################         DRAWING BOARD       ###########################################################
def boardDraw():
    global position
    global redDone
    global greenDone
    global yellowDone
    global blueDone
    
    #big squares
    pygame.draw.rect(win,red,(100,50,240,240))
    pygame.draw.rect(win,blue,(460,50,240,240))
    pygame.draw.rect(win,green,(100,410,240,240))
    pygame.draw.rect(win,yellow,(460,410,240,240))
    #borders
    pygame.draw.rect(win,black,(100,50,240,240),3)
    pygame.draw.rect(win,black,(460,50,240,240),3)
    pygame.draw.rect(win,black,(100,410,240,240),3)
    pygame.draw.rect(win,black,(460,410,240,240),3)   

    #inside squares
    pygame.draw.rect(win,white,(140,90,160,160))
    pygame.draw.rect(win,white,(500,90,160,160))
    pygame.draw.rect(win,white,(140,450,160,160))
    pygame.draw.rect(win,white,(500,450,160,160))
    #borders
    pygame.draw.rect(win,black,(140,90,160,160),3)
    pygame.draw.rect(win,black,(500,90,160,160),3)
    pygame.draw.rect(win,black,(140,450,160,160),3)
    pygame.draw.rect(win,black,(500,450,160,160),3)
    
    #circles
    if playerRed.win:
        if playerRed.name:
            if not redDone:
                playerRed.position = position
                if position == first:
                    position = second
                elif position == second:
                    position = third
                redDone = True
            win.blit(won,(220-won.get_width()/2,140-won.get_height()/2))
            win.blit(playerRed.position,(220-playerRed.position.get_width()/2,200-playerRed.position.get_height()/2))
        else:
            pygame.draw.circle(win,black,(175,125),25,3)
            pygame.draw.circle(win,black,(265,125),25,3)
            pygame.draw.circle(win,black,(175,215),25,3)
            pygame.draw.circle(win,black,(265,215),25,3)
    else:
        pygame.draw.circle(win,black,(175,125),25,3)
        pygame.draw.circle(win,black,(265,125),25,3)
        pygame.draw.circle(win,black,(175,215),25,3)
        pygame.draw.circle(win,black,(265,215),25,3)

    if playerGreen.win:
        if playerGreen.name:
            if not greenDone:
                playerGreen.position = position
                if position == first:
                    position = second
                elif position == second:
                    position = third
                greenDone = True
            win.blit(won,(220-won.get_width()/2,500-won.get_height()/2))
            win.blit(playerGreen.position,(220-playerGreen.position.get_width()/2,560-playerGreen.position.get_height()/2))
        else:
            pygame.draw.circle(win,black,(175,485),25,3)
            pygame.draw.circle(win,black,(265,485),25,3)
            pygame.draw.circle(win,black,(175,575),25,3)
            pygame.draw.circle(win,black,(265,575),25,3)
    else:
        pygame.draw.circle(win,black,(175,485),25,3)
        pygame.draw.circle(win,black,(265,485),25,3)
        pygame.draw.circle(win,black,(175,575),25,3)
        pygame.draw.circle(win,black,(265,575),25,3)

    if playerBlue.win:
        if playerBlue.name:
            if not blueDone:
                playerBlue.position = position
                if position == first:
                    position = second
                elif position == second:
                    position = third
                blueDone = True
            win.blit(won,(580-won.get_width()/2,140-won.get_height()/2))
            win.blit(playerBlue.position,(580-playerBlue.position.get_width()/2,200-playerBlue.position.get_height()/2))
        else:
            pygame.draw.circle(win,black,(535,125),25,3)
            pygame.draw.circle(win,black,(625,125),25,3)
            pygame.draw.circle(win,black,(535,215),25,3)
            pygame.draw.circle(win,black,(625,215),25,3)
    else:
        pygame.draw.circle(win,black,(535,125),25,3)
        pygame.draw.circle(win,black,(625,125),25,3)
        pygame.draw.circle(win,black,(535,215),25,3)
        pygame.draw.circle(win,black,(625,215),25,3)

    if playerYellow.win:
        if playerYellow.name:
            if not yellowDone:
                playerYellow.position = position
                if position == first:
                    position = second
                elif position == second:
                    position = third
                yellowDone = True
            win.blit(won,(580-won.get_width()/2,500-won.get_height()/2))
            win.blit(playerYellow.position,(580-playerYellow.position.get_width()/2,560-playerYellow.position.get_height()/2))
        else:
            pygame.draw.circle(win,black,(535,485),25,3)
            pygame.draw.circle(win,black,(625,485),25,3)
            pygame.draw.circle(win,black,(535,575),25,3)
            pygame.draw.circle(win,black,(625,575),25,3)
    else:
        pygame.draw.circle(win,black,(535,485),25,3)
        pygame.draw.circle(win,black,(625,485),25,3)
        pygame.draw.circle(win,black,(535,575),25,3)
        pygame.draw.circle(win,black,(625,575),25,3)

    #rows squares
    #red squares
    pygame.draw.rect(win,white,(100,290,40,40))
    pygame.draw.rect(win,white,(100,330,40,40))
    pygame.draw.rect(win,white,(100,370,40,40))
    pygame.draw.rect(win,red,(140,290,40,40))
    pygame.draw.rect(win,white,(140,370,40,40))
    pygame.draw.rect(win,red,(140,330,40,40))
    pygame.draw.rect(win,white,(180,290,40,40))
    pygame.draw.rect(win,red,(180,330,40,40))
    pygame.draw.rect(win,red,(180,370,40,40))
    pygame.draw.rect(win,white,(220,290,40,40))
    pygame.draw.rect(win,red,(220,330,40,40))
    pygame.draw.rect(win,white,(220,370,40,40))
    pygame.draw.rect(win,white,(260,290,40,40))
    pygame.draw.rect(win,red,(260,330,40,40))
    pygame.draw.rect(win,white,(260,370,40,40))
    pygame.draw.rect(win,white,(300,290,40,40))
    pygame.draw.rect(win,red,(300,330,40,40))
    pygame.draw.rect(win,white,(300,370,40,40))
    #borders
    pygame.draw.rect(win,black,(100,290,40,40),1)
    pygame.draw.rect(win,black,(100,330,40,40),1)
    pygame.draw.rect(win,black,(100,370,40,40),1)
    pygame.draw.rect(win,black,(140,290,40,40),1)
    pygame.draw.rect(win,black,(140,370,40,40),1)
    pygame.draw.rect(win,black,(140,330,40,40),1)
    pygame.draw.rect(win,black,(180,290,40,40),1)
    pygame.draw.rect(win,black,(180,330,40,40),1)
    pygame.draw.rect(win,black,(180,370,40,40),1)
    pygame.draw.rect(win,black,(220,290,40,40),1)
    pygame.draw.rect(win,black,(220,330,40,40),1)
    pygame.draw.rect(win,black,(220,370,40,40),1)
    pygame.draw.rect(win,black,(260,290,40,40),1)
    pygame.draw.rect(win,black,(260,330,40,40),1)
    pygame.draw.rect(win,black,(260,370,40,40),1)
    pygame.draw.rect(win,black,(300,290,40,40),1)
    pygame.draw.rect(win,black,(300,330,40,40),1)
    pygame.draw.rect(win,black,(300,370,40,40),1)

    #blue squares
    pygame.draw.rect(win,white,(340,50,40,40))
    pygame.draw.rect(win,white,(380,50,40,40))
    pygame.draw.rect(win,white,(420,50,40,40))
    pygame.draw.rect(win,white,(340,90,40,40))
    pygame.draw.rect(win,blue,(380,90,40,40))
    pygame.draw.rect(win,blue,(420,90,40,40))
    pygame.draw.rect(win,blue,(340,130,40,40))
    pygame.draw.rect(win,blue,(380,130,40,40))
    pygame.draw.rect(win,white,(420,130,40,40))
    pygame.draw.rect(win,white,(340,170,40,40))
    pygame.draw.rect(win,blue,(380,170,40,40))
    pygame.draw.rect(win,white,(420,170,40,40))
    pygame.draw.rect(win,white,(340,210,40,40))
    pygame.draw.rect(win,blue,(380,210,40,40))
    pygame.draw.rect(win,white,(420,210,40,40))
    pygame.draw.rect(win,white,(340,250,40,40))
    pygame.draw.rect(win,blue,(380,250,40,40))
    pygame.draw.rect(win,white,(420,250,40,40))
    #borders
    pygame.draw.rect(win,black,(340,50,40,40),1)
    pygame.draw.rect(win,black,(380,50,40,40),1)
    pygame.draw.rect(win,black,(420,50,40,40),1)
    pygame.draw.rect(win,black,(340,90,40,40),1)
    pygame.draw.rect(win,black,(380,90,40,40),1)
    pygame.draw.rect(win,black,(420,90,40,40),1)
    pygame.draw.rect(win,black,(340,130,40,40),1)
    pygame.draw.rect(win,black,(380,130,40,40),1)
    pygame.draw.rect(win,black,(420,130,40,40),1)
    pygame.draw.rect(win,black,(340,170,40,40),1)
    pygame.draw.rect(win,black,(380,170,40,40),1)
    pygame.draw.rect(win,black,(420,170,40,40),1)
    pygame.draw.rect(win,black,(340,210,40,40),1)
    pygame.draw.rect(win,black,(380,210,40,40),1)
    pygame.draw.rect(win,black,(420,210,40,40),1)
    pygame.draw.rect(win,black,(340,250,40,40),1)
    pygame.draw.rect(win,black,(380,250,40,40),1)
    pygame.draw.rect(win,black,(420,250,40,40),1)

    #green squares
    pygame.draw.rect(win,white,(340,410,40,40))
    pygame.draw.rect(win,green,(380,410,40,40))
    pygame.draw.rect(win,white,(420,410,40,40))
    pygame.draw.rect(win,white,(340,450,40,40))
    pygame.draw.rect(win,green,(380,450,40,40))
    pygame.draw.rect(win,white,(420,450,40,40))
    pygame.draw.rect(win,white,(340,490,40,40))
    pygame.draw.rect(win,green,(380,490,40,40))
    pygame.draw.rect(win,white,(420,490,40,40))
    pygame.draw.rect(win,white,(340,530,40,40))
    pygame.draw.rect(win,green,(380,530,40,40))
    pygame.draw.rect(win,green,(420,530,40,40))
    pygame.draw.rect(win,green,(340,570,40,40))
    pygame.draw.rect(win,green,(380,570,40,40))
    pygame.draw.rect(win,white,(420,570,40,40))
    pygame.draw.rect(win,white,(340,610,40,40))
    pygame.draw.rect(win,white,(380,610,40,40))
    pygame.draw.rect(win,white,(420,610,40,40))
    #borders
    pygame.draw.rect(win,black,(340,410,40,40),1)
    pygame.draw.rect(win,black,(380,410,40,40),1)
    pygame.draw.rect(win,black,(420,410,40,40),1)
    pygame.draw.rect(win,black,(340,450,40,40),1)
    pygame.draw.rect(win,black,(380,450,40,40),1)
    pygame.draw.rect(win,black,(420,450,40,40),1)
    pygame.draw.rect(win,black,(340,490,40,40),1)
    pygame.draw.rect(win,black,(380,490,40,40),1)
    pygame.draw.rect(win,black,(420,490,40,40),1)
    pygame.draw.rect(win,black,(340,530,40,40),1)
    pygame.draw.rect(win,black,(380,530,40,40),1)
    pygame.draw.rect(win,black,(420,530,40,40),1)
    pygame.draw.rect(win,black,(340,570,40,40),1)
    pygame.draw.rect(win,black,(380,570,40,40),1)
    pygame.draw.rect(win,black,(420,570,40,40),1)
    pygame.draw.rect(win,black,(340,610,40,40),1)
    pygame.draw.rect(win,black,(380,610,40,40),1)
    pygame.draw.rect(win,black,(420,610,40,40),1)

    #yellow squares
    pygame.draw.rect(win,white,(460,290,40,40))
    pygame.draw.rect(win,yellow,(460,330,40,40))
    pygame.draw.rect(win,white,(460,370,40,40))
    pygame.draw.rect(win,white,(500,290,40,40))
    pygame.draw.rect(win,yellow,(500,330,40,40))
    pygame.draw.rect(win,white,(500,370,40,40))
    pygame.draw.rect(win,white,(540,290,40,40))
    pygame.draw.rect(win,yellow,(540,330,40,40))
    pygame.draw.rect(win,white,(540,370,40,40))
    pygame.draw.rect(win,yellow,(580,290,40,40))
    pygame.draw.rect(win,yellow,(580,330,40,40))
    pygame.draw.rect(win,white,(580,370,40,40))
    pygame.draw.rect(win,white,(620,290,40,40))
    pygame.draw.rect(win,yellow,(620,330,40,40))
    pygame.draw.rect(win,yellow,(620,370,40,40))
    pygame.draw.rect(win,white,(660,290,40,40))
    pygame.draw.rect(win,white,(660,330,40,40))
    pygame.draw.rect(win,white,(660,370,40,40))
    #borders
    pygame.draw.rect(win,black,(460,290,40,40),1)
    pygame.draw.rect(win,black,(460,330,40,40),1)
    pygame.draw.rect(win,black,(460,370,40,40),1)
    pygame.draw.rect(win,black,(500,290,40,40),1)
    pygame.draw.rect(win,black,(500,330,40,40),1)
    pygame.draw.rect(win,black,(500,370,40,40),1)
    pygame.draw.rect(win,black,(540,290,40,40),1)
    pygame.draw.rect(win,black,(540,330,40,40),1)
    pygame.draw.rect(win,black,(540,370,40,40),1)
    pygame.draw.rect(win,black,(580,290,40,40),1)
    pygame.draw.rect(win,black,(580,330,40,40),1)
    pygame.draw.rect(win,black,(580,370,40,40),1)
    pygame.draw.rect(win,black,(620,290,40,40),1)
    pygame.draw.rect(win,black,(620,330,40,40),1)
    pygame.draw.rect(win,black,(620,370,40,40),1)
    pygame.draw.rect(win,black,(660,290,40,40),1)
    pygame.draw.rect(win,black,(660,330,40,40),1)
    pygame.draw.rect(win,black,(660,370,40,40),1)   
    
    #center box
    pygame.draw.polygon(win,red,((340,290),(340,410),(400,350)))
    pygame.draw.polygon(win,blue,((340,290),(460,290),(400,350)))
    pygame.draw.polygon(win,green,((460,410),(340,410),(400,350)))
    pygame.draw.polygon(win,yellow,((460,290),(460,410),(400,350)))
    pygame.draw.line(win,black,(340,290),(460,410))
    pygame.draw.line(win,black,(340,410),(460,290))

    #Border
    pygame.draw.rect(win,black,(340,290,120,120),2)
    pygame.draw.rect(win,white,(100,50,600,600),3)


#############################################     DRAWING FUNCTION          #################################################################
def winDraw():
    global tsCD
    global nmCD
    global allow
    global arrow
    win.fill(black)

    if play:

###################################    WHEN GAME IS BEING PLAYED       #########################################################################
        if game:
            boardDraw()
            win.blit(text,((boardWidth/2)-(text.get_width()/2),10))
            pygame.draw.rect(win,lightYellow,(0,0,redFont.get_width()+20,redFont.get_height()+20))
            pygame.draw.rect(win,red,(0,0,redFont.get_width()+20,redFont.get_height()+20),3)
            win.blit(redFont,(10,10))
            pygame.draw.rect(win,lightYellow,(0+10-10,boardHeight-greenFont.get_height()-20,greenFont.get_width()+20,greenFont.get_height()+20))
            pygame.draw.rect(win,red,(0+10-10,boardHeight-greenFont.get_height()-20,greenFont.get_width()+20,greenFont.get_height()+20),3)
            win.blit(greenFont,(0+10,boardHeight-greenFont.get_height()-10))
            pygame.draw.rect(win,lightYellow,(boardWidth-yellowFont.get_width()-10-10,boardHeight-yellowFont.get_height()-20,yellowFont.get_width()+20,yellowFont.get_height()+20))
            pygame.draw.rect(win,red,(boardWidth-yellowFont.get_width()-10-10,boardHeight-yellowFont.get_height()-20,yellowFont.get_width()+20,yellowFont.get_height()+20),3)
            win.blit(yellowFont,(boardWidth-yellowFont.get_width()-10,boardHeight-yellowFont.get_height()-10))
            pygame.draw.rect(win,lightYellow,(boardWidth-blueFont.get_width()-10-10,0,blueFont.get_width()+20,blueFont.get_height()+20))
            pygame.draw.rect(win,red,(boardWidth-blueFont.get_width()-10-10,0,blueFont.get_width()+20,blueFont.get_height()+20),3)
            win.blit(blueFont,(boardWidth-blueFont.get_width()-10,10))
            
            for piece in pieces:
                if Turn == 'Red' and piece.color != red:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)
                elif Turn == 'Green' and piece.color != green:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)
                elif Turn == 'Yellow' and piece.color != yellow:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)
                elif Turn == 'Blue' and piece.color != blue:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)

            for piece in pieces:
                if Turn == 'Red' and piece.color == red:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)
                elif Turn == 'Green' and piece.color == green:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)
                elif Turn == 'Yellow' and piece.color == yellow:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)
                elif Turn == 'Blue' and piece.color == blue:
                    if piece.active and not piece.home:
                        piece.draw(piece.x,piece.y)
                    elif not piece.home:
                        piece.draw(piece.startx,piece.starty)

                
                    
            for player in players:
                if player.threeSix:
                    if tsCD > 0:
                        if player == playerRed:
                            win.blit(threeS,(220-threeS.get_width()/2,70-threeS.get_height()/2))
                        elif player == playerGreen:
                            win.blit(threeS,(220-threeS.get_width()/2,630-threeS.get_height()/2))
                        elif player == playerYellow:
                            win.blit(threeS,(580-threeS.get_width()/2,630-threeS.get_height()/2))
                        else:
                            win.blit(threeS,(580-threeS.get_width()/2,70-threeS.get_height()/2))
                        tsCD -= 1
                    else:
                        player.threeSix = False
                        tsCD = 10

            for player in players:
                if player.noMove:
                    if nmCD > 0:
                        if player == playerRed:
                            win.blit(noMove,(220-noMove.get_width()/2,70-noMove.get_height()/2))
                        elif player == playerGreen:
                            win.blit(noMove,(220-noMove.get_width()/2,630-noMove.get_height()/2))
                        elif player == playerYellow:
                            win.blit(noMove,(580-noMove.get_width()/2,630-noMove.get_height()/2))
                        else:
                            win.blit(noMove,(580-noMove.get_width()/2,70-noMove.get_height()/2))
                        nmCD -= 1
                    else:
                        if Dice:
                            changeTurn()
                        player.noMove = False
                        nmCD = 10
                        

            if not diceChoice:
                for color in colorPlayers:
                        if Turn == color:
                            if pieceChoice == 1:
                                pygame.draw.circle(win,black,(50,245),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,315),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,385),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,455),30)
                                win.blit(textOne_w,(45,235))
                                win.blit(textTwo,(45,305))
                                win.blit(textThree,(45,375))
                                win.blit(textFour,(45,445))
                            elif pieceChoice == 2:
                                pygame.draw.circle(win,colorPlayers[color].color,(50,245),30)
                                pygame.draw.circle(win,black,(50,315),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,385),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,455),30)
                                win.blit(textOne,(45,235))
                                win.blit(textTwo_w,(45,305))
                                win.blit(textThree,(45,375))
                                win.blit(textFour,(45,445))
                            elif pieceChoice == 3:
                                pygame.draw.circle(win,colorPlayers[color].color,(50,245),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,315),30)
                                pygame.draw.circle(win,black,(50,385),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,455),30)
                                win.blit(textOne,(45,235))
                                win.blit(textTwo,(45,305))
                                win.blit(textThree_w,(45,375))
                                win.blit(textFour,(45,445))
                            else:
                                pygame.draw.circle(win,colorPlayers[color].color,(50,245),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,315),30)
                                pygame.draw.circle(win,colorPlayers[color].color,(50,385),30)
                                pygame.draw.circle(win,black,(50,455),30)
                                win.blit(textOne,(45,235))
                                win.blit(textTwo,(45,305))
                                win.blit(textThree,(45,375))
                                win.blit(textFour_w,(45,445))
                            pygame.draw.circle(win,white,(50,315),30,2)
                            pygame.draw.circle(win,white,(50,245),30,2)
                            pygame.draw.circle(win,white,(50,385),30,2)
                            pygame.draw.circle(win,white,(50,455),30,2)

                if not Dice:
                    instruct = True
                    for player in players:
                        if player.noMove or player.threeSix:
                            instruct = False
                    if instruct:
                        if Turn == 'Red':
                            win.blit(selectPiece,(220-selectPiece.get_width()/2,70-selectPiece.get_height()/2))
                            win.blit(usePiece,(220-usePiece.get_width()/2,270-usePiece.get_height()/2))
                        elif Turn == 'Green':
                            win.blit(selectPiece,(220-selectPiece.get_width()/2,430-selectPiece.get_height()/2))
                            win.blit(usePiece,(220-usePiece.get_width()/2,630-usePiece.get_height()/2))
                        elif Turn == 'Yellow':
                            win.blit(selectPiece,(580-selectPiece.get_width()/2,430-selectPiece.get_height()/2))
                            win.blit(usePiece,(580-usePiece.get_width()/2,630-usePiece.get_height()/2))
                        else:
                            win.blit(selectPiece,(580-selectPiece.get_width()/2,70-selectPiece.get_height()/2))
                            win.blit(usePiece,(580-usePiece.get_width()/2,270-usePiece.get_height()/2))
                            
                            
            else:
                for color in colorPlayers:
                        if Turn == color:
                            pygame.draw.circle(win,colorPlayers[color].color,(50,315),30)
                            pygame.draw.circle(win,colorPlayers[color].color,(50,245),30)
                            pygame.draw.circle(win,colorPlayers[color].color,(50,385),30)
                            pygame.draw.circle(win,colorPlayers[color].color,(50,455),30)
                            pygame.draw.circle(win,white,(50,315),30,2)
                            pygame.draw.circle(win,white,(50,245),30,2)
                            pygame.draw.circle(win,white,(50,385),30,2)
                            pygame.draw.circle(win,white,(50,455),30,2)
                            win.blit(textOne,(45,235))
                            win.blit(textTwo,(45,305))
                            win.blit(textThree,(45,375))
                            win.blit(textFour,(45,445))

                if not Dice:
                    instruct = True
                    for player in players:
                        if player.noMove or player.threeSix:
                            instruct = False
                    if instruct:
                        if Turn == 'Red':
                            win.blit(selectNo,(220-selectNo.get_width()/2,70-selectNo.get_height()/2))
                            win.blit(useNo,(220-useNo.get_width()/2,270-useNo.get_height()/2))
                        elif Turn == 'Green':
                            win.blit(selectNo,(220-selectNo.get_width()/2,430-selectNo.get_height()/2))
                            win.blit(useNo,(220-useNo.get_width()/2,630-useNo.get_height()/2))
                        elif Turn == 'Yellow':
                            win.blit(selectNo,(580-selectNo.get_width()/2,430-selectNo.get_height()/2))
                            win.blit(useNo,(580-useNo.get_width()/2,630-useNo.get_height()/2))
                        else:
                            win.blit(selectNo,(580-selectNo.get_width()/2,70-selectNo.get_height()/2))
                            win.blit(useNo,(580-useNo.get_width()/2,270-useNo.get_height()/2))
                    
                            
    
            if Dice:
                for color in colorPlayers:
                    if Turn == color:
                        drawDice(720,320,colorPlayers[color].currentNo)

                instruct = True
                for player in players:
                        if player.noMove or player.threeSix:
                            instruct = False
                if instruct:
                        if Turn == 'Red':
                            win.blit(roll,(220-roll.get_width()/2,70-roll.get_height()/2))
                        elif Turn == 'Green':
                            win.blit(roll,(220-roll.get_width()/2,630-roll.get_height()/2))
                        elif Turn == 'Yellow':
                            win.blit(roll,(580-roll.get_width()/2,630-roll.get_height()/2))
                        else:
                            win.blit(roll,(580-roll.get_width()/2,70-roll.get_height()/2))
                    
            else:
                for color in colorPlayers:
                    if Turn == color:
                        y = 320
                        yPlus = 320
                        yMinus = 320
                        flip = 1
                        change = 0
                        for num in colorPlayers[color].Count:
                            drawDice(730,y,num)
                            if flip == 1:
                                top = yMinus+30
                                bottom = yPlus+30
                                change += 70
                                yMinus -= change
                                y = yMinus
                                
                            else:
                                top = yMinus+30
                                bottom = yPlus+30
                                yPlus += change
                                y = yPlus
                                
                            flip = flip*(-1)
                        if allow:
                            arrow = top
                            allow = False
                        if diceChoice:
                            if keys[pygame.K_DOWN]:
                                if arrow < bottom:
                                    arrow += 70
                                else:
                                    arrow = top
                            if keys[pygame.K_UP]:
                                if arrow > top:
                                    arrow -= 70
                                else:
                                    arrow = bottom
                        else:
                            allow = True
                        pygame.draw.polygon(win,white,((725,arrow),(710,arrow-10),(710,arrow+10)))
                        
                                        
#############################################       NAME INPUTS        #####################################################################           
        else:
            win.blit(bg,(0,bgY))
            win.blit(text1,((boardWidth/2)-(text1.get_width()/2),100))
            
            if enter == 'red':
                pygame.draw.circle(win,red,(boardWidth//2-5,260),30)
                pygame.draw.circle(win,black,(boardWidth//2-5,260),30,3)
                pygame.draw.rect(win,black,((boardWidth/2)-(text16.get_width()/2)-10,350-6,text16.get_width()+20,text16.get_height()+10))
                pygame.draw.rect(win,white,((boardWidth/2)-(text16.get_width()/2)-10,350-6,text16.get_width()+20,text16.get_height()+10),2)
                win.blit(text16,((boardWidth/2)-(text16.get_width()/2),350))
                
            elif enter == 'green':
                pygame.draw.circle(win,green,(boardWidth//2-5,260),30)
                pygame.draw.circle(win,black,(boardWidth//2-5,260),30,3)
                pygame.draw.rect(win,black,((boardWidth/2)-(text17.get_width()/2)-10,350-6,text17.get_width()+20,text17.get_height()+10))
                pygame.draw.rect(win,white,((boardWidth/2)-(text17.get_width()/2)-10,350-6,text17.get_width()+20,text17.get_height()+10),2)
                win.blit(text17,((boardWidth/2)-(text17.get_width()/2),350))
                
            elif enter == 'yellow':                
                pygame.draw.circle(win,yellow,(boardWidth//2-5,260),30)
                pygame.draw.circle(win,black,(boardWidth//2-5,260),30,3)
                pygame.draw.rect(win,black,((boardWidth/2)-(text18.get_width()/2)-10,350-6,text18.get_width()+20,text18.get_height()+10))
                pygame.draw.rect(win,white,((boardWidth/2)-(text18.get_width()/2)-10,350-6,text18.get_width()+20,text18.get_height()+10),2)
                win.blit(text18,((boardWidth/2)-(text18.get_width()/2),350))
                
            else:
                pygame.draw.circle(win,blue,(boardWidth//2-5,260),30)
                pygame.draw.circle(win,black,(boardWidth//2-5,260),30,3)
                pygame.draw.rect(win,black,((boardWidth/2)-(text19.get_width()/2)-10,350-6,text19.get_width()+20,text19.get_height()+10))
                pygame.draw.rect(win,white,((boardWidth/2)-(text19.get_width()/2)-10,350-6,text19.get_width()+20,text19.get_height()+10),2)
                win.blit(text19,((boardWidth/2)-(text19.get_width()/2),350))

            text20 = font.render(name, 1, black)
            if cd < 4:
                pygame.draw.rect(win,white,((boardWidth/2)-(text20.get_width()/2)-10,440-10,text20.get_width()+20,text20.get_height()+20))
                pygame.draw.rect(win,black,((boardWidth/2)-(text20.get_width()/2)-10,440-10,text20.get_width()+20,text20.get_height()+20),2)
                win.blit(text20,((boardWidth/2)-(text20.get_width()/2),440))
            else:
                pygame.draw.rect(win,white,((boardWidth/2)-(text20.get_width()/2)-16,440-10,text20.get_width()+32,text20.get_height()+20))
                pygame.draw.rect(win,black,((boardWidth/2)-(text20.get_width()/2)-16,440-10,text20.get_width()+32,text20.get_height()+20),2)
                win.blit(text20,((boardWidth/2)-(text20.get_width()/2)-6,440))

##################################################      MAIN MENU       ####################################################################33                           
            
    elif guide:
        win.blit(text1,((boardWidth/2)-(text1.get_width()/2),80))
        win.blit(text9,((boardWidth/2)-(text9.get_width()/2),170))
        win.blit(text10,((boardWidth/2)-(text10.get_width()/2),205))
        win.blit(text11,((boardWidth/2)-(text11.get_width()/2),270))
        win.blit(text12,((boardWidth/2)-(text12.get_width()/2),305))
        win.blit(text13,((boardWidth/2)-(text13.get_width()/2),370))
        win.blit(text14,((boardWidth/2)-(text14.get_width()/2),435))
        win.blit(text15,((boardWidth/2)-(text15.get_width()/2),470))
        win.blit(text016,((boardWidth/2)-(text016.get_width()/2),535))

    elif start:
        win.blit(bg,(0,bgY))
        win.blit(text1,((boardWidth/2)-(text1.get_width()/2),100))
        pygame.draw.rect(win,black,((boardWidth/2)-(text4.get_width()/2)-10,230-10,text4.get_width()+20,text4.get_height()+20))
        win.blit(text3,((boardWidth/2)-(text3.get_width()/2),230))
        pygame.draw.rect(win,white,((boardWidth/2)-(text3.get_width()/2)-10,230-10,text3.get_width()+20,text3.get_height()+20),2)
        pygame.draw.rect(win,white,((boardWidth/2)-(text6.get_width()/2)-10,350-10,text6.get_width()+20,text6.get_height()+20))
        win.blit(text6,((boardWidth/2)-(text6.get_width()/2),350))
        pygame.draw.rect(win,black,((boardWidth/2)-(text6.get_width()/2)-10,350-10,text6.get_width()+20,text6.get_height()+20),2)
        pygame.draw.rect(win,white,((boardWidth/2)-(text8.get_width()/2)-10,470-10,text8.get_width()+20,text8.get_height()+20))
        win.blit(text8,((boardWidth/2)-(text8.get_width()/2),470))
        pygame.draw.rect(win,black,((boardWidth/2)-(text8.get_width()/2)-10,470-10,text8.get_width()+20,text8.get_height()+20),2)

    elif inst:
        win.blit(bg,(0,bgY))
        win.blit(text1,((boardWidth/2)-(text1.get_width()/2),100))
        pygame.draw.rect(win,white,((boardWidth/2)-(text4.get_width()/2)-10,230-10,text4.get_width()+20,text4.get_height()+20))
        win.blit(text4,((boardWidth/2)-(text4.get_width()/2),230))
        pygame.draw.rect(win,black,((boardWidth/2)-(text4.get_width()/2)-10,230-10,text4.get_width()+20,text4.get_height()+20),2)
        pygame.draw.rect(win,black,((boardWidth/2)-(text6.get_width()/2)-10,350-10,text6.get_width()+20,text6.get_height()+20))
        win.blit(text5,((boardWidth/2)-(text5.get_width()/2),350))
        pygame.draw.rect(win,white,((boardWidth/2)-(text5.get_width()/2)-10,350-10,text5.get_width()+20,text5.get_height()+20),2)
        pygame.draw.rect(win,white,((boardWidth/2)-(text8.get_width()/2)-10,470-10,text8.get_width()+20,text8.get_height()+20))
        win.blit(text8,((boardWidth/2)-(text8.get_width()/2),470))
        pygame.draw.rect(win,black,((boardWidth/2)-(text8.get_width()/2)-10,470-10,text8.get_width()+20,text8.get_height()+20),2)

    elif end:
        win.blit(bg,(0,bgY))
        win.blit(text1,((boardWidth/2)-(text1.get_width()/2),100))
        pygame.draw.rect(win,white,((boardWidth/2)-(text4.get_width()/2)-10,230-10,text4.get_width()+20,text4.get_height()+20))
        win.blit(text4,((boardWidth/2)-(text4.get_width()/2),230))
        pygame.draw.rect(win,black,((boardWidth/2)-(text4.get_width()/2)-10,230-10,text4.get_width()+20,text4.get_height()+20),2)
        pygame.draw.rect(win,white,((boardWidth/2)-(text6.get_width()/2)-10,350-10,text6.get_width()+20,text6.get_height()+20))
        win.blit(text6,((boardWidth/2)-(text6.get_width()/2),350))
        pygame.draw.rect(win,black,((boardWidth/2)-(text6.get_width()/2)-10,350-10,text6.get_width()+20,text6.get_height()+20),2)
        pygame.draw.rect(win,black,((boardWidth/2)-(text8.get_width()/2)-10,470-10,text8.get_width()+20,text8.get_height()+20))
        win.blit(text7,((boardWidth/2)-(text7.get_width()/2),470))
        pygame.draw.rect(win,white,((boardWidth/2)-(text7.get_width()/2)-10,470-10,text7.get_width()+20,text7.get_height()+20),2)

    if game:
        win.blit(text2,((boardWidth/2)-(text2.get_width()/2),670))
    else:
        win.blit(text2,((boardWidth/2)-(text2.get_width()/2),600))

    pygame.display.update()


    
#####################################################   TO SWITCH TURNS AMONG PLAYERS   ###########################################################

def changeTurn():
    global Turn
    global Dice
    global diceChoice
    
    if Turn == 'Red':
        Turn = 'Green'
        playerRed.Count = []
        playerRed.currentNo = 0
        playerRed.steps = 0
        playerRed.Bonus = False
        playerRed.BonusCount = []
    elif Turn == 'Green':
        Turn = 'Yellow'
        playerGreen.Count = []
        playerGreen.currentNo = 0
        playerGreen.steps = 0
        playerGreen.Bonus = False
        playerGreen.BonusCount = []
    elif Turn == 'Yellow':
        Turn = 'Blue'
        playerYellow.Count = []
        playerYellow.currentNo = 0
        playerYellow.steps = 0
        playerYellow.Bonus = False
        playerYellow.BonusCount = []
    else:
        Turn = 'Red'
        playerBlue.Count = []
        playerBlue.currentNo = 0
        playerBlue.steps = 0
        playerBlue.Bonus = False
        playerBlue.BonusCount = []
        
    Dice = True
    diceChoice = True


##################################################      TO DRAW DICE ON WINDOW         #########################################################
    
def drawDice(x,y,num):
    pygame.draw.rect(win,red,(x,y,60,60))
    pygame.draw.rect(win,white,(x,y,60,60),2)
    
    if num == 1:
        pygame.draw.circle(win,white,(x+30,y+30),5)
    elif num == 2:
        pygame.draw.circle(win,white,(x+45,y+15),5)
        pygame.draw.circle(win,white,(x+15,y+45),5)
    elif num == 3:
        pygame.draw.circle(win,white,(x+30,y+30),5)
        pygame.draw.circle(win,white,(x+45,y+15),5)
        pygame.draw.circle(win,white,(x+15,y+45),5)
    elif num == 4:
        pygame.draw.circle(win,white,(x+45,y+15),5)
        pygame.draw.circle(win,white,(x+15,y+45),5)
        pygame.draw.circle(win,white,(x+15,y+15),5)
        pygame.draw.circle(win,white,(x+45,y+45),5)
    elif num == 5:
        pygame.draw.circle(win,white,(x+45,y+15),5)
        pygame.draw.circle(win,white,(x+15,y+45),5)
        pygame.draw.circle(win,white,(x+15,y+15),5)
        pygame.draw.circle(win,white,(x+45,y+45),5)
        pygame.draw.circle(win,white,(x+30,y+30),5)
    elif num == 6:
        pygame.draw.circle(win,white,(x+45,y+15),5)
        pygame.draw.circle(win,white,(x+15,y+45),5)
        pygame.draw.circle(win,white,(x+15,y+15),5)
        pygame.draw.circle(win,white,(x+45,y+45),5)
        pygame.draw.circle(win,white,(x+45,y+30),5)
        pygame.draw.circle(win,white,(x+15,y+30),5)



#############################################################     CLASSES     ###################################################################
        
#########################################################    EXCEPTIONS           #############################################################

#####   WHEN NO PIECE IS MOVABLE  ########
class NoMove(Exception):

    def __init__(self):
        errorSound.play()
        self.msg = "You cannot make a move!"
        
#####   WHEN THREE CONSECUTIVE SIXES  #######        
class ThreeSixes(Exception):

    def __init__(self):
        errorSound.play()
        self.msg = "You got three consecutive sixes!"


###############         ABSTRACT CLASS FOR PLAYER           #############
class Player(metaclass=ABCMeta):
    
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.threeSix = False
        self.noMove = False
        self.currentNo = 0
        self.Count = []
        self.Bonus = False
        self.BonusCount = []
        self.steps = 0
        self.win = False
        self.position = first
        self.pieces = {1:self.p1,2:self.p2,3:self.p3,4:self.p4}
        if not self.name:
            self.p1.home = True
            self.p2.home = True
            self.p3.home = True
            self.p4.home = True
            self.win = True
            
####################           ROLLING DICE          ###################
    def turn(self):
        global Dice
        global diceCD
        
        try:
            if diceCD == 0:
                if keys[pygame.K_SPACE]:
                    diceSound.play()
                    diceCD += 1
                    self.currentNo = random.randint(1,6)
                    self.Count = self.Count+[self.currentNo]
                    if not self.Bonus:
                        if len(self.Count) >= 3:
                            if self.Count[-1]==6 and self.Count[-2]==6 and self.Count[-3]==6:
                                raise ThreeSixes()
                    else:
                        self.BonusCount = self.BonusCount+[self.currentNo]
                        if len(self.BonusCount) >= 3:
                            if self.BonusCount[-1]==6 and self.BonusCount[-2]==6 and self.BonusCount[-3]==6:
                                raise ThreeSixes()
                    if self.currentNo != 6:
                        move = 0
                        for num in self.Count:
                            if num != 6:
                                if not self.p1.active or self.p1.home or self.p1.steps+num > 56:
                                    if not self.p2.active or self.p2.home or self.p2.steps+num > 56:
                                        if not self.p3.active or self.p3.home or self.p3.steps+num > 56:
                                            if not self.p4.active or self.p4.home or self.p4.steps+num > 56:
                                                move += 1
                            else:
                                if self.p1.home or self.p1.steps+num > 56:
                                    if self.p2.home or self.p2.steps+num > 56:
                                        if self.p3.home or self.p3.steps+num > 56:
                                            if self.p4.home or self.p4.steps+num > 56:
                                                move += 1
                        if move == len(self.Count):
                            raise NoMove()
                        Dice=False
                        diceCD = 0
                        
            elif diceCD < 4:
                diceCD += 1
            else:
                diceCD = 0
                
        except NoMove:
            self.noMove = True
            
        except ThreeSixes:
            self.threeSix = True
            changeTurn()
            
##################################    TO MOVE PIECE AFTER DICE ROLL     ######################################                
    @abstractmethod
    def move(self):
        global Dice
        global diceChoice
        global pieceChoice
        global arrow
        global moveCD
            
        if not Dice:
            if moveCD == 0:
                if diceChoice:
                    if keys[pygame.K_RETURN]:
                        moveCD += 1
                        if not self.Count:
                            pass
                        elif arrow == 350:
                            self.steps = self.Count[0]
                        elif arrow == 280:
                            self.steps = self.Count[1]
                        elif arrow == 420:
                            self.steps = self.Count[2]
                        elif arrow == 210:
                            self.steps = self.Count[3]
                        elif arrow == 490:
                            self.steps = self.Count[4]
                        elif arrow == 140:
                            self.steps = self.Count[5]
                        elif arrow == 560:
                            self.steps = self.Count[6]
                        
                        try:
                            if self.steps != 6:
                                    if not self.p1.active or self.p1.home or self.p1.steps+self.steps > 56:
                                        if not self.p2.active or self.p2.home or self.p2.steps+self.steps > 56:
                                            if not self.p3.active or self.p3.home or self.p3.steps+self.steps > 56:
                                                if not self.p4.active or self.p4.home or self.p4.steps+self.steps > 56:
                                                    raise NoMove()
                            else:
                                    if self.p1.home or self.p1.steps+self.steps > 56:
                                        if self.p2.home or self.p2.steps+self.steps > 56:
                                            if self.p3.home or self.p3.steps+self.steps > 56:
                                                if self.p4.home or self.p4.steps+self.steps > 56:
                                                    raise NoMove()
                            diceChoice = False
                            if pieceChoice == 1:
                                if not self.p1.active and self.steps != 6:
                                    if self.p2.active and not self.p2.home and self.p2.steps+self.steps <= 56:
                                        pieceChoice = 2
                                    elif self.p3.active and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                    elif self.p4.active and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    else:
                                        raise NoMove()
                                elif self.p1.home or self.p1.steps+self.steps > 56:
                                    if (self.p2.active or self.steps == 6) and not self.p2.home and self.p2.steps+self.steps <= 56:
                                        pieceChoice = 2
                                    elif (self.p3.active or self.steps == 6) and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                    elif (self.p4.active or self.steps == 6) and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    else:
                                        raise NoMove()

                            elif pieceChoice == 2:
                                if not self.p2.active and self.steps != 6:
                                    if self.p3.active and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                    elif self.p4.active and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    elif self.p1.active and not self.p1.home and self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    else:
                                        raise NoMove()
                                elif self.p2.home or self.p2.steps+self.steps > 56:
                                    if (self.p3.active or self.steps == 6) and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                    elif (self.p4.active or self.steps == 6) and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    elif (self.p1.active or self.steps == 6) and not self.p1.home and self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    else:
                                        raise NoMove()

                            elif pieceChoice == 3:
                                if not self.p3.active and self.steps != 6:
                                    if self.p4.active and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    elif self.p1.active and not self.p1.home and self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    elif self.p2.active and not self.p2.home and self.p2.steps+self.steps <= 56:
                                        pieceChoice = 2
                                    else:
                                        raise NoMove()
                                elif self.p3.home or self.p3.steps+self.steps > 56:
                                    if (self.p4.active or self.steps == 6) and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    elif (self.p1.active or self.steps == 6) and not self.p1.home and self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    elif (self.p2.active or self.steps == 6) and not self.p2.home and self.p2.steps+self.steps <= 56:
                                        pieceChoice = 2
                                    else:
                                        raise NoMove()

                            elif pieceChoice == 4:
                                if not self.p4.active and self.steps != 6:
                                    if self.p1.active and not self.p1.home and self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    elif self.p2.active and not self.p2.home and self.p2.steps+self.steps <= 56:
                                        pieceChoice = 2
                                    elif self.p3.active and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                    else:
                                        raise NoMove()
                                elif self.p4.home or self.p4.steps+self.steps > 56:
                                    if (self.p1.active or self.steps == 6) and not self.p1.home and self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    elif (self.p2.active or self.steps == 6) and not self.p2.home and self.p2.steps+self.steps <= 56:
                                        pieceChoice = 2
                                    elif (self.p3.active or self.steps == 6) and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                    else:
                                        raise NoMove()

                        except NoMove:
                            self.noMove = True
                            diceChoice = True

                                    

                else:                        

                    if keys[pygame.K_DOWN]:
                        moveCD += 1
                        if  pieceChoice == 1:
                            if (self.steps == 6 or self.p2.active) and self.p2.steps+self.steps <= 56 and not self.p2.home:
                                    pieceChoice = 2
                            else:
                                if self.p3.active and not self.p3.home and self.p3.steps+self.steps <= 56:
                                        pieceChoice = 3
                                elif self.p4.active and not self.p4.home:
                                    if self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                    
                        elif  pieceChoice == 2:
                            if (self.steps == 6 or self.p3.active) and self.p3.steps+self.steps <= 56 and not self.p3.home:
                                    pieceChoice = 3
                            else:
                                if self.p4.active and not self.p4.home and self.p4.steps+self.steps <= 56:
                                        pieceChoice = 4
                                elif self.p1.active and not self.p1.home:
                                    if self.p1.steps+self.steps <= 56:
                                        pieceChoice = 1
                                    
                        elif  pieceChoice == 3:
                            if (self.steps == 6 or self.p4.active) and self.p4.steps+self.steps <= 56 and not self.p4.home:
                                    pieceChoice = 4
                            else:
                                if self.p1.active and self.p1.steps+self.steps <= 56 and not self.p1.home:
                                        pieceChoice = 1
                                elif self.p2.active:
                                    if self.p2.steps+self.steps <= 56 and not self.p2.home:
                                        pieceChoice = 2
                                    
                        else:
                            if (self.steps == 6 or self.p1.active) and self.p1.steps+self.steps <= 56 and not self.p1.home:
                                    pieceChoice = 1
                            else:
                                if self.p2.active and self.p2.steps+self.steps <= 56 and not self.p2.home:
                                        pieceChoice = 2
                                elif self.p3.active:
                                    if self.p3.steps+self.steps <= 56 and not self.p3.home:
                                        pieceChoice = 3
                                    
                    elif keys[pygame.K_UP]:
                        moveCD += 1
                        if  pieceChoice == 1:
                            if (self.steps == 6 or self.p4.active) and self.p4.steps+self.steps <= 56 and not self.p4.home:
                                    pieceChoice = 4
                            else:
                                if self.p3.active and self.p3.steps+self.steps <= 56 and not self.p3.home:
                                        pieceChoice = 3
                                elif self.p2.active:
                                    if self.p2.steps+self.steps <= 56 and not self.p2.home: 
                                        pieceChoice = 2
                                    
                        elif  pieceChoice == 2:
                            if (self.steps == 6 or self.p1.active) and self.p1.steps+self.steps <= 56 and not self.p1.home:
                                    pieceChoice = 1
                            else:
                                if self.p4.active and self.p4.steps+self.steps <= 56 and not self.p4.home:
                                        pieceChoice = 4
                                elif self.p3.active:
                                    if self.p3.steps+self.steps <= 56 and not self.p3.home:
                                        pieceChoice = 3
                                    
                        elif  pieceChoice == 3:
                            if (self.steps == 6 or self.p2.active) and self.p2.steps+self.steps <= 56 and not self.p2.home:
                                    pieceChoice = 2
                            else:
                                if self.p1.active and self.p1.steps+self.steps <= 56 and not self.p1.home:
                                        pieceChoice = 1
                                elif self.p4.active:
                                    if self.p4.steps+self.steps <= 56 and not self.p4.home:
                                        pieceChoice = 4
                                    
                        else:
                            if (self.steps == 6 or self.p3.active) and self.p3.steps+self.steps <= 56 and not self.p3.home:
                                    pieceChoice = 3
                            else:
                                if self.p2.active and self.p2.steps+self.steps <= 56 and not self.p2.home:
                                        pieceChoice = 2
                                elif self.p1.active:
                                    if self.p1.steps+self.steps <= 56 and not self.p1.home:
                                        pieceChoice = 1

            elif moveCD < 2:
                moveCD += 1
            else:
                moveCD = 0

                                           
                                
##################################  PIECE CLASS  ########################################
                                    
class Piece:

    def __init__(self,color,number,startx,starty,x,y):
        self.color=color
        self.number=number
        self.active=False
        self.double=False
        self.home=False
        self.stop=True
        self.startx=startx
        self.starty=starty
        self.initialx = x
        self.initialy = y
        self.x=x
        self.y=y
        self.steps = 0

##########################    WHEN PIECE KILLS ANOTHER PIECE     #######################
    def kill(self,victim):
        global killSound
        killSound.play()
        victim.active = False
        victim.steps = 0
        victim.stop = True
        victim.x = victim.initialx
        victim.y = victim.initialy
        

####################################                  TO DRAW PIECE              ######################################
    def draw(self,x,y):
        pygame.draw.circle(win,self.color,(x,y),18)
        pygame.draw.circle(win,black,(x,y),18,2)
        if self.number == 1:
            win.blit(textOne,(x-5,y-10))
        elif self.number == 2:
            win.blit(textTwo,(x-5,y-11))
        elif self.number == 3:
            win.blit(textThree,(x-5,y-10))
        else:
            win.blit(textFour,(x-6,y-11))


#######################################           RED PLAYER CLASS           ########################################################
            
class Red(Player):

    def __init__(self,name):
        self.color = red
        self.p1=Piece(self.color,1,175,125,160,310)
        self.p2=Piece(self.color,2,265,125,160,310)
        self.p3=Piece(self.color,3,175,215,160,310)
        self.p4=Piece(self.color,4,265,215,160,310)
        super().__init__(name,red)
        
        
    def move(self):
        global diceChoice
        global pieceChoice
        global Dice
        global pieces
        global moveCD
        
        pop = False       
        if not diceChoice:
            if moveCD == 0:
                if keys[pygame.K_RETURN]:
                    for num in self.pieces:
                        if pieceChoice == num:                        
                            if not self.pieces[num].active:
                                self.pieces[num].active = True
                            else:
                                for step in range(self.steps):
                                    
                                    if self.pieces[num].steps in range(0,4):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps == 4:
                                        self.pieces[num].x += 40
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(5,10):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(10,12):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(12,17):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps == 17:
                                        self.pieces[num].x += 40
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(18,23):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(23,25):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(25,30):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps == 30:
                                        self.pieces[num].x -= 40
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(31,36):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(36,38):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(38,43):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps == 43:
                                        self.pieces[num].y -= 40
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(44,49):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps == 49:
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(50,55):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps == 55:
                                        self.pieces[num].home = True
                                        
                                        Dice = True
                                        self.BonusCount = []
                                        self.Bonus = True
                                        self.currentNo = 0
                                        home = True
                                        
                                        for piece in self.pieces:
                                            if not self.pieces[piece].home:
                                                home = False
                                        if home:
                                            self.win = True
                                            
                                    self.pieces[num].steps += 1

                                self.pieces[num].double = False
                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color == piece.color and self.pieces[num].number != piece.number:                                            
                                            self.pieces[num].double = True
                                            piece.double = True
                                            

                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color != piece.color:
                                            if not piece.stop:
                                                if not piece.double or self.pieces[num].double:
                                                    self.pieces[num].kill(piece)
                                                    Dice = True
                                                    self.BonusCount = []
                                                    self.Bonus = True
                                                    self.currentNo = 0
                                                    

                                for piece in pieces:
                                    if piece.double:
                                        double = False
                                        for Piece in pieces:
                                            if Piece.x == piece.x and Piece.y == piece.y:
                                                if Piece.color == piece.color and Piece.number != piece.number:
                                                    double = True
                                                    
                                        if not double:
                                            piece.double = False
                                            for Piece in pieces:
                                                if Piece.x == piece.x and Piece.y == piece.y:
                                                    if Piece.color != piece.color:
                                                        if not piece.stop:
                                                            Piece.kill(piece)


                            moveSound.play()
                                    
                            if self.pieces[num].steps in [0,8,13,21,26,34,39,47,51,52,53,54,55]:
                                self.pieces[num].stop = True
                            else:
                                self.pieces[num].stop = False
                                
                            pop = True

                            
        super().move() 
        
        if pop:
            i = 0
            for no in self.Count:
                if self.steps == no:
                    index = i
                i+=1
            self.Count = self.Count[:index]+self.Count[index+1:]
            pop = False
            if not self.Count:
                if not Dice:
                    changeTurn()
                else:
                    diceChoice = True
            else:
                diceChoice = True

        if not Dice:
            if self.Count:
                try:
                    move = 0
                    for num in self.Count:
                        if num != 6:
                            if not self.p1.active or self.p1.home or self.p1.steps+num > 56:
                                if not self.p2.active or self.p2.home or self.p2.steps+num > 56:
                                    if not self.p3.active or self.p3.home or self.p3.steps+num > 56:
                                        if not self.p4.active or self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                        else:
                            if self.p1.home or self.p1.steps+num > 56:
                                if self.p2.home or self.p2.steps+num > 56:
                                    if self.p3.home or self.p3.steps+num > 56:
                                        if self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                    if move == len(self.Count):
                        Dice = True
                        raise NoMove()
                    
                except NoMove:
                    self.noMove = True

                
####################################        GREEN PLAYER CLASS             #########################################
                
class Green(Player):

    def __init__(self,name):
        self.color = green
        self.p1=Piece(self.color,1,175,485,360,590)
        self.p2=Piece(self.color,2,265,485,360,590)
        self.p3=Piece(self.color,3,175,575,360,590)
        self.p4=Piece(self.color,4,265,575,360,590)
        super().__init__(name,green)
        
        
    def move(self):
        global diceChoice
        global pieceChoice
        global Dice
        global pieces
        global moveCD
        
        pop = False
        if not diceChoice:
            if moveCD == 0:
                if keys[pygame.K_RETURN]:
                    for num in self.pieces:
                        if pieceChoice == num:
                            if not self.pieces[num].active:
                                self.pieces[num].active = True
                            else:
                                for step in range(self.steps):
                                    
                                    if self.pieces[num].steps in range(0,4):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps == 4:
                                        self.pieces[num].x -= 40
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(5,10):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(10,12):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(12,17):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps == 17:
                                        self.pieces[num].x += 40
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(18,23):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(23,25):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(25,30):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps == 30:
                                        self.pieces[num].x += 40
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(31,36):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(36,38):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(38,43):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps == 43:
                                        self.pieces[num].y += 40
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(44,49):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps == 49:
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(50,55):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps == 55:
                                        self.pieces[num].home = True
                                        
                                        Dice = True
                                        self.BonusCount = []
                                        self.Bonus = True
                                        self.currentNo = 0
                                        home = True
                                        
                                        for piece in self.pieces:
                                            if not self.pieces[piece].home:
                                                home = False
                                        if home:
                                            self.win = True
                                            
                                    self.pieces[num].steps += 1

                                self.pieces[num].double = False
                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color == piece.color and self.pieces[num].number != piece.number:                                            
                                            self.pieces[num].double = True
                                            piece.double = True


                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color != piece.color:
                                            if not piece.stop:
                                                if not piece.double or self.pieces[num].double:
                                                    self.pieces[num].kill(piece)
                                                    Dice = True
                                                    self.BonusCount = []
                                                    self.Bonus = True
                                                    self.currentNo = 0
                                                    

                                for piece in pieces:
                                    if piece.double:
                                        double = False
                                        for Piece in pieces:
                                            if Piece.x == piece.x and Piece.y == piece.y:
                                                if Piece.color == piece.color and Piece.number != piece.number:
                                                    double = True
                                                    
                                        if not double:
                                            piece.double = False
                                            for Piece in pieces:
                                                if Piece.x == piece.x and Piece.y == piece.y:
                                                    if Piece.color != piece.color:
                                                        if not piece.stop:
                                                            Piece.kill(piece)



                            moveSound.play()
                                                
                            if self.pieces[num].steps in [0,8,13,21,26,34,39,47,51,52,53,54,55]:
                                self.pieces[num].stop = True
                            else:
                                self.pieces[num].stop = False
                                
                            pop = True
                        
        super().move() 
       
        if pop:
            i = 0
            for no in self.Count:
                if self.steps == no:
                    index = i
                i+=1
            self.Count = self.Count[:index]+self.Count[index+1:]
            pop = False
            if not self.Count:
                if not Dice:
                    changeTurn()
                else:
                    diceChoice = True
            else:
                diceChoice = True

        if not Dice:
            if self.Count:
                try:
                    move = 0
                    for num in self.Count:
                        if num != 6:
                            if not self.p1.active or self.p1.home or self.p1.steps+num > 56:
                                if not self.p2.active or self.p2.home or self.p2.steps+num > 56:
                                    if not self.p3.active or self.p3.home or self.p3.steps+num > 56:
                                        if not self.p4.active or self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                        else:
                            if self.p1.home or self.p1.steps+num > 56:
                                if self.p2.home or self.p2.steps+num > 56:
                                    if self.p3.home or self.p3.steps+num > 56:
                                        if self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                    if move == len(self.Count):
                        Dice = True
                        raise NoMove()
                    
                except NoMove:
                    self.noMove = True
                
                            
#####################################        YELLOW PLAYER  CLASS           ######################################3
                
class Yellow(Player):

    def __init__(self,name):
        self.color = yellow
        self.p1=Piece(self.color,1,535,485,640,390)
        self.p2=Piece(self.color,2,625,485,640,390)
        self.p3=Piece(self.color,3,535,575,640,390)
        self.p4=Piece(self.color,4,625,575,640,390)
        super().__init__(name,yellow)
        

    def move(self):
        global diceChoice
        global pieceChoice
        global Dice
        global pieces
        global moveCD
        
        pop = False
        if not diceChoice:
            if moveCD == 0:
                if keys[pygame.K_RETURN]:
                    for num in self.pieces:
                        if pieceChoice == num:
                            if not self.pieces[num].active:
                                self.pieces[num].active = True
                            else:
                                for step in range(self.steps):
                                    
                                    if self.pieces[num].steps in range(0,4):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps == 4:
                                        self.pieces[num].x -= 40
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(5,10):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(10,12):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(12,17):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps == 17:
                                        self.pieces[num].x -= 40
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(18,23):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(23,25):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(25,30):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps == 30:
                                        self.pieces[num].x += 40
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(31,36):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(36,38):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(38,43):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps == 43:
                                        self.pieces[num].y += 40
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(44,49):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps == 49:
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(50,55):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps == 55:
                                        self.pieces[num].home = True
                                        
                                        Dice = True
                                        self.BonusCount = []
                                        self.Bonus = True
                                        self.currentNo = 0
                                        home = True
                                        
                                        for piece in self.pieces:
                                            if not self.pieces[piece].home:
                                                home = False
                                        if home:
                                            self.win = True
                                            
                                    self.pieces[num].steps += 1

                                self.pieces[num].double = False
                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color == piece.color and self.pieces[num].number != piece.number:                                            
                                            self.pieces[num].double = True
                                            piece.double = True


                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color != piece.color:
                                            if not piece.stop:
                                                if not piece.double or self.pieces[num].double:
                                                    self.pieces[num].kill(piece)
                                                    Dice = True
                                                    self.BonusCount = []
                                                    self.Bonus = True
                                                    self.currentNo = 0
                                                    

                                for piece in pieces:
                                    if piece.double:
                                        double = False
                                        for Piece in pieces:
                                            if Piece.x == piece.x and Piece.y == piece.y:
                                                if Piece.color == piece.color and Piece.number != piece.number:
                                                    double = True
                                                    
                                        if not double:
                                            piece.double = False
                                            for Piece in pieces:
                                                if Piece.x == piece.x and Piece.y == piece.y:
                                                    if Piece.color != piece.color:
                                                        if not piece.stop:
                                                            Piece.kill(piece)


                                                    
                            moveSound.play()
                                    
                            if self.pieces[num].steps in [0,8,13,21,26,34,39,47,51,52,53,54,55]:
                                self.pieces[num].stop = True
                            else:
                                self.pieces[num].stop = False
                                
                            pop = True
                            
        super().move() 
        
        if pop:
            i = 0
            for no in self.Count:
                if self.steps == no:
                    index = i
                i+=1
            self.Count = self.Count[:index]+self.Count[index+1:]
            pop = False
            if not self.Count:
                if not Dice:
                    changeTurn()
                else:
                    diceChoice = True
            else:
                diceChoice = True

        if not Dice:
            if self.Count:
                try:
                    move = 0
                    for num in self.Count:
                        if num != 6:
                            if not self.p1.active or self.p1.home or self.p1.steps+num > 56:
                                if not self.p2.active or self.p2.home or self.p2.steps+num > 56:
                                    if not self.p3.active or self.p3.home or self.p3.steps+num > 56:
                                        if not self.p4.active or self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                        else:
                            if self.p1.home or self.p1.steps+num > 56:
                                if self.p2.home or self.p2.steps+num > 56:
                                    if self.p3.home or self.p3.steps+num > 56:
                                        if self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                    if move == len(self.Count):
                        Dice = True
                        raise NoMove()
                    
                except NoMove:
                    self.noMove = True


########################################     BLUE PLAYER CLASS        #################################
                
class Blue(Player):

    def __init__(self,name):
        self.color = blue
        self.p1=Piece(self.color,1,535,125,440,110)
        self.p2=Piece(self.color,2,625,125,440,110)
        self.p3=Piece(self.color,3,535,215,440,110)
        self.p4=Piece(self.color,4,625,215,440,110)
        super().__init__(name,blue)
        
        
    def move(self):
        global diceChoice
        global pieceChoice
        global Dice
        global pieces
        global moveCD
        
        pop = False
        if not diceChoice:
            if moveCD == 0:
                if keys[pygame.K_RETURN]:
                    for num in self.pieces:
                        if pieceChoice == num:
                            if not self.pieces[num].active:
                                self.pieces[num].active = True
                            else:
                                for step in range(self.steps):
                                    
                                    if self.pieces[num].steps in range(0,4):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps == 4:
                                        self.pieces[num].x += 40
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(5,10):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(10,12):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(12,17):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps == 17:
                                        self.pieces[num].x -= 40
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(18,23):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps in range(23,25):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(25,30):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps == 30:
                                        self.pieces[num].x -= 40
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(31,36):
                                        self.pieces[num].x -= 40
                                    elif self.pieces[num].steps in range(36,38):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps in range(38,43):
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps == 43:
                                        self.pieces[num].y -= 40
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(44,49):
                                        self.pieces[num].y -= 40
                                    elif self.pieces[num].steps == 49:
                                        self.pieces[num].x += 40
                                    elif self.pieces[num].steps in range(50,55):
                                        self.pieces[num].y += 40
                                    elif self.pieces[num].steps == 55:
                                        self.pieces[num].home = True
                                        
                                        Dice = True
                                        self.BonusCount = []
                                        self.Bonus = True
                                        self.currentNo = 0
                                        home = True
                                        
                                        for piece in self.pieces:
                                            if not self.pieces[piece].home:
                                                home = False
                                        if home:
                                            self.win = True
                                            
                                    self.pieces[num].steps += 1

                                self.pieces[num].double = False
                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color == piece.color and self.pieces[num].number != piece.number:                                            
                                            self.pieces[num].double = True
                                            piece.double = True

                                for piece in pieces:
                                    if self.pieces[num].x == piece.x and self.pieces[num].y == piece.y:
                                        if self.pieces[num].color != piece.color:
                                            if not piece.stop:
                                                if not piece.double or self.pieces[num].double:
                                                    self.pieces[num].kill(piece)
                                                    Dice = True
                                                    self.BonusCount = []
                                                    self.Bonus = True
                                                    self.currentNo = 0
                                                    

                                for piece in pieces:
                                    if piece.double:
                                        double = False
                                        for Piece in pieces:
                                            if Piece.x == piece.x and Piece.y == piece.y:
                                                if Piece.color == piece.color and Piece.number != piece.number:
                                                    double = True
                                                    
                                        if not double:
                                            piece.double = False
                                            for Piece in pieces:
                                                if Piece.x == piece.x and Piece.y == piece.y:
                                                    if Piece.color != piece.color:
                                                        if not piece.stop:
                                                            Piece.kill(piece)


                                                    
                            moveSound.play()
                                    
                            if self.pieces[num].steps in [0,8,13,21,26,34,39,47,51,52,53,54,55]:
                                self.pieces[num].stop = True
                            else:
                                self.pieces[num].stop = False
                                
                            pop = True
                            
        super().move() 

        if pop:
            if len(self.Count) > 1:
                i = 0
                for no in self.Count:
                    if self.steps == no:
                        index = i
                    i+=1
                self.Count = self.Count[:index]+self.Count[index+1:]
            elif self.Count:
                self.Count = []
            pop = False
            if not self.Count:
                if not Dice:
                    changeTurn()
                else:
                    diceChoice = True
            else:
                diceChoice = True

        if not Dice:
            if self.Count:
                try:
                    move = 0
                    for num in self.Count:
                        if num != 6:
                            if not self.p1.active or self.p1.home or self.p1.steps+num > 56:
                                if not self.p2.active or self.p2.home or self.p2.steps+num > 56:
                                    if not self.p3.active or self.p3.home or self.p3.steps+num > 56:
                                        if not self.p4.active or self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                        else:
                            if self.p1.home or self.p1.steps+num > 56:
                                if self.p2.home or self.p2.steps+num > 56:
                                    if self.p3.home or self.p3.steps+num > 56:
                                        if self.p4.home or self.p4.steps+num > 56:
                                            move += 1
                    if move == len(self.Count):
                        Dice = True
                        raise NoMove()
                    
                except NoMove:
                    self.noMove = True
            
                    

clock = pygame.time.Clock()


#######################################################                MAIN LOOP              ###################################################

while run:
    clock.tick(7)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not play:

        if guide:
            if keys[pygame.K_ESCAPE]:
                buttonSound.play()
                guide = False
                inst = True

        elif keys[pygame.K_RETURN]:
            if start:
                buttonSound.play()
                start = False
                play = True
            elif inst:
                buttonSound.play()
                inst = False
                guide = True
            elif end:
                buttonSound.play()
                run = False

        elif keys[pygame.K_DOWN]:
            if start:
                start = False
                inst = True
            elif inst:
                inst = False
                end = True
            elif end:
                end = False
                start = True

        elif keys[pygame.K_UP]:
            if start:
                start = False
                end = True
            elif inst:
                inst = False
                start = True
            elif end:
                end = False
                inst = True

    else:
        if game:
            
            wins = 0
            for player in players:
                if player.win:
                    wins += 1
            if wins < 3:
                if Dice:
                    for color in colorPlayers:
                        if Turn == color:
                            if not colorPlayers[color].win:
                                colorPlayers[color].turn()
                            else:
                                changeTurn()
                    
                else:
                    for color in colorPlayers:
                        if Turn == color:
                            colorPlayers[color].move()
                            
            else:
                Dice = True

                if keys[pygame.K_RETURN]:
                    redName = ''
                    yellowName = ''
                    greenName = ''
                    blueName = ''
                    cd = 7
                    enter = 'red'
                    name = redName
                    Turn = 'Red'
                    Dice = True
                    tsCD = 10
                    nmCD = 10
                    run = True
                    play = False
                    start = True
                    inst = False
                    end = False
                    guide = False
                    game = False
                    diceChoice = True
                    diceCD = 0
                    allow = True
                    arrow = 350
                    pieceChoice = 1
                    redDone = False
                    greenDone = False
                    yellowDone = False
                    blueDone = False
                
                    
        else:
            if cd == 7:
                cd = 0
            else:
                cd += 1
            if cd < 4:
                if cd == 0:
                    name = name + '|'
            else:
                if cd == 4:
                    name = name[:-1]               
                
                    
            if keys[pygame.K_RETURN]:
                buttonSound.play()
                
                if enter == 'red':
                    name = greenName
                    enter = 'green'
                    redFont = font2.render(redName, 1, red)
                    playerRed = Red(redName)
                    
                elif enter == 'green':
                    name = yellowName
                    enter = 'yellow'
                    greenFont = font2.render(greenName, 1, red)
                    playerGreen = Green(greenName)
                    
                elif enter == 'yellow':
                    name = blueName
                    enter = 'blue'
                    yellowFont = font2.render(yellowName, 1, red)
                    playerYellow = Yellow(yellowName)
                    
                elif enter == 'blue':
                    game = True
                    blueFont = font2.render(blueName, 1, red)
                    playerBlue = Blue(blueName)
                    
                    players = [playerRed,playerGreen,playerYellow,playerBlue]
                    colorPlayers = {'Red':playerRed, 'Green':playerGreen, 'Yellow':playerYellow, 'Blue':playerBlue}
                    pieces = [playerRed.p1,playerRed.p2,playerRed.p3,playerRed.p4,playerGreen.p1,playerGreen.p2,playerGreen.p3,playerGreen.p4,playerYellow.p1,playerYellow.p2,playerYellow.p3,playerYellow.p4,playerBlue.p1,playerBlue.p2,playerBlue.p3,playerBlue.p4]

            elif keys[pygame.K_BACKSPACE]:
                        typeSound.play()
                        
                        if enter == 'red':
                            redName = redName[:-1]
                            if cd < 4:
                                name = redName + '|'
                            else:
                                name = redName
                                
                        elif enter == 'green':
                            greenName = greenName[:-1]
                            if cd < 4:
                                name = greenName + '|'
                            else:
                                name = greenName
                                
                        elif enter == 'yellow':
                            yellowName = yellowName[:-1]
                            if cd < 4:
                                name = yellowName + '|'
                            else:
                                name = yellowName
                                
                        elif enter == 'blue':
                            blueName = blueName[:-1]
                            if cd < 4:
                                name = blueName + '|'
                            else:
                                name = blueName

            else:
                for x in abc:
                    if keys[x]:
                        typeSound.play()
                        
                        if enter == 'red':
                            redName = redName + abc[x]
                            if cd < 4:
                                name = redName + '|'
                            else:
                                name = redName
                                
                        elif enter == 'green':
                            greenName = greenName + abc[x]
                            if cd < 4:
                                name = greenName + '|'
                            else:
                                name = greenName
                                
                        elif enter == 'yellow':
                            yellowName = yellowName + abc[x]
                            if cd < 4:
                                name = yellowName + '|'
                            else:
                                name = yellowName
                                
                        elif enter == 'blue':
                            blueName = blueName + abc[x]
                            if cd < 4:
                                name = blueName + '|'
                            else:
                                name = blueName

    winDraw()

pygame.quit()
