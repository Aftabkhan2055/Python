from tkinter import *
from tkinter.messagebox import *
def demo():
    n=int(textbox1.get())
    x=0
    for i in range(2,n//2+1):
        if n%i==0:
            x=1
            break
    if x==0:
        showinfo("","prime")
    else:
        showinfo("","not prime")
obj=Tk()


textbox1=Entry(obj)
textbox1.pack()
bt1=Button(obj,text="click",command=demo)
bt1.pack()
obj.mainloop()