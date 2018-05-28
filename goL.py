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
            Sprite(deadSquare,(10+(10+10)*i,10+(10+10)*j)) #The grid, ripped straight from the dot grid program

    

if __name__ == '__main__': # setup and runs game, just put all the def functions before

 data = {}

#colors for the color god
    green = Color(0x00FF00,1) #Green
    white = Color(0xFFFFFF,1) #white
    black = Color(0x000000,1) #Black
    
    buildBoard()
    deadSquare = RectangleAsset(30,30, LineStyle(1,white),black)
    liveSquare = RectangleAsset(30,30, LineStyle(1,white),green)
    redrawAll()
    App().run()