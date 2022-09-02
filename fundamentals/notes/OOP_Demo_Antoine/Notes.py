#python is an oop language
#classes are blueprints for creating objects
#good practice to have class name singular and capitalized


class Animal:
    #constructor is the properties of the class           EARTH IS A DEFAULT VALUE (if you give a region was not lsited EARTH would act as default region)
    def __init__(self, name, species, region="EARTH"):
        self.name = name
        self.species = species
        self. region = region

    #Methods are just functions that exist inside a class...METHODS HAVE "self"
    def message (self):
        print("This one goes out to my homie Abby!")
        return self

    def add(self, num1, num2):
        print(f"{self.name} is doing arithmetic! {num1} and {num2} = {num1+num2}")
        return self

#here we are creating an object of the class Animal         ****Because a region is listed, Africa overrides the default value
lion = Animal("Lion", "Cat", "Africa")
penguin = Animal("Penguin", "Bird", "Antartica")
print(lion.name, lion.species, lion. region)

#calling the method, penguin=self, lion
# penguin.add (1,3)
penguin.message().add(7,3)

