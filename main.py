from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from ttkthemes import themed_tk as tk
import os
from facerec import mark

def enroll():
    root.destroy()
    os.system("python newenrollment.py")

def login():
    root.destroy()
    os.system("python start.py")


root = tk.ThemedTk()
root.geometry("640x480")
root.title("Online Attendance") 
root.iconbitmap(r'att.ico')

root.get_themes()
root.set_theme("breeze")

menubar = Menu(root)
root.config(menu=menubar)

subMenu = Menu(menubar,tearoff=0)
menubar.add_command(label="LOGIN AGAIN",command=login)

statusbar=ttk.Label(root, text="Home Page", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

topframe = Frame(root)
topframe.pack(padx=20,pady=20)

#helloPhoto = ImageTk.PhotoImage(file='hello.png')
#helloico=ttk.Label(topframe, image = helloPhoto)
#helloico.grid(row=0,column=0,padx=20)

filelabel = ttk.Label(topframe, text = 'WELCOME TO ONLINE ATTENDANCE', font="Times 20 underline")
filelabel.grid(row=0,column=1,pady=20)

middleframe = Frame(root)
middleframe.pack()

enrolllabel = ttk.Label(middleframe, text = 'ENROLL A NEW STUDENT', font="Times 15 normal")
enrolllabel.pack(side=LEFT, padx=20)

enrollPhoto = PhotoImage(file='enroll.png')
enrollBtn = ttk.Button(middleframe, image = enrollPhoto, command=enroll)
enrollBtn.pack(pady=30)

bottomframe = Frame(root)
bottomframe.pack()

marklabel = ttk.Label(bottomframe, text = 'MARK ATTENDANCE', font="Times 15 normal")
marklabel.pack(side=LEFT, padx=20)

markPhoto = PhotoImage(file='mark.png')
markBtn = ttk.Button(bottomframe, image = markPhoto, command=mark)
markBtn.pack(pady=30)

root.mainloop()
