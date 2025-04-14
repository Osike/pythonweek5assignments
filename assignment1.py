# class_exercises.py

# Activity 1: GirlFriendNasrah Class
class GirlFriendNasrah:
    def __init__(self, skin_color, age, name):
        self.skin_color = skin_color
        self.age = age
        self.name = name

    def galnas(self):
        print("She is a beautiful lady.")

come_over = GirlFriendNasrah(skin_color="brown", age="21", name="nasrah")

print(come_over.name)
come_over.galnas()
print(come_over.age)
print(come_over.skin_color)

# Activity 2: Animal Polymorphism
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Hyena(Animal):
    def make_sound(self):
        print("Hehehehehe!")

dog = Dog()
hyena = Hyena()

dog.make_sound()
hyena.make_sound()

animals = [dog, hyena]

for animal in animals:
  animal.make_sound()