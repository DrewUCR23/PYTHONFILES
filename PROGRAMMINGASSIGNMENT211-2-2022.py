#(7 points) Q1. Write a python program to sort the words alphabetically in an
#string provided by the user. Use .split(), .sort() and for loop. For example, if
#given string is s= "Hello this Is an Example With cased letters" then your
#output should look
#The sorted words are:
#Example
#Hello
#Is
#With
#an
#cased
#letters
#this
wordsSorted = []
U= (input("What words would you like to sort?"))
NEWUSER= U.split()
print("This is a string with a split in it",NEWUSER)
newUSE= NEWUSER.sort()
for newUSE in NEWUSER:
    wordsSorted.append(newUSE)
    print("This is printed sorted with not appending a list:",newUSE)
print("This is the list in alpabetical order using the sort method",wordsSorted)
#(7 points) Q2. Assign an integer x between 40 and 50 and assign an integer y
#between 80 and 100.
#Write a python program using while loop that if x is less than 50 AND y is
#less than 100, increment both integers by 1 and program should stop if
#either integer reaches 50 or 100. Use while loop and print output for both x
#and y.
#For example, if you assign x = 46 and y = 97, your output should look
#47 98
#48 99#
#49 100
x= 41
y= 91
while  x< 50 and y<100:
     x+=1
     y+=1
     print (" X: {} and y: {}".format(x,y))
#(7 points) Q3.Write a function call isOdd with return to determine whether
#given integer is even or odd. Ask user to supply the integer
#(10 points)
     def isODD(USER):
         return(USER)  
USER = int(input("Enter a number: "))
if (USER % 2) == 0:
    print("{0} is Even".format(USER))
elif USER %2 !=0:
    print("{0} is Odd".format(USER))
    #Q4. Write a function that stores information about a car in a
#dictionary. The function should always receive a manufacturer and a model
#name. It should then accept an arbitrary number of keyword arguments. Call
#the function with the required information and two other name-value pairs,
def info_car(Manufacture, Model,color):
    car_info_dic1 = {"Manfacture:": Manufacture,  "Model": Model, "Colors":color,}
    car_info_dic1["Colors"] = color

    return(car_info_dic1)
Buick_regal = info_car("Buick","Regal Ls",color = "Gray")
print("An example of a predone car that is stored in Buick_regal with return:", Buick_regal)

#### user input
def info_car(Manufacture, Model, color):
    car_info_dic = {"Manfacture:": Manufacture,  "Model": Model, "Colors": color }
    car_info_dic["Colors"] = color
    print("A dictionary that stores user input to store a value of a car in a dictionary",car_info_dic)
Manufacture = (input("Enter the Manufactuer!"))
Model = (input("Enter the Model name!"))
color = (input("Enter the type of color you want to put in the dictionary!:"))
info_car( Manufacture, Model, color)

#(9 points) Q5. Assume n is a positive integer. Write a function call pSUM with
#parameter (x, n) that computes and prints the value of the sum.

def PSUM(X,N):
    sum= 1+X/1+pow(X,2)/2+pow(X,3)/3+pow(X,4)/4+pow(X,N)/N
    print(sum)
X= int(input("Enter the first number:"))
N = int(input("Enter the second number:"))
PSUM(X,N)
#(10 points) Q6. Write a function call pFact that takes two positive integers
#𝑘, 𝑚 and returns the product 𝑘 ∗ (𝑘 − 1) ∗ (𝑘 − 2) … . . (𝑘 − 𝑚) If 𝑘 ≤ 𝑚, it
#should return 0.

#value of zero doesn't call the function correctly
def PFACT(k,m):
    return(k,m)
    return([0])
k = int(input("Enter your first number:"))
m = int(input("Enter your second number:"))
x=0
product = k*(k-1)*(k-2)*(k-3)*(k-m)
if k<=m:
    print("The values of M AND N are less than or equal to m and returned", x)
else:
    print(product)



