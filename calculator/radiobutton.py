from tkinter import *
from tkinter.messagebox import *

root=Tk()

def display():
    showinfo("",str(v.get()))

v=IntVar ()
lb1=Label(root,text="enter the gender patient")
bt1=Button(root,text="click",command=display())

rd1=Radiobutton(root,text="male"    ,variable=v,value=1)
rd2=Radiobutton(root,text="female"  ,variable=v,value=2)
rd3=Radiobutton(root,text="babyboy"  ,variable=v,value=3)
rd4=Radiobutton(root,text="babygirl" ,variable=v,value=4)

lb1.grid(row=0,column=0)

rd1.grid(row=0,column=1)
rd2.grid(row=0,column=2)
rd3.grid(row=0,column=3)
rd4.grid(row=0,column=4)

bt1.grid(row=1,column=2)

root.mainloop()



