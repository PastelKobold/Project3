from tkinter import *

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
    if (arr[x][y] == arr[6][y]):
        if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
            arr[x][y].config(text = player)
            if player == "Red":
                player = "Yellow"
            else:
                player = "Red"
            checkWin()
    elif (arr[x+1][y]['text'] == "Red" or arr[x+1][y]['text'] == "Yellow"):
        if (arr[x][y]['text'] != "Red" and arr[x][y]['text'] != "Yellow"):
            arr[x][y].config(text = player)
            if player == "Red":
                player = "Yellow"
            else:
                player = "Red"
            checkWin()
        else:
            pass
    else:
        pass


root = Tk()
root.geometry('300x300')

#Make player
player = "Red"
rows, cols = (7, 7)
arr = [[0 for y in range(cols)] for x in range(rows)]
for x in range(cols):
    for y in range(rows):
        arr[x][y] = Button(root, text='', command= lambda x1=x, y1=y: press(x1,y1) , height = 3, width = 10)
        arr[x][y].grid(row = x, column = y)

winLbl = Label(root)

winLbl.grid(row = 8, column = 2, columnspan=3)

root.mainloop()