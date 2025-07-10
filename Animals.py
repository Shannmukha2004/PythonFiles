class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print('Bow Bow')
class Cat(Animal):
    def make_sound(self):
        print('meow meow')
a=Dog()
a.make_sound()