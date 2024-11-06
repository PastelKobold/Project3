from tkinter import *

def checkWin():
    winLbl.config(text = "You Win!")

def press(btn):
    global player
    btn.config(text = player)
    if player == "X":
        player = "O"
    else:
        player = "X"
    checkWin()

def resetB():
    btn1.config(text = '')
    btn2.config(text = '')
    btn3.config(text = '')
    btn4.config(text = '')
    btn5.config(text = '')
    btn6.config(text = '')
    btn7.config(text = '')
    btn8.config(text = '')
    btn9.config(text = '')

root = Tk()
root.geometry('300x300')

#Make player
player = "X"



#gggggggggggggggggggggggggggggg
#Small change

## Create Buttons
btn10 = Button(root, text='', command= lambda: press(btn1), height = 3, width = 10)
btn1 = Button(root, text='', command= lambda: press(btn1), height = 3, width = 10)
btn2 = Button(root, text='', command= lambda: press(btn2), height = 3, width = 10)
btn3 = Button(root, text='', command= lambda: press(btn3), height = 3, width = 10)
btn4 = Button(root, text='', command= lambda: press(btn4), height = 3, width = 10)
btn5 = Button(root, text='', command= lambda: press(btn5), height = 3, width = 10)
btn6 = Button(root, text='', command= lambda: press(btn6), height = 3, width = 10)
btn7 = Button(root, text='', command= lambda: press(btn7), height = 3, width = 10)
btn8 = Button(root, text='', command= lambda: press(btn8), height = 3, width = 10)
btn9 = Button(root, text='', command= lambda: press(btn9), height = 3, width = 10)
reset = Button(root, text = "reset", command = resetB(), height = 3, width = 10)

winLbl = Label(root)
## Layout Buttons
btn1.grid(row = 1, column = 1)
btn2.grid(row = 1, column = 2)
btn3.grid(row = 1, column = 3)
btn4.grid(row = 2, column = 1)
btn5.grid(row = 2, column = 2)
btn6.grid(row = 2, column = 3)
btn7.grid(row = 3, column = 1)
btn8.grid(row = 3, column = 2)
btn9.grid(row = 3, column = 3)
reset.grid(row = 5, column = 2)

winLbl.grid(row = 4, column = 1, columnspan=3)

root.mainloop()