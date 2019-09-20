from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

def test():
        if v1.get()==1:
                showinfo("","Postgraduate")
        if v2.get()==1:
                showinfo("","Graduate")
        if v3.get() ==1:
                showinfo("","Senior")
        if v4.get() == 1:
                showinfo("","Matric")


root=Tk ()

v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()

rd1=Checkbutton(root,text="postgraduate",variable=v1)
rd2=Checkbutton(root,text="graduate",variable=v2)
rd3=Checkbutton(root,text="senior",variable=v3)
rd4=Checkbutton(root,text="matric",variable=v4)

rd1.grid(row=0,column=0)
rd2.grid(row=0,column=1)
rd3.grid(row=0,column=2)
rd4.grid(row=0,column=3)

bt1=Button(root,text="click",command=test)
bt1.grid(row=1,column=4)

root.mainloop()