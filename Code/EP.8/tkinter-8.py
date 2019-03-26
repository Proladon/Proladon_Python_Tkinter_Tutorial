
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.8
# Youtube影片: 
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*



win = Tk()
win.geometry("400x400")

def des():
    fr_1.fr.destroy()

class frame:
    def __init__(self):
        self.fr = Frame(win)
        self.fr.pack(side=LEFT)

fr_1 = frame()

fr_2 = Frame(win)
fr_2.pack(side=RIGHT)

btn = Button(fr_1, text="Button")
btn.pack()
btn = Button(fr_2, text="Button", command= des)
btn.pack()

win.mainloop()