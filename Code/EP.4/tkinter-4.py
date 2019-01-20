
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.4 Label、Entry (功能連結)
# Youtube影片: https://youtu.be/bG8qUpH2Bzw
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*

win = Tk()
win.geometry("400x200")
win.config(bg="#323232")

def ok():
    # 取得輸入值 (回傳為 String字串 資料型態)
    t = en.get()
    # 設置 lb 物件的文字內容
    lb.config(text= t)

# Label 物件
lb = Label(bg="#323232", fg="white", text="This is lable")
lb.pack()

# 輸入框
en = Entry()
en.pack()

# 按鈕
btn = Button(text="Ok", command= ok)
btn.pack()

win.mainloop()
