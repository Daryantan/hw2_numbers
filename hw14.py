# hw_14.1
# Виняток користувача
# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента


class TooManyStudentsError(Exception):
    def __init__(self, message="You already have the maximum amount of students!"):
        self.message = message
        super().__init__(self.message)
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, Age: {self.age}, Name: {self.first_name} {self.last_name}"
        print(f"gender: {self.gender}, age: {self.age}, first name is: {self.first_name}, last name is: {self.last_name}")

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
       return super().__str__() + f", Record book: {self.record_book}"

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
try:
    for i in range(11):
        student = Student('Male', 20 + i, f'Student{i}', f'LastName{i}', f'AN{i}')
        gr.add_student(student)
except TooManyStudentsError as e:
    print(e)
# print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!