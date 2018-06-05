#Matt Westelman
#5/23/18
#goL.py- Conway's game of life

from ggame import *

def buildBoard(): #the blank matrix, will be edited when you click
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    return(board)

def redrawAll(): #makes the board, sprites both dead and live ones
    for item in App().spritelist[:]:
        item.destroy()
    Sprite(text,(0,300))
    for i in range(10): #a row of boxes!
        for j in range(10): #Columns of boxes!
            if data["board"][i][j]==0:
                Sprite(deadSquare,((30)*i,(30)*j))
            else:
                Sprite(liveSquare,((30)*i,(30)*j))

def numNeighbors(r,c): #Determines how many neighbors a cell has
    live = 0
    if r != 0 and c != 0 and data["board"][r-1][c-1]==1:
        live +=1
    if r != 0 and data["board"][r-1][c]==1:
        live +=1
    if r != 0 and c != 9 and data["board"][r-1][c+1]==1:
        live +=1
    if c != 0 and data["board"][r][c-1]==1:
        live +=1
    if c != 9 and data["board"][r][c+1]==1:
        live +=1
    if r != 9 and c != 0 and data["board"][r+1][c-1]==1:
        live +=1
    if r != 9 and data["board"][r+1][c]==1:
        live +=1
    if r != 9 and c != 9 and data["board"][r+1][c+1]==1:
        live +=1
    return(live) 

def nextGen(): #Moves to the next generation, killing and reviving whichever cells fit the requirements. Brutal.
    new = buildBoard()
    for r in range(10): #a row of boxes!
        for c in range(10): #Columns of boxes!
            num = numNeighbors(r,c)
            if new[r][c]== 0 and num == 3: #Determines life
                new[r][c]=1
            elif new[r][c]==1 and num <= 1 or num >= 4: #Determines death
                new[r][c]=0
            elif new[r][c]== 1 and num == 3 or num ==2: #Determines survival
                new[r][c]=1
    data["board"] = new
    redrawAll()

            
def mouseClick(event): #makes the mouse click function
    xBox = event.x//30
    yBox = event.y//30
    if event.y >= 300: #clicking near next gen will advance it
        nextGen()
    else: #changes a cell to live or dead
        if data["board"][xBox][yBox] == 0: 
            data["board"][xBox][yBox] = 1
        elif data["board"][xBox][yBox] == 1:
            data["board"][xBox][yBox] = 0
        redrawAll()
    

if __name__ == '__main__': # setup and runs game, just put all the def functions before

#Holds variables in a dictionary
    data = {}
    data["board"] = buildBoard() #The matrix


#colors for the color god
    green = Color(0x00FF00,1) #Green
    white = Color(0xFFFFFF,1) #white
    black = Color(0x000000,1) #Black
    
#Graphics for the graphic throne   
    deadSquare = RectangleAsset(30,30, LineStyle(1,white),black)
    liveSquare = RectangleAsset(30,30, LineStyle(1,black),green) #live/dead squares
    text = TextAsset("Next Gen",fill=black, style='bold 40pt Times') #Next gen
    

    redrawAll() #Delete sprites, and puts the ones it needs back on
    Sprite(text,(0,300))
    App().listenMouseEvent('click', mouseClick) 
    App().run()
