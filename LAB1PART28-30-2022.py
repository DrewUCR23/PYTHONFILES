#p import statistics
import statistics 
a = input("Enter the first number:")
print(a)
b = input("Enter the second number:")
print(b)
c = input("Enter the third number:")
print(c)
alistl = (float(a),float(b), float(c))
alistl2 = (float(a),float(b), float(c))

x = statistics.mean(alistl)
z = statistics.median(alistl2)
print("The Mean is :", x)
print("The median is:", z),

#q q) Write python statement that demonstrates if a person is age older than 12 and less than 20 then the person is teenager. 
   #Assign person is 14 years old. Use logical operator to print result

age = input("Enter your age!:  ")
person = int(age)
if person > 12 and person < 20:
    print("This is person is a teenager!")
else:
       print("You are not a teenager!")
      
#r)  What is the result?
       a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
       b = set(a)
       print( len(a) - len(b))
       print("The answer is 6 which is the difference between set(a) 10 and b of 4.")
       #The result is 6 because len(a) is 10 numbers in the set - 4 integers= which is 6.
    

#S) Define a Dictionary, population that provides information on the world's largest cities. The key is the name of a city (a string), and the associated
   #value is its population in millions of people.
    #first_dict = ({1:'Shanghai Population: 17.8 m', 2: 'Instanbul Population 13.3 M', 3: 'Karachi Population: 13.0 M', 4: 'Mumbai Population: 12.5 M'})
    #print(first_dict)
       key_dict = { 'Cities: Shanghai':17.8 , 'Instanbul':13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
       print (key_dict['Cities: Shanghai'])
       print(key_dict)


#Q2) Compute and print the sum of 3 user entered numbers
       a= int(input("Put your 1st number here:"))
       b= int(input("Put your 2nd number here:"))
       c= int(input("Put your 3rd number here:"))
       print("Yor total sum is    " + str(a+b+c))

#Q3. Compute and print the sum of five user-entered numbers
       A = int(input("Enter your 1st number here: "))
       B= int(input("Enter your second number here:"))
       C = int(input("Enter your third number here: "))
       D= int(input("Enter your fourth number here: "))
       E = int(input("Enter your fifth number here: "))
       print("Your total sum is: " + str(A+B+C+D+E))
     
#Q4. Sum of user-entered number of numbers. (This is a bit challenging. You will need to use for loop. Try and see if you can make it work)
num = int(input('How many numbers?:     '))
total_num = 0
for n in range(num):
    numbers = float(input('Enter numbers: '))
    total_num += numbers
print('Sum of  ', num, 'number is  ', total_num)
           
#Q5. Average of user-entered number of numbers.(This is a bit challenging. You will need to use for loop. Try and see if you can make it work)
#average= total_sum/num
num = int(input('How many numbers?:     '))
total_num = 0
for n in range(num):
    numbers = float(input('Enter numbers:  '))
    total_num += numbers
print('Sum of  ', num, 'number is  ', total_num)
print("The average is", total_num/num)                                                      
           
#Q6. Median of five numbers.
import statistics 
a = input("Enter the first number:")
print(a)
b = input("Enter the second number:")
print(b)
c = input("Enter the third number:")
print(c)
d = input("Enter the fourth number:")
print(d)
e = input("Enter the fifth number:")
print(e)
alistl = (float(a),float(b), float(c), float(d),float(e))
#x = statistics.mean(alistl)
y = statistics.median(alistl)
print("The Median is :", y)

#Q7. Draw a shape using python turtle. You must draw different shape other than you saw in class. Also, draw a shape with filled color. 
#For example, draw an Octagon and filled with yellow color.
import turtle
t = turtle.Pen()
r = 50
###circle 
t.circle(r)

import turtle
t = turtle.Turtle()
t.fillcolor('black')
t.begin_fill()
for i in range(5):
  t.forward(300)
  t.right(90)
t.end_fill()       
        

           
          

