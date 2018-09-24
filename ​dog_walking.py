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
        if all([dog.is_hungry for dog in self.pets_list]):
            return "My dogs are hungry."
        return "My dogs are not hungry"

    def feed_all(self):
        for dog in self.pets_list:
            if dog.is_hungry is True:
                dog.eat()
        return "My dogs are not hungry"

    def walk(self):
        for dog in self.pets_list:
            print(dog.walk())


class Dog:
    number_of_dogs = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        Dog.number_of_dogs += 1

    def __str__(self):
        return "{} is {}.".format(self.name, self.age)

    @classmethod
    def number(cls):
        return "I have {} dogs".format(Dog.number_of_dogs)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)


dog1 = Dog('Tom', 6)
dog2 = Dog('Fletcher', 7)
dog3 = Dog('Larry', 9)
pets = Pets(dog1, dog2, dog3)

print(Dog.number())
print(pets)
print(pets.check_all())
print(pets.feed_all())
print(pets.check_all())
