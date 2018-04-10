# Defining a class
# class Cheeseburger(object):
#     def __init__(self, patty, cheese):  # TWO underscores before and after
#         self.patty = patty
#         self.cheese = cheese
#         self.eaten = False
#
#     def give(self, name):
#         print(name + "is thankful")
#
#     def cut(self):
#         print("you cut the cheeseburger")
#
#     def eat(self):
#         print("you eat the Cheeseburger")
#         self.eaten = True
#
#
# burger1 = Cheeseburger("beef", "havarti")
# burger2 = Cheeseburger("bacon", "swiss")
#
# print(burger1.eaten)
# print(burger2.eaten)
#
# burger1.eat()
# print(burger1.eaten)
# print(burger2.eaten)

class Car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.color = color
        self.door = num_of_doors
        self.running = False
        self.hp = hp
        self.name = name
        self.air_conditioning = True

    def true_on(self):
        if self.running:
            print("nothing happens.")
        else:
            self.running =True
            print("the car starts.")

    def move_forward(self):
            if self.running:
                self.running = False
                print("you turn the car off")
            else:
                print("the car is already off")
def go_for_drive(self,passengers):
    print("%d passengers get in." % passengers)
    self.passengers = passengers
    self.trun_on()
    self.forward()
    self.forward()
    self.forward()
    self.turn_off()
    passengers("%d passenger get out." % passengers)
    self.passengers = 0
my_Car = Car("dodge_challenger_demon", "red", 300, 99999999)
