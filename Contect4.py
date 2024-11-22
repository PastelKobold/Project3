from tkinter import *
from PIL import Image, ImageFilter

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
            if ((x < 7 and x > 4 and y < 4)):
                if(arr[x][y]['text']==arr[x-1][y+1]['text']==arr[x-2][y+2]['text']==arr[x-3][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")

            if ((x > 4 and y > 4) and (x < 7 and y < 7)):
                if(arr[x][y]['text']==arr[x-1][y-1]['text']==arr[x-2][y-2]['text']==arr[x-3][y-3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Red Wins!")
                    else:
                        playerturn.config(text = "Reset")
                        winLbl.config(text = "Yellow Wins!")
            

def press(x,y):
    global player
    global red_photo
    global yellow_photo
    #red_photo = PhotoImage(file = "Red.png")
    #yellow_photo = PhotoImage(file = "Yellow.png")
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

def resetB(arr):
    global photo
    for x in range(cols):
        for y in range(rows):
            arr[x][y].config(image = photo)
            arr[x][y].config(text = "")
            winLbl.config(text = "")

def resetB(arr):
    for x in range(cols):
        for y in range(rows):
            arr[x][y].config(image = '')

root = Tk()
root.geometry('300x300')
#Make player
player = "Red"
photo = PhotoImage(file = "Empty.png")
#global red_photo
red_photo = PhotoImage(file = "Red.png")
#global yellow_photo
yellow_photo = PhotoImage(file = "Yellow.png")
rows, cols = (7, 7)
arr = [[0 for y in range(cols)] for x in range(rows)]
for x in range(cols):
    for y in range(rows):
        arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) , height = 30, width = 30, image=photo)
        arr[x][y].grid(row = x, column = y)

showturn = Button(root, text='', height = 30, width = 30, image=red_photo)
showturn.grid(row = 8, column = 11)

reset = Button(root, text = "Reset", command = lambda: resetB(arr), height = 3, width = 10)
reset.grid(row = 25, column = 5, columnspan=4)
## Create Buttons
# btn1 = Button(root, text='', command= lambda: press(btn1), height = 3, width = 10)
# btn2 = Button(root, text='', command= lambda: press(btn2), height = 3, width = 10)
# btn3 = Button(root, text='', command= lambda: press(btn3), height = 3, width = 10)
# btn4 = Button(root, text='', command= lambda: press(btn4), height = 3, width = 10)
# btn5 = Button(root, text='', command= lambda: press(btn5), height = 3, width = 10)
# btn6 = Button(root, text='', command= lambda: press(btn6), height = 3, width = 10)
# btn7 = Button(root, text='', command= lambda: press(btn7), height = 3, width = 10)
# btn8 = Button(root, text='', command= lambda: press(btn8), height = 3, width = 10)
# btn9 = Button(root, text='', command= lambda: press(btn9), height = 3, width = 10)
# reset = Button(root, text = "reset", command = lambda: resetB(), height = 3, width = 10)

winLbl = Label(root)
playerturn = Label(root, text="Red starts")
## Layout Buttons
# btn1.grid(row = 1, column = 1)
# btn2.grid(row = 1, column = 2)
# btn3.grid(row = 1, column = 3)
# btn4.grid(row = 2, column = 1)
# btn5.grid(row = 2, column = 2)
# btn6.grid(row = 2, column = 3)
# btn7.grid(row = 3, column = 1)
# btn8.grid(row = 3, column = 2)
# btn9.grid(row = 3, column = 3)
# reset.grid(row = 5, column = 2)

winLbl.grid(row = 8, column = 2, columnspan=3)
playerturn.grid(row = 11, column=2, columnspan=3)


root.mainloop()