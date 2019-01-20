
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.6 布局 pack、place、grid
# Youtube影片: 
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*

win = Tk()

win.title("")
win.geometry("400x200")

# # pack 布局
# btn = Button(text="Button")
# btn.pack()

# grid 布局
btn = Button(text="Button")
btn.grid(row=1, column=0)

# place 布局
btn = Button(bg="red")
btn.place(width=150, height=30, x=30,y=50)

win.mainloop()