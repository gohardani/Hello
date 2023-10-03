
class Cup:
    def __init__(self):
        self.color = None
        self.content = None
        print(f"Cup is {self.color} and its content is {self.content}.")

    def fill(self, beverage):
        self.content = beverage
        print(f"Cup is {self.content}.")

    def empty(self):
        self.content = None
        print(f"Cup is {self.content}.")


redCup = Cup()
redCup.color = "red"
redCup.content = "tea"
redCup.empty()
redCup.fill("coffee")
