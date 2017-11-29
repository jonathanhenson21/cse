print ("Hello World")

 # nathan

a = 4
b = 3
c = 9

print( a + b )

print( c * b - a )

print( c** a / b )

print(13 % 12)

#  the "%" sign is a modulus. if finds the reminder

car_name = "the wiebe moble"
car_type = "bmw"
car_cylinders = 8
car_mpg = 5000.9

print ("I have a car %s. it's pretty nice." % car_name )
print ("i have a car called %s." % ( car_name, car_type))











#Function


 def print_hw() :
     print("hello world")
     print ("enjoy the day.")


print_hw()



def say_hi(name):
    print("helo %s" % name)
    print ("coding is great!")

say_hi("Jonathan")


def print_age ( name, age):
    print ("%s is %d years old" % (name, age))
    age = age + 1
    print("next year, %s will be %d years old" % ( name, age ))

print_age("Nathan", 14)



def algebra_hw(x) :
    return x**3 + 4*x**2 + 7 * x - 4
print (algebra_hw(3))
print (algebra_hw(4))
print (algebra_hw(5))
print (algebra_hw(6))
print (algebra_hw(7))




 # if statements


 def grade grade_calc(percentage):
    if perceentage >= 90:
    return"A"
elif percentage >= 80:
    return "B"
elif percentage >= 70:
    return "C"

elif pecentage >= 60:
    return "D"

else:
    "F"