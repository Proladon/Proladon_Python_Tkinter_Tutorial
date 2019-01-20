
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.1 建立基本視窗
# Youtube影片: https://youtu.be/_wXmXBpCAfc
#//////////////////////////////////////////////////////////////////////////////#

#python3 tkinter
#導入tkinter模組
from tkinter import*

win = Tk() #建立主視窗
win.title("tkinter test")

btn = Button(text="btn")
btn.pack()

win.mainloop() #常駐主視窗
