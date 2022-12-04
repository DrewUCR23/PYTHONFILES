
#(20 points) Q1. Create a class call Bank_Account that has following functions
#and produce output with user entered value.
#1. __init__
#2. deposit
#3. withdraw
#4. display
#Create objects to show deposit, withdraw and display as following.
#Output:
#Hello!!! Welcome to the Deposit & Withdrawal Machine
#Enter amount to be Deposited: 100
#Amount Deposited: 100.0
##Enter amount to be Withdrawn: 20
#You Withdrew: 20.0
#Net Available Balance= 80.0
class BANK_ACCOUNT:
    def __init__(SELF,IN_DEPOSIT=0):
        SELF.BALANCE = IN_DEPOSIT
    def DEPOSIT(SELF):
        A = float(input("Enter the amount to be deposited:"))
        SELF.BALANCE +=A
        return(print("Amounted deposited",A))
    def WITHDRAW(SELF):
        B = float(input("Enter amount to be Withdrawn:"))
        SELF.BALANCE -=B
        if(SELF.BALANCE<=0):
            SELF.BALANCE =0
            print("You cannot withdraw, you are over your balance")
        else:
            print("You Withdraw:", B)
            print("Net Available Balance:",SELF.BALANCE)
        
##initializing the object to be called
C= BANK_ACCOUNT()
C.DEPOSIT()
C.WITHDRAW()
#(15 points) Q2. Make a class called Restaurant. The __init__() method for 
#Restaurant should store two attributes: a restaurant_name and a 
#cuisine_type. Make a method called describe_restaurant() that prints these 
#two pieces of information, and a method called open_restaurant() that prints 
#a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes 
#individually, and then call both methods.
class RESTAURANT:
    def __init__(SELF, RN, CT):
        SELF.RN = RN
        SELF.CT = CT
    def DR(SELF):
        print("This is the name of the restaurant",SELF.RN)
        print("This type of cuisine is",SELF.CT)
    def OPENR(SELF):
        print("The restaurant is now open! Come on in!")
    def ICEN(SELF,RN):
        SELF.RN = RN
    def NEW(SELF):
        print("The name of the icecream restaurant is!",SELF.RN)
        
R = RESTAURANT("Drew's Pizza Restaurant","Italian Pizza, Spicy Pizza and fancy food! Love it!")
print("This is the first attribute using an instance from restaurant which is the name", R.RN)
print("This is the second attribute using an instance from restaurant and is the cusiine type which is ", R.CT)
R.DR()
R.OPENR()    
#(15 points) Q3. An ice cream stand is a specific kind of restaurant. Write a 
#class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Q2. Add an attribute called flavors that stores a list of ice cream flavors. 
#Write a method that displays these flavors. Create an instance of 
#IceCreamStand, and call this method.
class RESTAURANT:
    def __init__(SELF, RN, CT):
        SELF.RN = RN
        SELF.CT = CT
    def DR(SELF):
        print("This is the name of the restaurant",SELF.RN)
        print("This type of cuisine is",SELF.CT)
    def OPENR(SELF):
        print("The restaurant is now open! Come on in!")
    def ICEN(SELF,RN):
        SELF.RN = RN
    def NEW(SELF):
        print("The name of the icecream restaurant is!",SELF.RN)
        
##R = RESTAURANT("Drew's Pizza Restaurant","Italian Pizza, Spicy Pizza and fancy food! Love it!")
#print("This is the first attribute using an instance from restaurant which is the name", R.RN)
#print("This is the second attribute using an instance from restaurant and is the cusiine type which is ", R.CT)
#R.DR()
#R.OPENR()
#R.ICEN("Drew's Delicious IceCream Parlor!")
#R.NEW()
class ICECREAMSTAND(RESTAURANT):
  flavors_list = ["Rocky road", "Vanilla", "Chocolate " , "Black Cherry"]
  def __init__(SELF,RN,CT, FLAVORS):
      super().__init__(RN,CT)
      SELF.FLAVORS = FLAVORS
        #SELF.FLAVORS1 = FLAVORS1
        #SELF.FLAVORS2 = FLAVOR2
        #SELF.FLAVORS3 = FLAVORS3
  def PRINT_FLAVORS(SELF):
        print("These are the flavors of icecream we have:",ICECREAMSTAND.flavors_list, "and",SELF.FLAVORS, "using strawberry as an argument")
        #SELF.FLAVORS,SELF.FLAVORS1,SELF.FLAVORS2,SELF.FLAVORS3)

IC= ICECREAMSTAND( " ", " ", "Strawberry CheeseCake")             #"Vanilla", "Chocolate", "Black Cherry")
IC.PRINT_FLAVORS()
IC.ICEN("Drew's Delicious IceCream Parlor")
IC.NEW()

