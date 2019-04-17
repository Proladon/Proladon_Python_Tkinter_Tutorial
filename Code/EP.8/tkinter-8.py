
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.8 Scale尺度(滑桿)
# Youtube影片: https://youtu.be/EfKJG_TSr8U
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*
from tkinter import messagebox as Mesg


win = Tk()
win.geometry("400x400+800+300")

def change(self):
    s_value = s.get() # 讀取拉桿的value
    win.attributes("-alpha", s_value/100) # 設置視窗透明度

# 方向, 寬度, 長度
s = Scale(orient=HORIZONTAL, width=100, length=200)
# 設置範圍 mini 10 ~ max 100
s.config(from_=10, to=100)
# 顯示value, 間隔刻度, 解析度, 設置顯示位數
s.config(showvalue=1, tickinterval=10, resolution=10, digits=1)
# Label
s.config(label="Tkinter Slider")
# 直接設置初始值
s.set(50)

s.config(command=change)
s.pack()

win.mainloop()

