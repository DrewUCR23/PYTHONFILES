#Q1. Create a class call Canine with attributes as following.
#attr1 ="mammal"
#attr2 ="dog"
#Now define a function call fun(self) within the class Canine that prints I'm a mammal and I'm a dog using a sample method
#Then instantiate object call Roger by assigning Rodger = Canine()
#Now print I'm a mammal accessing class attributes through object and print I'm a dog using method through object.
class CANINE():
    attr1 = "mammal"
    attr2 = "dog"
    def fun(self):
        print("I am a", self.attr1, "and I am a",self.attr2, "using a sample method")

    def METHOD(JOY):
        print("I'm a", JOY.attr2, "using the method through object")

RODGER = CANINE()

print("I'm a", RODGER.attr1, "accessing class attributes through object")
RODGER.fun ()
RODGER.METHOD()
#Q2. 
#a) Create a class call Car with __init__() method with arguments of color and style
#b) Initialize color and style using self
#c) Create two instance attributes of color and style
#d) Create one class attribute of wheels = 4
#e) Create an object c by calling class name and passing arguments of SUV and Black
#f) Create access attributes by printing style & color
#g) Modify the attribute by changing car style to Sedan
#h) Create method showDescrption and print the car description with no arguments
#i) Create method changeColor with color argument and user can change color
class CAR:
    WHEELS= 4
    def __init__(SELF,COLOR,STYLE):
        SELF.COLOR = COLOR
        SELF.STYLE = STYLE
    def CHANGECOLOR(SELF, COLOR):
        SELF.COLOR = COLOR
    def CHANGESTYLE(SELF,STYLE):
        SELF.STYLE = STYLE
    def DESCRIPTION(SELF):
        print("This  is a car with the new style of",SELF.COLOR, SELF.STYLE)
    def SHOWD(SELF):
        return(f"The new color is {SELF.COLOR} and this the style is {SELF.STYLE} using no arguments in SHOW DESCRIPTION")
    def USER(SELF):
        print("Enter your new color for your car")
        COLOR = str(input())
        SELF.CHANGECOLOR(COLOR)
        print(f"This is the new color of your car: {SELF.COLOR}")
        return SELF.SHOWD();

C = CAR("BLACK", "SUV") 
print("This is  a", C.COLOR, C.STYLE, "which was done accessing the attribues of color and style")
print("These are the class attributes for wheels which are the class attributes from car", C.WHEELS)       
C.CHANGESTYLE("BUICK SEDAN")
C.DESCRIPTION()
C.CHANGECOLOR("BLUE")
C.DESCRIPTION()
A = C.SHOWD()
print(A)
C.DESCRIPTION()
USERCAR = C.USER()
print(USERCAR)
#Q3
#a) Define base class call Vehicle() with function description that prints I'm a vehicle
#b) Create subclass call Car with inheriting from Vehicle with function description that prints I'm a car
#c) Create an object v = Vehicle() and c = Car()
#d) Prints I'am a vehicle and I'm a car
#e) Add a method call setSpeed that prints Now traveling at xxx miles per hour
#f) Prints Now Traveling at 25 mph
class VEHICLE():
    def DESCRIPTION(SELF):
        print("I'm a vehicle")
class CAR(VEHICLE):
    def DESCRIPTION2(SELF):
        print("I'm a car and I am a description from the subclass car")
    def SETSPEED(MPH):
        MPH = '25'
        print("I'm now traveling at XXX number miles per hour")
        print("I am now traveling at {} miles per hour".format(MPH))


                
V= VEHICLE()
C = CAR()
V.DESCRIPTION()
C.DESCRIPTION2()
C.DESCRIPTION()
C.SETSPEED()
#Q4.
#3Demonstrate Reading and Writing to file in Python using file call ShallDiePoemByShakespeare.txt under Files in Canvas
FILE = open("SHAKESPEARE.txt", 'r')
print("This is reading the file for read only:", FILE.read())

FILE.close()
FILE = open("SHAKESPEARE.txt", "a")
FILE.write("This is me writing to a file the append function rather than by using the write function")
FILE.close()

FILE = open("SHAKESPEARE.txt", "r")

print("This is using the read function",FILE.read())
FILE= open("SHAKESPEARE.txt" , "r+")
FILE.write("I am now reading and writing to the file right now, Romeo Romeo where art though Romeo? Juliet is the east and I am the son!")
print(FILE.read())
FILE.close()

#Q5.
#Demonstrate try except code where cookies are divided by people and if there is zero people
#then it will invoke ZeroDivisionError.

cookies = 40
people = 0
try:
    print (cookies/people)
except:
    print("ZeroDivisionError")

    
