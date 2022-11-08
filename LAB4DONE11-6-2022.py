#Q1. Write a python program that asking user for age and then if the age >21, then write output as "You are legal drinking age" 
#if younger than 21, write output as "You are a minor. You can't drink".
age = int(input("What is your age?"))
if (age>=21):
    print("You are legal drinking age!")
elif (age<21):
    print("You are a minor, You can't drink!")
#Q2.Create a list call banned_users that contains following persons. andrew, carole, david
#assign user = marie. Write a python conditional statement that prints following. 
#Marie, you can post a response if you wish.
username = input("What is your user name?!")
banned_users = ['Andrew', 'carole', 'david']
user = 'marie'
if user in username:
    print("Marie you can post a response if you wish!")
elif username in banned_users:
    print("You are banned and cannot respond")
#Q3. num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. 
#If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd = []
for num in num_list:
    if num % 2!=0:
        odd.append(num)
sum =0
count=0
for odd1 in odd:
 if count ==5:
     sum+=odd1
     count +=1
     print("This is an odd number list from num_list:",odd)
     print("This is the sum of 5 elements",sum)
 elif count<5:
      sum+=odd1
      count +=1
print("This is an odd number list from num_list:",odd)
print("This is the sum of 4 elements",odd[1]+odd[2]+odd[3]+odd[4])

#Q4. Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. 
#You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. 
#If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
#Remember that break works in both for and while loops. Use whichever loop seems most appropriate. 
#Consider adding print statements to your code to help you resolve bugs.
#characters
headline_list2 =["In 2008 The US faced problems because the world  was in financial disarray due to faulty loans given out", " ",""""that caused issuess This world is green and blue
 and all is not well in this world """]
new_ticker = ""
for items in headline_list2:
    new_ticker += " "+items
    if len(new_ticker) >=140:
        new_ticker = new_ticker[:140]
        break;
print(new_ticker)

#Q5. Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

#For instance, 6 has four factors: 1, 2, 3, 6.
#1 X 6 = 6
#2 X 3 = 6
#So we know 6 is not a prime number.
#In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

#If the numbers are prime, the code should print "[number] is a prime number."
#If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and 
#the number itself: "[factor] is a factor of [number]".
check_prime = [2,3,5,7]
pn = int(input("Enter a number to determine whether it is prime or not?"))
if pn in check_prime:
    print(pn, "is a prime number")
elif pn not in check_prime:
    for i in range(1, pn+1):
        if pn % i ==0:
            print("and a factor other than one", " factor {} is a factor of number {}".format(i,pn))
print(pn, "is not a prime number")

#Q6. Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. 
#I've included two test cases that you can use to verify that your function works correctly. Once you've written your function, use the Test Run button to test your code.
def population_density(n,a):
    population = n/a
    print(population)
    weeks= n/7
n = int(input("What is the population of the area:"))
a = float(input("What is the land area of this region:"))
population_density(n, a)
#Q7. Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
#For example, calling the function and printing the result like this:
#print(readable_timedelta(10))
#should output the following:
#1 week(s) and 3 day(s).
def readable_timedelta(a):
    weeks = int(a/7)
    days= a%7
    print( "{}: weeks and {}: days".format(weeks,days))
    #return readable_timedelta()
a= int(input("Enter your number of days you wish to convert:"))
readable_timedelta(a)
#Q8. Ask user to enter an integer and write a program to determine if divisibleby 2 using for loop. Be sure to print output whether a given number is divisible by 2
a = int(input("Enter a integer or number value?"))
if a % 2==0:
    print ("The integer is divisible by the value of 2")
else:
    print("The integer is not divisible by a value  of 2")
#Q9: Q9. Demonstrate print vs. return in functions by creating a function call show_plus_ten(num) which prints (num + 10) and 
#the other function call add_ten(num) where it returns (num + 10)
#using the print statement  and return statement

num= "num"
def add_ten(num):
    return(num)
print(add_ten(num),"+",10)
#using a print statement
def show_plus_ten(num):
   print(num,"+",10)
show_plus_ten(num)
#using a print statement
def show_plus_ten(num):
   print(num,"+",10)
show_plus_ten(num)
#Q10. Write a Python program that calculates factorial of user entered integer with following rules.
 #    a) No factorial for negative number
  #   b) zero factorial is equal to 1
   #  c) factorial is multiplication of all previous numbers up to the number. For example, 5 factorial (5!) is 1*2*3*4*5=120
    # Use If then statement and for loops
import math
integers = int(input("Enter your first integer!:"))
if integers<0:
    print("Sorry, their does not exist factorials for negative numbers!")
elif integers==0:
        print("The factorial for the following number is:", 1)
else:
    product = 1
    for factorial in range(1,integers+1):
         product *=factorial
         print("The factorial for the following number is using computation:",product)
print("This is the factorial using the factorial import math library",math.factorial(integers))
#Q11. Create a function call gain_weight with parameter weight & increase. Then use for loop to calculate weight for
#each week for 52 weeks with passing parameter of initial weight and initial amount of increase.
#Your output should look like below if you use initial weight of 140 pounds and 0.5 pounds each week.
#Week 1 is 140.5
#Week 2 is 141.0
#Week 3 is 141.5
#Week 4 is 142.0

def gain_weight(weight, increase):
    gain_weight = weight 
    for week in range(1,53):
        gain_weight += increase
        print('Week %s is %s' % (week,gain_weight))
gain_weight(140,0.5)
