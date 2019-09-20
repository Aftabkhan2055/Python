from tkinter import *
from tkinter.messagebox import *


#def reset():


root=Tk()
play=0

root.geometry("300x340+50+50")
root.title("calculator")

Tops=Frame(root,width=300,height=20,bd=4,relief="raise")
Tops.pack(side=TOP)

Below=Frame(root,width=300,height=300,bd=4,relief="raise")
Below.pack(side=BOTTOM)

txtDisplay=Entry(Tops,font=('arial',18,'bold'),width=21,bd=4,justify='right')
txtDisplay.grid(row=0,column=0)





bt7=Button(root,padx=1,pady=1,bd=4,fg="black",font=('arial',18,'bold'))









root.mainloop()
