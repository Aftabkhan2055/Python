class demo:
    ls=[]
    def accept(self):
        s=input("enter the number in comma seprated from")
        ar=s.split(",")
        self.ls=list(map(lambda x: int (x),ar))
    def display(self):
        print("sum is",sum(self.ls))
        print("max is", max(self.ls))
        print("min is",min(self.ls))
x=demo ()
x.accept()
x.display()
