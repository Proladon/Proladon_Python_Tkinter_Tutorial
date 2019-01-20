
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.2 視窗基本屬性(大小、透明度、置頂、標題、ICON)
# Youtube影片: https://youtu.be/qkxkLLzu3H0
#//////////////////////////////////////////////////////////////////////////////#


from tkinter import* #導入Tkinter模組

win = Tk() #建立Tk視窗

#標題
win.title("tkinter gui")


#大小
win.geometry("400x400") #寬x高
win.minsize(width=400, height=200) #最小範圍
win.maxsize(width=1024, height=768) #最大範圍
win.resizable(0, 0) # 1 = True, 0 = False

#ICON (.ico檔, 在同一個資料夾下或是直接給予完整路徑)
win.iconbitmap("E:\Coding\Python\GUI Test\github512.ico") 

#顏色
win.config(bg="skyblue")

#透明度
win.attributes("-alpha", 0.5)   #1~0,  1=100%  0=0%

#置頂
win.attributes("-topmost", 1) # 1 = True, 0 = False

#循環常駐主視窗
win.mainloop()
