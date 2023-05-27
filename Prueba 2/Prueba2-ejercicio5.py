
print("inicio de valores")
x=10000
z=-1
s=0
y="1100"

print("x= ",{x})
print("z= ",{z})
print("s= ",{s})
print("y= ",{y})

print("Inicio While")
while(x > 0):
    if(len(y) > 3):
        x=x/10
        print("if(len(y) > 3): dentro de while")
        print("x= ",{x})
        print("z= ",{z})
        print("s= ",{s})
        print("y= ",{y})
    if(len(y) >6):
        x=0
        print("if(len(y) >6): dentro de while")
        print("x= ",{x})
        print("z= ",{z})
        print("s= ",{s})
        print("y= ",{y})
        print("Inicio for")
    for i in range (int(x/200)):
        print("Inicio for")
        print("i= ",{i})
        print("x= ",{x})
        print("z= ",{z})
        print("s= ",{s})
        print("y= ",{y})        
        if(i>3):
            s=s + z**i
            print("if(i>3): dentro de for")
            print("i= ",{i})
            print("x= ",{x})
            print("z= ",{z})
            print("s= ",{s})
            print("y= ",{y})
        elif(i%2==0):
            y=y+y[i+z]*3
            print("elif(i%2==0): dentro de for")
            print("i= ",{i})
            print("x= ",{x})
            print("z= ",{z})
            print("s= ",{s})
            print("y= ",{y})
        s=s +len (y)* (z**i)
        print("s=s +len (y)* (z**i) parte final")
        print("i= ",{i})
        print("x= ",{x})
        print("z= ",{z})
        print("s= ",{s})
        print("y= ",{y})

