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