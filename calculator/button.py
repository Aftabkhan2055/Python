from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

def test():
    if x.get()==1:
        showinfo("","postgraduate")
    elif x.get()==2:
        showinfo("","graduate")
    elif x.get()==3:
        showinfo("","senior")
    elif x.get()==4:
        showinfo("","matric")


root=Tk()
x=IntVar()

rd1=Radiobutton(root,text="postgraduate",value=1,variable=x)
rd2=Radiobutton(root,text="graduate",value=2,variable=x)
rd3=Radiobutton(root,text="senior",value=3,variable=x)
rd4=Radiobutton(root,text="matric",value=4,variable=x)

rd1.grid(row=0,column=0)
rd2.grid(row=0,column=1)
rd3.grid(row=0,column=2)
rd4.grid(row=0,column=3)

bt1=Button(root,text="click",command=test)
bt1.grid(row=1,column=4)

root.mainloop()