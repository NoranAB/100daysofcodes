import pygame
from tkinter import *  # tkinter package import
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from random import randint
import sys
#from Computer_AI import*
import random


def game():
    p1.clear()
    p2.clear()
#Global Variables
ActivePlayer=1
p1=[] #what player one selected
p2=[] #what player two selected
#AI=[] #Artifical Intellegence (Computer)


pygame.init() #initialize pygame so it runs
root = Tk()
root.title ("Tic Tac Toe") #pygame window name
root.resizable(0,0)
frame = Frame(root, width = 420, height=400) # This sets the boundries of the pygame screen
root.configure(bg="plum1")
myFont=("weight='bold'") #create a font object
#to play again
p1.clear()
p2.clear()

# Center form
def center_coordinates(self,i,j):
    icoord= j*self.box_size+(self.box_width)/2 - self.width/20
    jcoord= i*self.box_size+(self.box_height)/2 - self.height/20
    return(icoord,jcoord)

#root.title
style = ttk.Style()
style.theme_use('classic')



def reset():
    bu1["text"] = " "
    bu1.config(command=lambda: ButtonClick(1))
    bu2["text"] = " "
    bu2.config(command=lambda: ButtonClick(2))
    bu3["text"] = " "
    bu3.config(command=lambda: ButtonClick(3))
    bu4["text"] = " "
    bu4.config(command=lambda: ButtonClick(4))
    bu5["text"] = " "
    bu5.config(command=lambda: ButtonClick(5))
    bu6["text"] = " "
    bu6.config(command=lambda: ButtonClick(6))
    bu7["text"] = " "
    bu7.config(command=lambda: ButtonClick(7))
    bu8["text"] = " "
    bu8.config(command=lambda: ButtonClick(8))
    bu9["text"] = " "
    bu9.config(command=lambda: ButtonClick(9))
    pass


laba = Label(root, text=" Player Vs Player ", relief="sunken", font="bold 18", bg="plum1", fg='pink4', width=13)
laba.grid(row=0, column=1)

pagain= Button(root, text="  Play Again  ", relief="ridge", font="times 17", bg="pink4", fg='plum1', width=12, command=reset)
pagain.grid(row=4, column=1)

bclose= Button(root, text="  Exit  ", relief="ridge", font="times 17", bg="pink4", fg='plum1', width=12, command=root.destroy)
bclose.grid(row=4, column=0)

#def request():
btn1 = Button(root, text="  VS AI  ", relief="sunken", font="times 17", width=12, bg="pink4", fg='plum1',
              command=lambda: ButtonClick(AI))
btn1.grid(row=4, column=2)

#root.title
style = ttk.Style()
style.theme_use('classic')

#Add Buttons

btns = StringVar()
click = True
def check(btns):
    global click
    if btns["text"] == " " and click == True:
        btns["text"] = "p1"
        click = False
        #scorekeeper()
    elif btns["text"] == " " and click == False:
        btns["text"] = "p2"
        click = True
        #scorekeeper()


# Add Buttons
bu1 = ttk.Button(root,text=' ')
bu1.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu1.config(command=lambda: ButtonClick(1))

bu2 = ttk.Button(root,text=' ')
bu2.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: ButtonClick(2))

bu3 = ttk.Button(root,text=' ')
bu3.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: ButtonClick(3))

bu4 = ttk.Button(root,text=' ')
bu4.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5 = ttk.Button(root,text=' ')
bu5.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6 = ttk.Button(root,text=' ')
bu6.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7 = ttk.Button(root,text=' ')
bu7.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8 = ttk.Button(root,text=' ')
bu8.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9 = ttk.Button(root,text='   ')
bu9.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: ButtonClick(9))


#Activate buttons
def ButtonClick(id):
    print("ID:{}".format(id))
    global ActivePlayer
    global p1
    global p2
   #global AI
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        root.title("Tic Tac Toe :Player X")
        ActivePlayer=2
        print("p1:{}".format(p1))
        #AutoPlay() #AI

    elif(ActivePlayer==2):
        SetLayout(id, "O")
        p2.append(id)
        root.title("Tic Tac Toe :Player O")
        ActivePlayer=1
        print("p2:{}".format(p2))
    CheckWiner()


def SetLayout(id, PlayerSymbol):
    if id==1:
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])

    elif id==2:
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
        Winer = 1
    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winer = 2
    if((  4 in p1) and (5 in p1) and (6 in p1)):
        Winer = 1

    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winer = 2

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
        reset()
        game()

    elif Winer==2:
        messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
        reset()
        game()

    else:
    elif:
        if len(p1) == 5 and len(p2) ==4:
            messagebox.showinfo(title= "GAME OVER -_- " , message="Opps! There is No Winner.., Can you click Play again")
            #reset() #call to restart game


"""""  for X in range(0,len(root.but)):
         root.but[X].set(True)
         root.but[X].setText('')

    elif root.get()=='O':
     #QMessageBox.information(root. 'Tic Tac Toe', p2 is Win !', QMessageBox.ok)
         root.p2 = root.p2 +1
         root.p2O.setText(str(root.p2))
    for p1 in range(0,len(root.but)):
         root.but[X].setEnabled(True)
         root.but[X].setText('')
    elif root.oper() == 'all':

    for X in range(0,len(root.but)):
         root.but[X].setEnabled(True)
         root.but[X].setText('')
    elif:
        if root.game == 'p1':
           root.game = 'p2'
    elif root.game == 'p2':
         root.game = 'p1'" """


while CheckWiner():
    if 1<=choice<=9 and cell[choice-1] == ' ':
        reset()
#reset()
root.mainloop()


