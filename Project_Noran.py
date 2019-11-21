#TIC TAC TOE GAME

import pygame
from tkinter import *  # tkinter package import
from tkinter import ttk
from tkinter import messagebox

#Global Variables
ActivePlayer=1
p1=[] #what player one selected
p2=[] #what player two selected


pygame.init() #initialize pygame so it runs
root = Tk()
root.title ("Tic Tac Toe") #pygame window name
root.resizable(0,0)
frame = Frame(root, width = 420, height=400) # This sets the boundries of the pygame screen
root.configure(bg="plum1")
myFont=("weight='bold'") #create a font object
#root.title
style = ttk.Style()
style.theme_use('classic')
#to play again
p1.clear()
p2.clear()

# Center form
def center_coordinates(self,i,j):
    icoord= j*self.box_size+(self.box_width)/2 - self.width/20
    jcoord= i*self.box_size+(self.box_height)/2 - self.height/20
    return(icoord,jcoord)


btn = StringVar()
click = True
def check(btn):
    global click
    if btn["text"] == " " and click == True:
        btn["text"] = "X"
        click = False
        scorekeeper()
    elif btn["text"] == " " and click == False:
        btn["text"] = "O"
        click = True
        scorekeeper()

laba = Label(root, text=" Player Vs Player ", relief="sunken", font="bold 18", bg="plum1", fg='pink4', width=13)
laba.grid(row=0, column=1)

p1 = IntVar()
p2 = IntVar()

laba1 = Label(root, text=" X :", relief="sunken", font="bold 12", bg="plum1", fg='pink4', padx=4, pady=4)
laba1.grid(row=0, column=0, sticky=W)
laba1 = Entry(root, textvariable= p1, relief="flat", font="bold 12", bg="plum1", fg='pink4', width=6)
laba1.grid(row=0, column=0)

laba2 = Label(root, text=" O :", relief="sunken", font="bold 12", bg="plum1", fg='pink4', padx=4, pady=4)
laba2.grid(row=4, column=2, sticky=W)
laba2 = Entry(root, textvariable= p2, relief="flat", font="bold 12", bg="plum1", fg='pink4', width=5)
laba2.grid(row=4, column=2)

p1.set(0)
p2.set(0)


def scorekeeper():
    if (bu1["text"] == "X" and bu2["text"] == "X" and bu3["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if  (bu4["text"] == "X" and bu5["text"] == "X" and bu6["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if (bu7["text"] == "X" and bu8["text"] == "X" and bu9["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if  (bu1["text"] == "X" and bu4["text"] == "X" and bu7["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if  (bu2["text"] == "X" and bu5["text"] == "X" and bu8["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if (bu3["text"] == "X" and bu6["text"] == "X" and bu9["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if  (bu1["text"] == "X" and bu5["text"] == "X" and bu9["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if (bu3["text"] == "X" and bu5["text"] == "X" and bu7["text"] == "X"):
        r = p1.get()
        score = (r + 1)
        p1.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")
        reset()
    if (bu1["text"] == "O" and bu2["text"] == "O" and bu3["text"] == "O"):
        r = p2.get()
        score = (r + 1)
        p2.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
        reset()
    if (bu4["text"] == "O" and bu5["text"] == "O" and bu6["text"] == "O"):
        r = p2.get()
        score = (r + 1)
        p2.set(score)
        messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
        reset()
    if (bu7["text"] == "O" and bu8["text"] == "O" and bu9["text"] == "O"):
       r = p2.get()
       score = (r + 1)
       p2.set(score)
       messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
       reset()
    if (bu1["text"] == "O" and bu4["text"] == "O" and bu7["text"] == "O"):
       r = p2.get()
       score = (r + 1)
       p2.set(score)
       messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
       reset()
    if (bu2["text"] == "O" and bu5["text"] == "O" and bu8["text"] == "O"):
       r = p2.get()
       score = (r + 1)
       p2.set(score)
       messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
    if (bu3["text"] == "O" and bu6["text"] == "O" and bu9["text"] == "O"):
       r = p2.get()
       score = (r + 1)
       p2.set(score)
       messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
       reset()
    if (bu1["text"] == "O" and bu5["text"] == "O" and bu9["text"] == "O"):
       r = p2.get()
       score = (r + 1)
       p2.set(score)
       messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
       reset()
    if (bu3["text"] == "O" and bu5["text"] == "O" and bu7["text"] == "O"):
       r = p2.get()
       score = (r + 1)
       p2.set(score)
       messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")
       reset()


#to restart game
def reset():
    bu1["text"] = " "
    bu2["text"] = " "
    bu3["text"] = " "
    bu4["text"] = " "
    bu5["text"] = " "
    bu6["text"] = " "
    bu7["text"] = " "
    bu8["text"] = " "
    bu9["text"] = " "


#Buttons close and play again
pagain= Button(root, text="  Play Again  ", relief="ridge", font="times 17", bg="pink4", fg='plum1', width=10,
               command=reset)
pagain.grid(row=4, column=1)

bclose= Button(root, text="  Exit  ", relief="ridge", font="times 17", bg="pink4", fg='plum1', width=10,
               command=root.destroy)
bclose.grid(row=4, column=0)


# Add Buttons
bu1 = ttk.Button(root,text=' ')
bu1.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu1.config(command=lambda: check(bu1))

bu2 = ttk.Button(root,text=' ')
bu2.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: check(bu2))

bu3 = ttk.Button(root,text=' ')
bu3.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: check(bu3))

bu4 = ttk.Button(root,text=' ')
bu4.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: check(bu4))

bu5 = ttk.Button(root,text=' ')
bu5.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: check(bu5))

bu6 = ttk.Button(root,text=' ')
bu6.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: check(bu6))

bu7 = ttk.Button(root,text=' ')
bu7.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: check(bu7))

bu8 = ttk.Button(root,text=' ')
bu8.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: check(bu8))

bu9 = ttk.Button(root,text='   ')
bu9.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: check(bu9))


root.mainloop()
