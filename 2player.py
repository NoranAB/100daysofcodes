import pygame
from tkinter import *
import tkinter
#rom tkinter.messagebox import


# alien_invasion.py
import sys
import pygame
#-------- Final Project "XO" --------
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Final Project of 'المبادرة السعودية للمطورين'")
root.geometry("1070x670+100+39")
root.configure(background = 'Cadet Blue')

#--------------- FRAME ---------------
Tops = Frame(root, bg='Cadet Blue', pady=2, width=1070, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial', 40, 'bold'), text="Tic Tac Toe Game", bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg='Powder Blue', bd=10, width=1250, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

#--------------- PLAYERS ---------------
"""p1 = IntVar()
p2 = IntVar()

p1X = Label(root, font=('arial', 30, 'bold'), text="Player X:", padx=2, pady=2, bg='Cadet Blue')
p1X.grid(row=0, column=0, sticky=W)
p1X = Entry(root, font=('arial', 30, 'bold'), bd=2, fg="black", textvariable=p1,
                width=9, justify=LEFT).grid(row=0, column=1)

p2O = Label(root, font=('arial', 30, 'bold'), text="Player O:", padx=2, pady=2, bg='Cadet Blue')
p2O.grid(row=1, column=0, sticky=W)
p2O = Entry(root, font=('arial', 30, 'bold'), bd=2, fg="black", textvariable=p2,
                width=9, justify=LEFT).grid(row=1, column=1)

p1.set(0)
p2.set(0)"""

#--------------- FUNCTIONS ---------------
buttons = StringVar()
click = True

def check(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

"""def scorekeeper():
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")
    if (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = playerX.get()
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "YOU'RE WINNER !!")

    if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="pink")
        button2.configure(background="pink")
        button3.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="pink")
        button5.configure(background="pink")
        button6.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="pink")
        button8.configure(background="pink")
        button9.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="pink")
        button4.configure(background="pink")
        button7.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="pink")
        button5.configure(background="pink")
        button8.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="pink")
        button6.configure(background="pink")
        button9.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="pink")
        button5.configure(background="pink")
        button9.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")
    if (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="pink")
        button5.configure(background="pink")
        button7.configure(background="pink")
        n = playerO.get()
        score = (n + 1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "YOU'RE WINNER !!")"""

def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")

def newGame():
    reset()
    playerX.set(0)
    playerO.set(0)

#--------------- BUTTONS ---------------
btnReset = Button(RightFrame2, text="Reset", font=('arial 26 bold'), height=1, width=18, command=reset)
btnReset.grid(row=2, column=0, padx=5, pady=7)

btnNewGame = Button(RightFrame2, text="New Game", font=('arial 26 bold'), height=1, width=18, command=newGame)
btnNewGame.grid(row=3, column=0, padx=5, pady=7)

#--------------- SQUARES BUTTONS # ---------------
button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda:check(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

root.mainloop()