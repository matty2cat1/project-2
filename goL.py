#Matt Westelman
#5/23/18
#goL.py- Conway's game of life

from ggame import *

def buildBoard(): #the blank board
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    return(board)

def redrawAll():
    for i in range(10): #a row of boxes!
        for j in range(10): #Columns of boxes!
            Sprite(deadSquare,((30)*i,(30)*j)) #The grid, ripped straight from the dot grid program
            
def mouseClick(event):
    xBox = round(event.x-5,1)
    yBox = round(event.y-5,1)
    if board[xBox[yBox]] == 0:
        data["board"][xBox][yBox] = 1
    else:
        data["board"][xBox][yBox] = 0


    

if __name__ == '__main__': # setup and runs game, just put all the def functions before

#Holds variables in a dictionary
    data = {}
    data["board"] = buildBoard()


#colors for the color god
    green = Color(0x00FF00,1) #Green
    white = Color(0xFFFFFF,1) #white
    black = Color(0x000000,1) #Black
    
    
    deadSquare = RectangleAsset(30,30, LineStyle(1,black),white)
    liveSquare = RectangleAsset(30,30, LineStyle(1,white),black)
    redrawAll()
    App().listenMouseEvent('click', mouseClick) 
    App().run()