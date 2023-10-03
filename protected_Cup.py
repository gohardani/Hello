
class Cup:
    def __init__(self):
        self.color = None
        self._content = None # protected variable
        print(f"Cup is {self.color} and its content is {self._content}.")

    def fill(self, beverage):
        self._content = beverage
        print(f"Cup is {self._content}.")

    def empty(self):
        self._content = None
        print(f"Cup is {self._content}.")


redCup = Cup()
redCup.color = "red"
redCup._content = "tea"
redCup.empty()
redCup.fill("coffee")
