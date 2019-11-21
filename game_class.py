import pygame
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()







'''import pygame
from tkinter import *
from functools import partial


def raise_frame(frame):
    frame.tkraise()


main_win = Tk()
main_win.geometry('500x500')
main_win.title("التنقل بين الفريمات")

second_frame = Frame(main_win)
second_frame.place(x=0, y=0, width=500, height=500)

first_frame = Frame(main_win)
first_frame.place(x=0, y=0, width=500, height=500)

label_0 = Label(first_frame, text="هذا الفريم الرئيسي", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

Button(first_frame, text='الذهاب للفريم الثاني', width=20, bg='brown', fg='white',
       command=lambda: raise_frame(second_frame)).place(x=180, y=380)

label_8 = Label(second_frame, text="هذا الفريم الثاني", width=20, font=("bold", 20))
label_8.place(x=90, y=53)

Button(second_frame, text='العودة للفريم الاول', width=20, bg='brown', fg='white',
       command=lambda: raise_frame(first_frame)).place(x=180, y=380)

main_win.mainloop()'''