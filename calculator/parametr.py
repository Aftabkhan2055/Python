class demo:

    def __init__ (self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def display(self):
        print ("value of a is",self.a)
        print("value of b is", self.b)
        print("value of c is", self.c)
x=demo(10,20,30)
x.display()
