
class Animal:
    """
    Inheritage
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow.")

cat = Cat("Koshen", "Domestic Shorthair")
print(cat.name)
cat.eat()
cat.meow()

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof.")

    def eat(self):
        print(f"{self.name} is eating dog food.")


dog = Dog("Raki", "Domestic")
print(dog.name)
dog.bark()
dog.eat()