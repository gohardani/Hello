
class Student:
    """
    # Simple data structure:
    # Create a class called "Student" that has attributes name and grade
    # and create a method called "display_info" to display the student's information.
    """
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"{self.name} got {self.grade} in Database.")


student1 = Student("Mostafa", 15)
student2 = Student("Ali", 18)

student1.display_info()
student2.display_info()
