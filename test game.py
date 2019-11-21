import pygame
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

click = True
tk = None
def start():
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe")

    def play(button):
        global click, tk

        if button["text"] == " " and click:
            button["text"] = "X"
            click = False
        elif button["text"] == " ":
            button['text'] = "O"
            click = True

        if (bu1["text"] == "X" and bu2["text"] == "X" and bu3["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu4["text"] == "X" and bu5["text"] == "X" and bu6["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu7["text"] == "X" and bu8["text"] == "X" and bu9["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu1["text"] == "X" and bu4["text"] == "X" and bu7["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu2["text"] == "X" and bu5["text"] == "X" and bu8["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu3["text"] == "X" and bu6["text"] == "X" and bu9["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu1["text"] == "X" and bu5["text"] == "X" and bu9["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer") or
            bu3["text"] == "X" and bu5["text"] == "X" and bu7["text"] == "X"):
            r = p1.get()
            score = (r + 1)
            p1.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player X is the winer")









           # answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')
            #tk.destroy()
            #if answer == 'yes': start()

def scorekeeper():

        elif (bu1["text"] == "O" and bu2["text"] == "O" and bu3["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu4["text"] == "O" and bu5["text"] == "O" and bu6["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu7["text"] == "O" and bu8["text"] == "O" and bu9["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu1["text"] == "O" and bu4["text"] == "O" and bu7["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu2["text"] == "O" and bu5["text"] == "O" and bu8["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu3["text"] == "O" and bu6["text"] == "O" and bu9["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu1["text"] == "O" and bu5["text"] == "O" and bu9["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer") or
            bu3["text"] == "O" and bu5["text"] == "O" and bu7["text"] == "O"):
            r = p2.get()
            score = (r + 1)
            p2.set(score)
            messagebox.showinfo(title="CONGRATS ^_^", message="Player O is the winer")



            #answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')
            #tk.destroy()
            #if answer == 'yes': start()

    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)

    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda:play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda:play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)


    tk.mainloop()

start()







# other
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        i -= vel
    if keys[pygame.K_RIGHT]:
        i += vel
    if keys[pygame.K_UP]:
        j -= vel
    if keys[pygame.K_DOWN]:
        j += vel


    pygame.draw.rect(Win, (225, 0, 0), (i, j, width, height))
    pygame.display.update()
pygame.quit()





def ButtonClick(id):
    btn1 = Button(root, text="  VS AI  ", font="times 17", width=20, bg="pink4", fg='plum1')
    btn1.config(command=lambda: ButtonClick(1))
    btn1.grid(row=4, column=2)
    print("ID:{}".format(id))
    global ActivePlayer
    global p1
    global AI
    if (ActivePlayer == 1):
        SetLayout(id, "X")
        p1.append(id)
        root.title("Tic Tac Toe :Player X")
        ActivePlayer = 2
        print("p1:{}".format(p1))
        AutoPlay() AI





     for X in range(0,len(root.but)):
         root.but[X].setEnabled(True)
         root.but[X].setText('')

elif root.oper()=='O':
     QMessageBox.information(root. 'Tic Tac Toe', Player 2 is Win !', QMessageBox.ok)
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
     if root.game == 'X':
         root.game = 'O'
     elif root.game == 'O':
         root.game = 'X'






p1 = IntVar()
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
p2.set(0)
