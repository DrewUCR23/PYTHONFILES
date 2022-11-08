
#Q1. (5 pts) Consider following list of cities. 
#San Francisco, Los Angeles, Portland, Seattle, New York, Boston, Chicago, St#Louis, Dallas.
#Please show your input and output for following questions
#a) Create a list call cities with cities listed above
cities = ["San Francisco", "Los Angeles", "Seattle", "New York", "Boston", "Chicago", "St.Louis","Dallas"]
print("The 1st list:", cities)
#b) Sort the cities in alphabetical order
cities.sort()
print( "The sorted list:",cities)
#c) Print the city at location 4
print(cities[4])
#d) Print the cities at location 2 to 4
print(cities[2:4])
#e) Add Cincinnati to the list
cities.append("Cinnanti")
print("This is the updated cities list:", cities)
#f) Determine if Miami is in the list
miami_list = "Miami" in cities
print("Miami is not in the list and is:",miami_list)
#g) Sort the list in the reverse order
cities.sort( reverse = True)
print("This is sort in reverse:",cities)
#h) Determine the length of the list
print ("This length of the list is",len(cities))
#i) Add Denver to the beginning of the list without replacing existing item in #the beginning of the list.
#use the insert and the location of the value to insert it in the front of an item
#insert is useful for inserting a new item at the index of 0 location within the given set
cities.insert(0,"Denver")
print("This is the new list with denver:",cities)
#Q2. (5 pts) Suppose first and last are names. Write the code that prints them with first initials swapped. For example, if first = "Monty" and last = "Python" 
#the code will print Ponty Mython.

first = "Drew"
Last = "Gonzales"
new_first = first.replace("D", "G")
new_Last = Last.replace("G", "D")
print("Original Name:",first+"   "+ Last)
print("New Name:", new_first+ "  "+ new_Last)
#Q3. (5 pts) Write the code that asks user for the length and height of a 
#rectangle and prints the area of that rectangle.
a = int(input("What is the length of the rectangle?:"))
b= int(input("What is the height of the rectangle?:"))
calculation = a*b
print("This is the area of the rectangle:", calculation)
#Q4. (5 pts) The variable inches hold an integer number of inches. Write the  code that prints the equivalent number of feet and inches. So, if inches = 29
#your code should print 2 feet, 5 inches.
a1= int(input("How many inches you want to put in?"))
calculation = a1/12
print("The number of inches put in:", a1)
print("The amount of inches converted to feet is:",calculation)
#Q5. (5 pts) Write the code that asks a user for his/her name and age and prints that 2020+age will be a great year. If their name is Mickey and their 
#age is 19 the output of your program should exactly match the following.
#Please tell me your name: Mickey
##How old are you, Mickey? 19 
#Then 2039 will be your year!
a2 = input("What's your first and last name?")
print(a)
b1 = int(input("What's your age?"))
c= 2020
print(b1)
print("Then", c+b1, "will be your year!") 
#Q6. (5 pts) We all know that 360◦ = 2π radians. Write the code that asks the 
#user to input an integer number of degrees, converts it to radians, and prints the result. (An approximate answer is fine.)
import math
a3 = float(input("What is the number of degrees you wish to put in and convert to radians?"))
print("The number of degrees is:",a3)
CalculationCon = a3* math.pi/180
print("The numbers of degrees converted to radians is:", CalculationCon)
#Q7. (5 pts) Suppose mystring is a string containing an odd number of letters. 
#Write the code segment that would print its middle character to the screen.
mystring = 'drewa'
print("A string with an odd set of numbers:", mystring)
print("The middle character is:",mystring[2])
#Q8. (5 pts) Create a dictionary that maps the following countries to their 
#respective capitals. The capitals are indicated in parenthesis beside the 
#country names below.
#USA(Washington D.C#
#United Kingdom(London)
#China(Beijing)
#Japan(Tokyo)
#France(Paris#
countries = {'Washington DÇ': 'USA' , 'London':'United Kingdom', 'Bejing':'China', 'Tokyo': 'Japan', 'Paris':'France'}
print(countries)
#a) Delete the third country from the dictionary and print the dictionary
del countries['Bejing']
print("The dictionary with 3rd country deleted:",countries)
#b) Add Germany(Berlin) to the dictionary and print the dictionary 4
#adding a new item to the dictionary is done by creating a value and a new key.
#note if a dictionary does not have key values then it is defined as a set rather than a dictionary
countries1 = {'Washington D.C': 'USA', 'United Kingdom(London)':'London', 'Bejing':'China', 'Tokyo': 'Japan', 'Paris':'France'}
countries1['Berlin'] = 'Germany'
print("The dictinary with germany added",countries1)
#Q9. (5 pts) Write print command that prints out following. Your code must 
#use ‘ ‘ ‘ ‘ ‘ ‘to contain all code within one statement

#Use multiple '''''to promote a longer print statement
print('''''Date:
 December 25,2022,
 11:50 PM
Venue:
Convention Center
Number of guests: 200''''')
#Date:
#December 25, 2022
#Time:
#11:50 PM
#Venue:
#Convention Center
#Number of guests:
#200
##refer to last lecture for this portion of code.
#Q10. (5 pts) Write a python code call message that prints out following 
#using place holders and .format( ) method
#The price of this Apple laptop is 1299 USD and the exchange rate is 1 USD to 
#1.320 Canadian dollar
laptop = 'Apple'
price = 1299
exchangeRate = 1.320

Message = "(Format Method)The price of this {0:s} laptop is {1:d} USD and the exchange rate is 1 dollar to {2:1.3} Canadian dollars.".format(laptop,price,exchangeRate)
print(Message)
laptop2 = "Apple"
ER= 1.320
p = 1299
message1 = "(Using placeholder method )The price of this %s laptop is %d USD and the exchange rate is  1 dollar to  %1.3f Canadian dollars." %(laptop2,p,ER)
print(message1)
#You must use place holder for name of the laptop = Apple, the price =1299
#and the exchange rate is 1 USD to 1.320 Canadian dollar
