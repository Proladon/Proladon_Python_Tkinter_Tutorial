
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.7 佈局 pack、place
# Youtube影片: 
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*

win = Tk()

win.title("")
win.geometry("200x200+800+400")

# Pack 佈局
btn = Button(text="Button")
btn.pack(side=TOP)
# btn = Button(text="Button")
# btn.pack(side=LEFT)
# btn = Button(text="Button")
# btn.pack(side=BOTTOM)
# btn = Button(text="Button")
# btn.pack(side=RIGHT)

# Place 佈局
# anchor = 原點位置
btn = Button(text="Button")
btn.place(anchor=CENTER, x=100, y=100, width=100, height=50)

# Grid 佈局
# btn = Button(text="Button")
# btn.grid(row=0, column=0)

win.mainloop()