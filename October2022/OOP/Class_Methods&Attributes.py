class Person:
    nr_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person() #    ->   class method
        # Person.nr_people += 1   ->   class attribute, we can call nr_people outside de def function

    @classmethod
    def number_of_people_(cls):
        return cls.nr_people # class method calls only to the class itself

    @classmethod
    def add_person(cls):
        cls.nr_people += 1


p1 = Person("Daniel")
# print(Person.nr_people)
p2 = Person("Negreanu")
# print(Person.nr_people)
print(Person.number_of_people_())


''' class Math:
        @staticmethod
            def add5()x:    ->>  static methods don't change anything, more for organisation
                return x + 5
print(Math.add5(10))  '''

'''
A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.

The difference between a static method and a class method is:

    Static method knows nothing about the class and just deals with the parameters
    Class method works with the class since its parameter is always the class itself.

The class method can be called both by the class and its object.
'''