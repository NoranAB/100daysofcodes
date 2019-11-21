import pygame
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import tkinter as tk
root = tk.Tk()

# Create a Tkinter variable
tkvar = tk.StringVar(root)

# options
choices = ['Pizza','Lasagne','Fries','Fish','Potatoe']
tkvar.set('Pizza') # set the default option

def on_selection(value):
    global choice
    choice = value  # store the user's choice
    root.destroy()  # close window

popupMenu = tk.OptionMenu(root, tkvar, *choices, command=on_selection)
tk.Label(root, text="Choose a dish").grid(row=0, column=0)
popupMenu.grid(row=1, column =0)

root.mainloop()

# Do whatever you want with the user's choice after closing the window
print('You have chosen %s' % choice)











"""def btnClick(Human):
    gcont = True
    while gcont:
        for event in pygame.event.get(): #print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quiut()


def key_press(event):


root.bind('<bth1>', key_press)

def button_press(event):
    #print("Button is pressed")
bth1.pack()
bth1.bind('<ButtonPress', button_press)








def btnClick (bth1):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (action == "Start"):
        game_loop()
    elif (bth2)
        (action == "Start"):
        game_loop()






 def HumanbtnClick(bth1):

        for i in range(3):
            for j in range(3):
                tile=pg.Rect(j*self.box_size,i*self.box_size,self.box_width,self.box_height)
                if tile.collidepoint((x,y))==1 and board[i][j]=='_' :
                    self.mark_x(i,j)
                    return True
        else:"""













