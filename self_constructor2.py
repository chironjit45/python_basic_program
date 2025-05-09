class Student:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an object of Student
student1 = Student("Rahim", 20)

# Call the method
student1.display_info()
