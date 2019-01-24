
#//////////////////////////////////////////////////////////////////////////////#
#【Proladon】Python GUI - Tkinter EP.6 佈局 pack、place、grid
# Youtube影片: 
#//////////////////////////////////////////////////////////////////////////////#

from tkinter import*

win = Tk()

win.title("")
win.geometry("+800+400")

# Grid 網格佈局
user = Label(text="User ")
user.grid(row=0, column=0)

password = Label(text="Password ")
password.grid(row=1, column=0)

user_entry = Entry(bg="#323232")
user_entry.grid(row=0, column=1)

password_entry = Entry(bg="#323232)
password_entry.grid(row=1, column=1)

# # 跨行Span
# user = Label(text="User ")
# user.grid(row=0, column=0)

# password = Label(text="Password ")
# password.grid(row=1, column=0)

# user_entry = Entry(bg="#323232", font="微軟正黑體 20")
# user_entry.grid(row=0, column=1, rowspan=2)

win.mainloop()
