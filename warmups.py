# New python File: warmups.py

# 12.4.17
# write a python function
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space between them.


def reverse_order(Firstname, Lastname):
    print("%s, %s" % (Lastname, Firstname))
     #print("%s, %s" % (last_name, first_name)) # Concatenation

# 12.5.17


"""Write a function called add_py
that takes one parameter  called "name" 
and prints out name.py


example:
add_py("John") == "John.py"
"""

# 12.6.17
"""Write a function called "add"
which take three parameters
and print the sum of the number
"""


def add(num1, num2, num3):
    print(num1 + num2 + num3)


add(15, 18, 9000)
add(80, 90, 100)
