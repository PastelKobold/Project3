from tkinter import *

def checkWin():
    #Check for range
    #Left, Right, Up, Diagonal
    for x in range(cols):
        for y in range(rows):
            if(arr[x][y]['text']==arr[x+1][y]['text']==arr[x+2][y]['text']==arr[x+3][y]['text'] and arr[x][y]['text']!= ''):
               winLbl.config(text = "You Win!")
            if(arr[x][y]['text']==arr[x][y+1]['text']==arr[x][y+2]['text']==arr[x][y+3]['text'] and arr[x][y]['text']!= ''):
               winLbl.config(text = "You Win!")

def press(x,y):
    global player
    arr[x][y].config(text = player)
    if player == "Red":
        player = "Yellow"
    else:
        player = "Red"
    checkWin()

# def resetB():
#     btn1.config(text = '')
#     btn2.config(text = '')
#     btn3.config(text = '')
#     btn4.config(text = '')
#     btn5.config(text = '')
#     btn6.config(text = '')
#     btn7.config(text = '')
#     btn8.config(text = '')
#     btn9.config(text = '')

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

root.mainloop()