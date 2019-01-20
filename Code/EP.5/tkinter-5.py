
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.5 第一個程式 X,Y座標隨機產生器
# Youtube影片: https://youtu.be/qkxkLLzu3H0
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*

# 處理隨機數生成
import random
# 處理複製的功能
import pyperclip

# Tk視窗參數設定
win = Tk()
win.title("Random X,Y Generator")
# win.geometry(長x寬 +X +Y)
win.geometry("400x220+800+400")
win.config(bg="#323232")

#////////////////////////////////////#

title_text = Label(text="Random X,Y Generator", fg="skyblue", bg="#323232")
# obj.config(font="字型 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()


# 最小值 文字 與 輸入框
min_range = Label(text="Min range", fg="white", bg="#323232")
min_range.pack()
min_entry = Entry()
min_entry.pack()

# 最大值 文字 與 輸入框
max_range = Label(text="Max range", fg="white", bg="#323232")
max_range.pack()
max_entry = Entry()
max_entry.pack()

# 顯示 X,Y 座標
x_show = Label(text="", fg="white", bg="#323232")
x_show.pack()
y_show = Label(text="", fg="white", bg="#323232")
y_show.pack()

def gen_xy ():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    # random.randint(最小值, 最大值)
    x = str(random.randint(min_val, max_val))
    y = str(random.randint(min_val, max_val))
    x_show.config(text="X: " + x)
    y_show.config(text="Y: " + y)

def copy ():
    xy = x_show.cget("text") + "\n" + y_show.cget("text")
    pyperclip.copy(xy)
  
# 生成及複製按鈕
generate_btn = Button(text="Generate", command= gen_xy)
generate_btn.pack()
copy_btn = Button(text="Copy", command= copy)
copy_btn.pack()


win.mainloop()


