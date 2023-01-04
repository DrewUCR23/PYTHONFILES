#2 points) Q1. What is the main difference between for loop and while loop in python?
#(2 points)
The difference between a for loop and a while loop in python has to do with the way in which each method iterates.
A for loop in python typically goes as for  x in range(1,10) as an example sets a specific value as the maximum range boundary. In this example we have the maximum number of iteration values that we will be looking
for. Furthermore, the for loop also typically uses in to check for a set value that is within a list, set,tupple or even a dictionary etc. In doing so a for loop has a definite starting and a definite ending point
wihout having to specify a limit on the counters. A while loop typicall typically consists of a variable or quantity and a comparison statement that is true or not true.
For ex, x = 10 while x==10:  X +=1 . As an example this loop will go on forever unless it has a specific if conditional or break statement that has the capacity of stopping the while loop.
In this case the X value is boolean true because the quantity value is 10. Therefore, the counter of X +=1 will keep incrementing forever. If I add  x= 10 max_counter = 25
while(X<MAX_Counter)x +=1  if(X==MAX_Counter) print("This value has hit 25", "and the value is:", X) break;. It now has a specific truth conditional to tell it to stop with the break; statement. In  a for loop
this is not necessary because the boundary stops it. Therefore, a for loop has an inbuilt limit and specified incrementer while a while-loop does not. You specify it and a stop condtion or
it will not work correctly. A for loop is for when you want an exact starting point and end point for a counter. A while loop may be better if you want longer loops
or you want to keep looping a user input. A boundary limit like in for 1 in range(1,25) has the limit boundary of 25 is mandatory in this for loop. It is useful while in a while loop
this is purely optional and not necessary.
#Q2. What is argument and What is parameter in python functions.
#What is the difference between them?
#(2 points)
#Q3. Explain what class is and what object is in python and give simple
A class is basically a container for methods that can be contained with the class. A class can also have attributes that you can call on and print out those given values.
While, an object is an instance of class where that class is defined as the object. As a defined object of a given class you can call upon methods or general
attributes from the class and call on them accoridngly. In this sample class has the attributes of happy in emotion  and emotion two that hold the string values of angry and happy.
Next, we have a method for _init__ that initialize the other arguments which will eventually hold other string values that represent emotions. Then I intialized the object
as C= HAPPY() with two string values that will replaced for emotion3 and emotion 4. The difference between class and object is that an object is an instance of a class that
allows the user to call arguments and methods from the class. The class serves as the general container for attributes and methods. If you do not make the class an object
then you cannot call on the class until it has been made into an object. Classes can also have subclasses with inheritance that allows a sub-class to assume all the qualities
of the main class(parent class) for the (child class) etc.
For example, 
class HAPPY():
    EMOTION = "happy"
    EMOTION2 = "angry"
    def __init__(SELF, EMOTION3, EMOTION4):
        SELF.EMOTION3=EMOTION3
        SELF.EMOTION4 = EMOTION4
    def EMOTIONS(SELF):
        print("These are the emotions as a human has", SELF.EMOTION3, SELF.EMOTION4, "& attributes as well", C.EMOTION, C.EMOTION2)

C= HAPPY("JOY","SORROW")
C.EMOTIONS()
print("This is printing from attributes of the class", C.EMOTION, C.EMOTION2)
#example explaining class and object.
#(2 points)
#Q4. Circle each reason we use functions:
#a) to reduce code duplication     <----A 
#b) to allow for the use of mathematics
#c) to make a program more modular   <-----a function makes the program more modular and simplistic because you need less code because you can call the same function
#d) to reduce the number of variables.  <--- this also allows for lesser variables because you can call the same method(check answer)

#(2 points) Q5. Circle the term that means, placing a decision inside of another decision
#a) cohabitation b) spooning c) nesting d) encapsulation  is the correct answer (check answer)
#(2 points)
#Q6. For each statement about functions, tell true or false and briefly 
#explain.
#a) A function must either return something or print something, or both.
#b) A function must have at least one parameter.
#c) A function cannot modify the value of any of its arguments.
#(12 points)

