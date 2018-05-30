#Matt Westelman
#5/23/18
#goL.py- Conway's game of life

from ggame import *

def buildBoard(): #the blank board
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    return(board)

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for i in range(10): #a row of boxes!
        for j in range(10): #Columns of boxes!
            if data["board"][i][j]==0:
                Sprite(deadSquare,((30)*i,(30)*j))
            else:
                Sprite(liveSquare,((30)*i,(30)*j))

            
def mouseClick(event):
    xBox = event.x//30
    yBox = event.y//30
    if data["board"][xBox][yBox] == 0:
        data["board"][xBox][yBox] = 1
    else:
        data["board"][xBox][yBox] = 0
    redrawAll()

def numNeighbors(r,c):
    board[r][c]
    if board[r-1][c-1]==1:
        numNeighbors+=1
    if board[r-1][c]==1:
        numNeighbors+=1
    if board[r-1][c+1]==1:
        numNeighbors+=1
    if board[r][c-1]==1:
        numNeighbors+=1
    if board[r][c+1]==1:
        numNeighbors+=1
    if board[r+1][c-1]==1:
        numNeighbors+=1
    if board[r+1][c]==1:
        numNeighbors+=1
    if board[r+1][c+1]==1:
        numNeighbors+=1
    return(numNeighbors) 
        

if __name__ == '__main__': # setup and runs game, just put all the def functions before

#Holds variables in a dictionary
    data = {}
    data["board"] = buildBoard()


#colors for the color god
    green = Color(0x00FF00,1) #Green
    white = Color(0xFFFFFF,1) #white
    black = Color(0x000000,1) #Black
    
    
    deadSquare = RectangleAsset(30,30, LineStyle(1,white),black)
    liveSquare = RectangleAsset(30,30, LineStyle(1,black),green)
    redrawAll()
    App().listenMouseEvent('click', mouseClick) 
    App().run()