#Q1. Please show your input and output for following questions
#a) Create a list call planets with ['Earth', 'Moon', 'Venus', 'Mars', 'Mercury']
planets = ['Earth', 'Moon', 'Venus', 'Mars', 'Mercury']
#b) Print the planet at location 4
print(planets[4])
#c) Print the planet at location 2 to 4
print(planets[2:4])
#d) Add Jupiter to the end of the list and print the list
planets.append("Jupiter") == 5
print(planets)
#e) Sort the planets in alphabetical order and print the list
planets.sort()
print("This list has been sorted",planets) #d
#f) Determine if Sun is in the list
planets = ['Earth', 'Moon', 'Venus', 'Mars', 'Mercury']
print("Sun is not in the list and is:","Sun" in planets)
 #g) Sort the planets in the reverse order and print the list
planets.sort(reverse = True) #d
print("This list is printed in the reverse order",planets)
#h) Determine the length of the list
print("The length of the list is,",(len(planets))) #d
#i) Add Jupiter to the beginning of the list without replacing existing item and print the list
planets1 = ['Earth', 'Moon', 'Venus', 'Mars', 'Mercury']
planets1.insert(0,'Jupiter')  #use this method of insert(integer,string)
print("This is jupiter added to the list",planets1)
#j) Remove the last planet in the list using pop() and print the list
planets1.pop(5)
print("This is the list with mercury removed,",planets1) #d
#k) Remove 1st location item planets[0] using del
del planets1[0]
print("The list using delete to remove Jupiter",planets1)#d
#l) Remove Mars using remove()
planets1.remove("Mars") #d
print("This is the list with mars removed with remove value",planets1)
#Q2. Please show your input and output for following questions
#a) import numpy as np
import numpy as np 
#b) Create an array call array1 with [11,22,33,44]
array1 = np.array([11,22,33,44])
print("This is the first array:", array1)
#c) Create another array call array2 with adding 777 in the beginning of the list in array1
array2 = np.insert(array1,0,777)
print(array2)

#d) Create another array call array4 with adding 555 in the beginning of the list in array1 
   #and 999 at the end of the list
#when inserting an item into an array you must always specify index and then the value that you wished to be inserted in the array
array4 = np.insert(array2,0,555)
print(array4)
array5 = np.insert(array4,6,999)
print("The entire array with 999 and 555 inserted in index 0-6 accordingy:,",array5)
#Q3. Declare checking_balance = 1000 and saving_balance = 1500
    #If checking balance is less than 2000, transfer 500 from saving_balance then print 
    #both checking and saving balance
checking_balance = 1000
saving_balance = 1500

if checking_balance < 2000:
    new_savingbalance = saving_balance - 500
    newchecking_balance = checking_balance+500
    print("Original Checking Balance:", checking_balance, "Original Saving Balance:", saving_balance)
    print("This is your new check balance,:", newchecking_balance, "This is your new savings balance", new_savingbalance)

#Q4. Ask user for his or her age. Write a code if age<21, print illegal drinking age, 
   #if age >65 print Eligible for Medicare else print Keep Working
    
age = int(input("What is your age?"))
if age<21:
    print("Your at an illegal drinking age")
if age > 65:
    print("Your eligible for medicare")
else:
     print("You need to keep working!")
#Q5. Write Python program that asking users to enter two numbers and evaluate these two numbers to determine
    #if two numbers are same or one is larger than the other. USe if statements and do not use functions.
a1 = int(input("Enter your first number:"))
b1= int(input("Entet your second number:"))
if a1 >b1:
    print("A is greater than b and is not the same", a1>b1)
elif  a1<b1:
    print("A is less than b which is ", a1<b1)
elif a1==b1:
    print("A is equal to b")
else:
    print("This is an invalid input")
#Q6. Write Python program that asking users to enter 1 or 2. If user input 1, print Hello World and if user input 2 then print
    #Python Rocks and if user do not enter anything or other numbers or characters that are not equal to 1 or 2, 
    #print You did not enter a valid number.    #n >2 and n <1
#when your writing an else statement you must the colon after else: in order to end that given statement
n = int(input("Enter 1 or 2:"))
if n == 1:
             print("Hello World")
if n ==2:
             print("Python rocks!")
else:
    print("You did not enter a valid number")

#Q7. A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
    #The list of perfect number is: 6, 28, 496, 8128, 33550336
    #Write a python code to determine if user entered a perfect number using If Then conditional statement. Do not use loop.

# you can use an in if statement to search through a list or a set

perfectN = [6, 28, 496, 8128, 33550336]
pn = int(input("Enter a number that will be determined as a perfectnumber!:"))
if pn in perfectN:
    print(pn, "is a perfect number!")
else: #pn != perfectN
   print("This is not a perfect number:", pn)
#Q8. Write Python program that  the user entered input is even or odd integer. USe If Then statement. Do not use Loops.
 
num = int(input("Enter your first input?"))
#sum = a-1
if (num %2)==0:
    print("This value is an even number:", num)
else:
    print("This value is an odd number:", num)

#Q9. Create a dictionary call scores for following.
            #"Rick Sanchez": 70,
             #"Morty Smith": 35,
             #"Summer Smith": 82,
             #"Jerry Smith": 23,
             #"Beth Smith": 98
     #Write a Python program that determines which student passed the class. Passing score is greater than or equal to 65.
dictionary = {"Rick Sanchez:":70,"Morty:": 35, "Summer Smith:": 82, "Jerry Smith:": 23, "Beth Smith:": 98}
#passingscore= int(input("What are the grades of each student?"))
for key, value in dictionary.items():
  if(value >=65):
      print ("The following people have passsed the class:",key,value)
for key, value in dictionary.items():
    if (value <65):
        print("The following students have failed the class:", key, value)


                

