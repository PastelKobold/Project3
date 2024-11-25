from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFilter

#Gavin Catron and Sarah Webster

#Check win conditions
def checkWin():
    #Check for range
    #Left, Right, Up, Diagonal
    for x in range(cols):
        for y in range(rows):
            if (x < 4):
                if(arr[x][y]['text']==arr[x+1][y]['text']==arr[x+2][y]['text']==arr[x+3][y]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            if (y < 4):
                if(arr[x][y]['text']==arr[x][y+1]['text']==arr[x][y+2]['text']==arr[x][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            #Diagonals
            if ((x < 7 and x > 4 and y < 4)):
                if(arr[x][y]['text']==arr[x-1][y+1]['text']==arr[x-2][y+2]['text']==arr[x-3][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")

            if (x > 4  and (x < 7 and y < 7)):
                if((arr[x][y]['text']==arr[x-1][y-1]['text']==arr[x-2][y-2]['text']==arr[x-3][y-3]['text']) and arr[x][y]['text']!= '' and  (not x-3 < 0) and (not y-3 < 0)):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            
#Function to handle when player clicks a button.
def press(x,y):
    global player
    global red_photo
    global yellow_photo
    if (winLbl['text'] != "Yellow Wins!" and winLbl['text'] != "Red Wins!"):
        if (arr[x][y] == arr[6][y]):
            if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
                arr[x][y].config(text = player)
                if player == "Red":
                    arr[x][y].config(image=red_photo)
                    player = "Yellow"
                    playerturn.config(text = "Yellow's turn")
                    showturn.config(image=yellow_photo)
                else:
                    arr[x][y].config(image=yellow_photo)
                    player = "Red"
                    playerturn.config(text = "Red's turn")
                    showturn.config(image=red_photo)
                checkWin()
        elif (arr[x+1][y]['text'] == "Red" or arr[x+1][y]['text'] == "Yellow"):
            if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
                arr[x][y].config(text = player)
                if player == "Red":
                    arr[x][y].config(image=red_photo)
                    player = "Yellow"
                    playerturn.config(text = "Yellow's turn")
                    showturn.config(image=yellow_photo)
                else:
                    arr[x][y].config(image=yellow_photo)
                    player = "Red"
                    playerturn.config(text = "Red's turn")
                    showturn.config(image=red_photo)
                checkWin()

#Help button that explains game
def help():
    messagebox.showinfo("Game instructions","Players choose yellow or red discs. They drop the discs into the grid, starting in the middle or at the edge to stack their colored discs upwards, horizontally, or diagonally. Use strategy to block opponents while aiming to be the first player to get 4 in a row to win.")

#Resets game
def resetB(arr):
    global photo
    for x in range(cols):
        for y in range(rows):
            arr[x][y].config(image = photo)
            arr[x][y].config(text = '')
            winLbl.config(text = '')

root = Tk()
root.geometry('300x300')
#Make player
player = "Red"
#Loading colors for game
photo = PhotoImage(file = "Empty.png")
red_photo = PhotoImage(file = "Red.png")
yellow_photo = PhotoImage(file = "Yellow.png")
#Creating game grid
rows, cols = (7, 7)
arr = [[0 for y in range(cols)] for x in range(rows)]
for x in range(cols):
    for y in range(rows):
        arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) , height = 30, width = 30, image=photo)
        arr[x][y].grid(row = x, column = y)

#Creating buttons
showturn = Button(root, text='', height = 30, width = 30, image=red_photo)
showturn.grid(row = 8, column = 11)

info = Button(root, text="Help",  command = lambda: help(), height = 3, width = 10)
info.grid(row = 27, column=1,columnspan=4)

reset = Button(root, text = "Reset", command = lambda: resetB(arr), height = 3, width = 10)
reset.grid(row = 25, column = 1, columnspan=4)

winLbl = Label(root)
playerturn = Label(root, text="Red starts")

winLbl.grid(row = 8, column = 2, columnspan=3)
playerturn.grid(row = 11, column=2, columnspan=3)


root.mainloop()