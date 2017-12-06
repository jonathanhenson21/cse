# 12.4.17
# Write a Python function
# Which accepts the user's
# first and last name
# and print them in reverse order
# with a space between them.


def reverse_order(firstname, lastname):
    print("%s, %s" % (lastname, firstname))
    # print("%s, %s" % (last_name, first_name)) # Concatenation


# 12.5.17
"""Write a function called add_py
that takes out one parameter called "name"
and prints out name.py




example: 
add_py("John") == "John.py"" 
"""


def add_py(name):
    print("%s.py" % name)

# 12.6.17


"""Write a function called "add"
which takes three parameters
and prints the sum of the numbers
"""


def add(num1, num2, num3):
    print(num1 + num2 + num3)


add(15, 18, 9000)
add(80, 90, 100)
