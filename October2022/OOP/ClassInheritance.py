class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am a {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to say!\n")


class Dog(Pet):
    def speak(self):
        print("WOOF WOOF!\n")

class Cat(Pet):
    def speak(self):
        print("MEOW MEOW!\n")

class Fish(Pet):
        pass

p = Pet("Jerry", 2)
p.show(), p.speak()

d = Dog("Charles", 5)
d.show(), d.speak()

c = Cat("Lizzy", 3)
c.show(), c.speak()

f = Fish("Bubbles", 2)
f.show(), f.speak()

