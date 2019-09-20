from tkinter import *
from tkinter.messagebox import *
def sum():
    s=(textbox1.get())
    ar=s.split(",")
    total=0
    for s in ar:
        total=total+int(s)
    showinfo("","total is "+str(total))
obj=Tk()
obj.geometry("300x300")
obj.title("aftab")
textbox1=Entry(obj)
textbox1.pack()
bt1=Button(obj,text="click",command=sum)
bt1.pack()
obj.mainloop()