#  print ("Hello World")
#
# # nathan
#
#  a = 4
#  b = 3
#  c = 9
#
#  print( a + b )
#
#  print( c * b - a )
#
#  print( c** a / b )
#
#  print(13 % 12)
#
#  #  the "%" sign is a modulus. if finds the reminder
#
#  car_name = "the bat car"
#  car_type = "bmw"
#  car_cylinders = 8
#  car_mpg = 5000.9
#
#  print ("I have a car %s. it's pretty nice." % car_name )
#  print ("I have a car called %s." % (car_name, car_type)) # watch the order
#  print ("what is your name?")
#
#  name = input (">_ ")
#  print ("hello %s," % name )
#
#  print ("hello %s," % name )
#
#  age = input ("how are old you?")
#
#  print ("%s?! that's old really old. you belong in a retirment home.")
#
#
#  Function
#
#
#    def print_hw() :
#       print("hello world")
#       print ("enjoy the day.")
#
#
#  print_hw()
#
#
#
#  def say_hi(name):
#    print("helo %s" % name)
#      print ("coding is great!")
#
#  say_hi("Jonathan")
#
#
#  def print_age ( name, age):
#      print ("%s is %d years old" % (name, age))
#      age = age + 1
#      print("next year, %s will be %d years old" % ( name, age ))
#
#  print_age("Nathan", 14)
#
#
#
#  def algebra_hw(x) :
#      return x**3 + 4*x**2 + 7 * x - 4
#  print (algebra_hw(3))
#  print (algebra_hw(4))
#  print (algebra_hw(5))
#  print (algebra_hw(6))
#  print (algebra_hw(7))
#
#
#
#  # if statements
#
#
#   def grade grade_calc(percentage):
#      if perceentage >= 90:
#      return"A"
#  elif percentage >= 80:
#      return "B"
#  elif percentage >= 70:
#      return "C"
#  elif pecentage >= 60:
#      return "D"
#
#  else:
#      "F"
#      print(gread_calc(59)


""" write a Fuction called "happy birthday"
that "sings" (prints) Happy Birthday
It must take one parameter called ("name")"""

#
# def happy_birthday(name):
#     print("happy birthday to you")
#     print("happy birthday to you")
#     print("happy birthday dear " + name)
#     print("happy birthday to you ")
#
#
# happy_birthday("jordan")
#
# # Loop
# for num in range(10):
#         print(num + 1)
#
#
# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
# import random  # this should be on line 1
# print(random.randint(0, 1000))
#
# # Recasting
# c = '1'
# print(c == 1)
#
# # we have a string and int
# print(int(c) == 1)

# print(1 == 1)
# print(1 != 2)
# print(not False)

the_count = [1, 2, 3, 4, 5, 6, ]
cheeseburger_ingredients = ['cheese', " beef", "sauce", "sesame seed bun", "avocado", "onion", "bacon", ]
print("cheeseburger_ingredients{0}")
print("sesame seed bun is the best bread ever")
print(len(cheeseburger_ingredients))

for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)
# # for item in the_count:
#      print(item)
for item in the_count:
    print(item * 2)

length = len(cheeseburger_ingredients)
range(5)
range(len(cheeseburger_ingredients))
for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("the item at index %d is %s" % (num, item))
strOne = "hello world!"
listOne = list(strOne)
print(listOne)
listOne[-1] = '.'

print(listOne)
cheeseburger_ingredients.append("fries")

# remove things from a list
cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

import string
print(string)
print(string.ascii_lowercase)
print(string.punctuation)

# making things lowercase
strTwo = "This Is A VeRY Odds sEnTeNCE"
lowercase = strTwo.lower()
print(lowercase)
