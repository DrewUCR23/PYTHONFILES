X = int(input("Enter your first integer value"))
Y= int(input("Enter your second integer value accordingly"))
while(X and Y):
    X = int(input("Enter your first integer value"))
    Y= int(input("Enter your second integer value accordingly"))
    LIST =[]
    if(X == "!"):
        break
    elif  X <50 and Y <50:
        print("This is the quantity of X:", X)
    elif X >=50 and Y >= 50:
            print("The value of X and Y is:", X,Y)
            for Z in LIST:
                LIST.append(X)
    else:
        print("You've put in the wrong value! Try again!")

if(X>=50 and Y>=50):
    for i in LIST:
        print("Can we print te elements of i and what will be their count iterations", i)
        for X in LIST:
            print(LIST)



Z = int(input("Enter your first number"))
A = int(input("Enter your second number:"))
if Z==20 and A==40:
    print("My name is Superhuman boy!")
elif Z ==43 and  A==42:
    print("YES BABY")
else:
    print("This is the wrong input")
    



    
