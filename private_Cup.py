
class Cup:
    def __init__(self, color):
        self.color = color  # protected variable
        self.__content = None  # private variable
        print(f"Cup is {self.color} and its content is {self.__content}.")

    def fill(self, beverage):
        self.__content = beverage
        print(f"Cup is {self.__content}.")

    def empty(self):
        self.__content = None
        print(f"Cup is {self.__content}.")


redCup = Cup("red")
redCup.color = "red"
redCup.__content = "tea"
redCup.empty()
redCup.fill("coffee")
