
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.8
# Youtube影片: 
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*
from tkinter import messagebox as Mesg


win = Tk()
win.geometry("400x400")

ck_value = IntVar()
ck_value2 = IntVar()
def show_val():
    print(ck_value)
    print(ck_value2)

ck = Checkbutton(text="number1", variable=ck_value)
ck.pack()

btn = Button(text="show", command= show_val)
btn.pack()






win.mainloop()