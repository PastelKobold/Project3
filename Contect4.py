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
                        winLbl.config(text = "Red Wins!")
                    else:
                        winLbl.config(text = "Yellow Wins!")
            if (y < 4):
                if(arr[x][y]['text']==arr[x][y+1]['text']==arr[x][y+2]['text']==arr[x][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        winLbl.config(text = "Red Wins!")
                    else:
                        winLbl.config(text = "Yellow Wins!")
            if (x < 4 and y < 4):
                if(arr[x][y]['text']==arr[x+1][y+1]['text']==arr[x+2][y+2]['text']==arr[x+3][y+3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        winLbl.config(text = "Red Wins!")
                    else:
                        winLbl.config(text = "Yellow Wins!")

            if ((x > 4 and y > 4) and (x < 7 and y < 7)):
                if(arr[x][y]['text']==arr[x-1][y-1]['text']==arr[x-2][y-2]['text']==arr[x-3][y-3]['text'] and arr[x][y]['text']!= ''):
                    if(arr[x][y]['text'] == "Red"):
                        winLbl.config(text = "Red Wins!")
                    else:
                        winLbl.config(text = "Yellow Wins!")
            

def press(x,y):
    global player
    red_photo = PhotoImage(file = "Red.png")
    yellow_photo = PhotoImage(file = "Yellow.png")
    if (arr[x][y] == arr[6][y]):
        if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
            # arr[x][y].config(text=player)
            if player == "Red":
                player = "Yellow"
                arr[x][y].config(image=yellow_photo)
            else:
                player = "Red"
                arr[x][y].config(image=red_photo)
            checkWin()
    elif (arr[x+1][y]['text'] == "Red" or arr[x+1][y]['text'] == "Yellow"):
        if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
            # arr[x][y].config(text = player)
            if player == "Red":
                player = "Yellow"
                arr[x][y].config(image=yellow_photo)
            else:
                player = "Red"
                arr[x][y].config(image=red_photo)
            checkWin()
        else:
            pass
    else:
        pass

def resetB(arr):
    for x in range(cols):
        for y in range(rows):
            arr[x][y].config(image = '')

root = Tk()
root.geometry('300x300')
#Make player
player = "Red"
photo = PhotoImage(file = "Empty.png")
rows, cols = (7, 7)
arr = [[0 for y in range(cols)] for x in range(rows)]
for x in range(cols):
    for y in range(rows):
        arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) ,image=photo)
        arr[x][y].grid(row = x, column = y)

winLbl = Label(root)
reset = Button(root, text = "Reset", command = lambda: resetB(arr), height = 3, width = 10)
reset.grid(row = 9, column = 3)

winLbl.grid(row = 8, column = 2, columnspan=3)

root.mainloop()