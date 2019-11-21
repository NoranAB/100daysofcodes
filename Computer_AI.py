#def greeting(AI):
#    print(AI)
#from gaming noran import *

import pygame
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
#from gaming noran import *
#def greeting(AI):

#root=Tk()
#button=ttk.Button(root,text='AI')
#button.pack()

#def buClick():
 #   root()
#button.config(command=buClick)
import pygame as p,random
def Computer_AI():
    q=p.display
    T=16
    b=q.set_mode([256]*2).fill
    l=[]
    d=a=x=1
    c=p.event.get
    while not(x&528 or x in l):
        l=l[a!=x:]+[x]
        while a&528 or a in l:
            a=random.randrange(512)
#def beginscreen():
        global game
        global turn
        turn = {'Player': 0, 'Computer': 0}
        game = Game()
        game.createboard()


#if 'btn1' in root:
 #   Computer_AI()
  #  '''open the game'''


# Global Variables
ActivePlayer = 1
p1 = []  # what player one selected
p2 = []  # Artifical Intellegence (Computer)


plum1 = 255, 187, 255
pygame.init()  # initialize pygame and our window

AI = Tk()
AI.resizable(0,0)
AI.title("Tic Tac Toe Player VS Computer")
width = 410
height = 400
frame = Frame(AI, width=410, height=400)
AI.configure(bg="plum1")
myFont = ("weight='bold'")


# Add Buttons
bu1 = ttk.Button(AI,text=' ')
bu1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
bu1.config(command=lambda: ButtonClick(1))

bu2 = ttk.Button(AI,text=' ')
bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: ButtonClick(2))

bu3 = ttk.Button(AI,text=' ')
bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: ButtonClick(3))

bu4 = ttk.Button(AI,text=' ')
bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5 = ttk.Button(AI,text=' ')
bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6 = ttk.Button(AI,text=' ')
bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7 = ttk.Button(AI,text=' ')
bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8 = ttk.Button(AI,text=' ')
bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9 = ttk.Button(AI,text='   ')
bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: ButtonClick(9))


# Activate buttons
def ButtonClick(id):
    print("ID:{}".format(id))
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        AI.title("Tic Tac Toe :Player X")
        ActivePlayer=2
        print("p1:{}".format(p1))
        AutoPlay()
    elif(ActivePlayer==2):
        SetLayout(id, "O")
        p2.append(id)
        AI.title("Tic Tac Toe :Computer O")
        ActivePlayer=1
        print("p2:{}".format(p2))
    CheckWiner()

def SetLayout(id, PlayerSymbol):
        if id == 1:
            bu1.config(text=PlayerSymbol)
            bu1.state(['disabled'])

        elif id == 2:
            bu2.config(text=PlayerSymbol)
            bu2.state(['disabled'])

        elif id == 3:
            bu3.config(text=PlayerSymbol)
            bu3.state(['disabled'])

        elif id == 4:
            bu4.config(text=PlayerSymbol)
            bu4.state(['disabled'])

        elif id == 5:
            bu5.config(text=PlayerSymbol)
            bu5.state(['disabled'])

        elif id == 6:
            bu6.config(text=PlayerSymbol)
            bu6.state(['disabled'])

        elif id == 7:
            bu7.config(text=PlayerSymbol)
            bu7.state(['disabled'])

        elif id == 8:
            bu8.config(text=PlayerSymbol)
            bu8.state(['disabled'])

        elif id == 9:
            bu9.config(text=PlayerSymbol)
            bu9.state(['disabled'])

def CheckWiner():
    Winer=-1
    if((  1 in p1) and (2 in p1) and (3 in p1)):
        Winer= 1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winer=2

    if((  4 in p1) and (5 in p1) and (6 in p1)):
        Winer=1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winer=2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winer = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winer=2

    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winer = 1
    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winer = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winer = 1
    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winer = 2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Winer = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winer = 2

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        Winer = 1
    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winer = 2

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winer = 1
    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winer = 2

    if Winer== 1:
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")

    elif Winer==2:
        messagebox.showinfo(title="CONGRATS ^_^", message="Computer O is the winer")



# When playing with Artifical Intellegance (Computer(AI))
def AutoPlay():
        global p1
        global p2
        EmptyCells = []
        for cell in range(9):  # الكمبيوتر يبحث عن الخلايا الغير مأخوذه
            if (not ((cell + 1 in p1) or (cell + 1 in p2))):
                EmptyCells.append(cell + 1)
        RandIndex = randint(0, len(EmptyCells) - 1)
        ButtonClick(EmptyCells[RandIndex])


#quit()
AI.mainloop()
