
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.3 Button按鈕(功能連結、大小、顏色、圖片)
# Youtube影片: https://youtu.be/zVp1Dg_WQwU
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*

win = Tk()

win.title("tkinter gui")
win.geometry("400x200")

# Function
def say_hi ():
    print("Hi everyone !")

# Image
img = PhotoImage(file="G:\Image\Icon\Coding.png")

# Button
btn = Button(text="Click me")
btn.config(image= img) # 指定圖片
btn.config(command= say_hi) # 指定Function
btn.pack()

win.mainloop()