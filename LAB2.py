#Q1. Create a list call cars that contains following car makers
#BMW, Chrysler, Ford, GM, Honda, Hyundai, Kia, Mercedes, Nissan, VW
carmaker = ["BMW", "Ford", "Chrystler", "Honda", "GM", "HYUNDAI", "KIA", "MERCEDES", "NISSAN", "VW"]
#a) print your list
print(*carmaker)
#b) print carmaker with index 1
print(carmaker[1])        
#c) print carmakers at index 3  and index 7
print(carmaker[3:7])
#d) print first three carmakers in the list
carmaker1= carmaker[0:3]
print(carmaker1)
#e) Explain why print(cars[-1]) will print VW
print(carmaker[-1])
print("Cars-1 prints VW because it registers the last item in the domain as the first item to be printed out therefore it recognizes -1 as 7 the first item to be printed")
#f) Add Tesla to the list using append
carmaker.append("Tesla")
#g) Add Porsche to the 3rd index using insert
carmaker.insert(3, 'Porsche')
#h) Delete Nissan from the list
del carmaker[8]
#i) Sort your list in alphabetical order
carmaker.sort
print("This list uses the sort method", carmaker)
#j) repeat your carmakers list three times and print output
print("The list output is printed 3 times",carmaker*3)
#k) print the length of your list
print(len(carmaker))
#l) Demonstrate sort() and sorted() using your carmakers list
carmaker.sort(reverse= True)
print("The sort method makes the values of the list be permanent",carmaker)
print ("The sorted method is a temporary change to the set,",sorted(carmaker))
print("I've been this a third time with sort to demonstrated that the change of sorted reverts,", carmaker)
print("I've kept sort in reverse to demonstrate the permanent list data vs the temporary state of sorted")
#m) Reverse your carmakers list in reverse alphabetical order
carmaker.reverse()
print("The sort method went from reverse alphabetical to alphabetical using .reverse", carmaker)
#n) Create a tuple call perfectNumber and add known perfect numbers to the list
 #tupples are used to store multiple items in a single variable and a tuple is uncahgeable similar to a constant
perfectNumber = (6,28,496,8128)
perfectNumber1 = (perfectNumber,8589869056)
print("A tupple with 4 perfect numbers:",perfectNumber)
print("A tupple with 5 perfect numbers",perfectNumber1)
#o) Try to add 2 to your list perfectNumber
perfectNumber = (6,28,496,8128,)
perfectNumber2 = (*perfectNumber1, 2)
print("This is a tupple with 2 added",perfectNumber2)
#2. Create a set call countries that contains following countries
countries =  {'Canada', 'USA', 'Mexico', 'France', 'Germany', 'UK', 'Russia', 'China', 'Japan', 'Korea', 'South Africa', 'UAE', 'India', 'Australia', 'India','Brazil'}
#print how many countries are in the set
print(len(countries))
print("Not sure the difference betwene how many countries and length: This number of countries is 15")
#b) Determine the length of the set
print("The length of this set is",len(countries))
#c) Display countries from index 0 to index 4    sort is permanent and sorted is temporary
sortedcountries = (sorted(countries))
print(sortedcountries[0:4])
#d) Sort your set
sortedcountries.sort()
print("I converted a set to a list. The output is:",sortedcountries)
#e) rename the set to country_set
country_set = set(countries)
print("The country is now a set again:",country_set)
#f) Using country_set, add country Ghana
country_set.add("Ghana")
print("The new set with Ghana added:",country_set)
#g) Determine if Argentina is in the set
arg_in_set =  "Argentina" in countries
print(arg_in_set)
#f) print updated set
country_set = sorted(countries)
country_set.append("Ghana")
country_set.sort()
print("This is the updated set no argentina is in the lst and alphabetical:", country_set)
#g) using pop() to remove country. Which country was removed?
countries_set = countries.pop()
print("The following country was removed from the set:",countries_set)
#Q3. Create a dictionary(map) with following content and name it
totalMedalOlympic2016 = {'USA': 216, 'CHINA': 70, 'GBR': 67, 'RUSSIA':57, 'GERMANY':  42, 'FRANCE':  42, 'JAPAN':  41, 'AUSTRIALIA':  29, 'ITALY':  28, 'CANADA':  22, 'KOREA': 21}          
#dictionary uses curly brackets
#Country		Total medals
#USA 		121
#China		70
#GBR		67
#Russia		57
#Germany	42
#France		42
#Japan		41
#Australia	29
#Italy		28
#Canada		22
#Korea		21
#a) Using keys to print the country
print("Using key method",totalMedalOlympic2016.keys())
#b) Using values to print medal counts
print("This is the total medal for one country: China: ",totalMedalOlympic2016.get('CHINA'))
print("This is the total medals for all the countries in the dictionary",totalMedalOlympic2016.values()) 
#c) Add brazil to dictionary with 19 medal counts
totalMedalOlympic2016["Brazil"] = 19
print("Brazils medal count shows I added brazil to the list",totalMedalOlympic2016.get("Brazil"))
#d) Print totalMedalOlympic2016 dictionary including last country Brazil
print("This is with brazil added",totalMedalOlympic2016)
#e) Determine if country Poland is in the dictionary. It must indicate whether it is true or false
pol_in_set =  "Poland" in totalMedalOlympic2016
print("Poland is not in the dictinary and is", pol_in_set)
#f) Use get method to retrieve Poland's medal count
x = totalMedalOlympic2016.get("Poland")
#is_null = x is None
print("Polands medal count is 0 or:", x)
#g) Use identity operator to check see if Poland is in the dictionary. Your answer should be either True or false
pol_in_set =  "Poland" in totalMedalOlympic2016
#pol_in_set in totalMedalOlympic2016
print("(identity operator)Poland is not in the set and is:", pol_in_set is  totalMedalOlympic2016)
#Q4. Create an array call array and add known perfect numbers to the list. Be sure that you import numpy and array
#import array as arr
#import numpy as np
#array = np.array([6, 28, 496, 8128])
#a) Divide array by 3
#print(array/division)
import array as arr
import numpy as np
division = 3
array = np.array([6, 28, 496, 8128])
output = np.divide(array, division)
print(output)
#b) Add 7 to the array
array = array+7
print(array)
#c) Multiply array by 13
array = array *13
print(array)
#d) Add number 144 to array
array = np.append(array,133)
print(array)
#e) Remove 8128 from array
array = np.delete(array, 3)
print(array)
#b) create a list call listPerfectNum and divide that list by 3. Do you get an error?
divide = 3
listPerfectNUM =[]
#print(listPerfectNUM/divide)
print(" Yes an error was given that is does not support the operand type for list and integer. Also, I would assume because their are no values in this list it would become undefined.")

#. Import turtle and draw two circles, two squares and draw a cirle and filled with red color
import turtle
#first circle change the positions with t.setx and t.sety
t = turtle.Pen()
t.penup()
t.setx(100)
t.pendown()
t.circle(100)

#second circle
t.penup()
t.setx(-200)
t.pendown()
t.circle(50)
#third circle
t.penup()
t.setx(200)
t.sety(-200)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(110)
t.end_fill()

#SQUARE 1
t.penup()
t.sety(-100)
t.setx(-100)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

#SQUARE 2
t.penup()
t.sety(100)
t.setx(-120)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