#Q7. Think of at least three kinds of your favorite pizza. Store these 
#pizza names in a list, and then use a for loop to print the name of each pizza.
#Modify your for loop to print a sentence using the name of the pizza instead of 
#printing just the name of the pizza. For each pizza you should have one line of 
#output containing a simple statement like I like pepperoni pizza.
#Add a line at the end of your program, outside the for loop, that states how much 
#you like pizza. The output should consist of three or more lines about the kinds of 
#pizza you like and then an additional sentence, such as I really love pizza! Use for 
#loops
PIZZA = ["PEPPERONI PIZZA", "PINNEAPPLE PIZZA", "JALAPENO PIZZA"]
for i in PIZZA:
    print(i)
    print("I really love {}".format(i))



print("I really love Pizza!")
# A user input that stores a argument

PIZZA = []

for i in range(5):
    A= input("Enter your pizza flavors")
    PIZZA.append(A)
    for X in PIZZA:
        print("I really love this {} pizza ".format(X))

print("I really love this pizza")


#(12 points) Q8 Write a function that accepts a list of items a person wants on a sandwich. The 
#function should have one parameter that collects as many items as the function call provides, and 
#it should print a summary of the sandwich that is being ordered. Call the function three items, 
#using a different number of arguments each time.
print("press 2 for the second response to exit the loop for ingredients")
def SANDWICH():
    LIST = []
    while len(LIST) <7:
        A = input("What type of ingredients do you want on your sandwitch?")
        B = input("What is your second ingredient:")
        if  A== "2":
            print("The loop has ended")
            print("I'll make you a great sandwitch:")
            #LIST.append(A)
            break
        if A !="" and B !="":
            LIST.append(A)
            LIST.append(B)
    if(A):
        for i in LIST:
            print("adding {} to your sandwich.".format(i))
    if(B):
            print("Your sandwich is ready!")

SANDWICH()
SANDWICH()
SANDWICH()
#(14 points) Q9. Create a class call Employee and a subclass call Developer that inherits 
#characteristics from Employee.
class EMPLOYEE():
    LOCATION = "Riverside,CA"
    def __init__(SELF, NAME,EMAIL,ROLE):
        SELF.NAME = NAME
        SELF.EMAIL= EMAIL
        SELF.ROLE = ROLE
    def GET_INFO(SELF):
        print("This is the name {}, this is the email {} and this is the role {}".format(SELF.NAME,SELF.EMAIL, SELF.ROLE))
    def CHANGE_LOCALE(SELF):
        EMPLOYEE.LOCATION = "Seattle, WA"
class D(EMPLOYEE):
    def __init__(SELF, NAME,EMAIL,ROLE, LANGUAGE):
        super().__init__(NAME,EMAIL, ROLE)
        SELF.LANGUAGE = LANGUAGE
    def GET_INFO1(SELF):
        print("This is the name {}, this is the email {} and this is the role {} and this is the language {} USING the subclass get info.".format(SELF.NAME, SELF.EMAIL,SELF.ROLE, SELF.LANGUAGE))

EMPLOYEE1 = D("MICKEY MOUSE", "MMOUSE@DISNEY.COM", "LEAD CHARACTER", "PYTHON")
EMPLOYEE2= D("DONALD DUCK", "DDUCK@DISNEY.COM", "BAD CHARACTER", "FORTRAN")
print("This is the location of employee 1", EMPLOYEE.LOCATION)
EMPLOYEE1.CHANGE_LOCALE()
print("This is the new location for employee 1:", EMPLOYEE.LOCATION)
EMPLOYEE1.GET_INFO()
EMPLOYEE2.GET_INFO1()
print("This is employee 2's language", EMPLOYEE2.LANGUAGE)

EMPLOYEE1.GET_INFO()
