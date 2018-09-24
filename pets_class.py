class Pets:

    def __init__(self, *args):
        self.dog1 = args[0]
        self.dog2 = args[1]
        self.dog3 = args[2]
        self.pets_list = [self.dog1, self.dog2, self.dog3]

    def __str__(self):
        return "{}\n" \
               "{}\n" \
               "{}\n" \
               "and they are mammals, of course".format(self.dog1, self.dog2, self.dog3)

    def check_all(self):
        if all([self.dog1.is_hungry, self.dog2.is_hungry, self.dog3.is_hungry]):
            return "My dogs are hungry."
        return "My dogs are not hungry"


class Dog:
    number_of_dogs = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        Dog.number_of_dogs += 1

    def __str__(self):
        return "{} is {}".format(self.name, self.age)

    @classmethod
    def number(cls):
        return "I have {} dogs".format(Dog.number_of_dogs)

    def eat(self):
        self.is_hungry = False

