from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
def test():
    s=int(textbox1.get())
    if cb1.get()=="fahrenheit to celcius":
        t=(s-32)/1.8
        showinfo("",t)
    elif cb1.get()=="celcius to fahrenheit":
        t = (s *1.8)+32
        showinfo("", t)

root=Tk()
root.geometry("400x300")
textbox1=Entry(root)

lb1=Label(root,text="enter the temperature")
cb1=Combobox(root,state="readonly",width=35,values=("fahrenheit to celcius","celcius to fahrenheit"))
bt1=Button(root,text="result",command=test)




lb1.grid(row=0,column=0)
textbox1.grid(row=0,column=1)
cb1.grid(row=1,column=1)
bt1.grid(row=2,column=1)

root.mainloop()


