class Animal:
    def __init__(self, name, species, region):
        self.name = name
        self.species = species
        self. region = region
        is_extinct = False
    
    def eat(self):
        print("The animal is eating!")

    def sleep(self):
        print("The animal is sleeping! shhhhhhh")

    def mating(self):
        print("The animal is mating.")

class Lion(Animal):
    def __init__(self, name, species, region):
        super().__init__(name, species, region, is_extinct)
        self.name = name
        self.species = species
        self. region = region
        self.extinct = is_extinct


class Rabbit(Animal):
    def eat(self):
        print("The rabbit is eating a carrot...")

class Bear(Animal):
    def sleep(self):
        random_number = random.randint(1,10)
        if random_number == 7:
            print ("The bear is hibernating!")
        else:
            print("It isn't winter yet!")


simba = Lion ("Simba", "Cat", "Africa")
bugs_bunny = Rabbit("Bugs Bunny", "Rabbit", "America")
yogi_bear = Bear("Yogi Bear", "Bear", "Northwest")

simba.eat()
bugs_bunny.eat()
yogi_bear.sleep()

simba.is_extinct = True
print (simba.is_extinct)
