class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, Name: {self.first_name} {self.last_name}"
        print(f"gender: {self.gender}, age: {self.age}, first name is: {self.first_name},"
              f" last name is: {self.last_name}")
