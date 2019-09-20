x=[]
for i in range(1,5):
    a = int(input("enter the temperature of fahrenheit"))
    x.append(a)
p=list(map(lambda a:(a-32)/1.8,x))
print(p)