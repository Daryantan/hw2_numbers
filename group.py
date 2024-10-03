import student
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
        else:
            print(f"Student with last name {last_name} not found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Group Number: {self.number}\nStudents:\n{all_students}'

class TooManyStudentsError(Exception):
    def __init__(self, message="You already have the maximum amount of students!"):
        self.message = message
        super().__init__(self.message)