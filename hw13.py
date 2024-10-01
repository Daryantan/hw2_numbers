# hw_13.1
# Група студентів
# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об('єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.)
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# Нижче наведені заготовки, які необхідно доповнити.
# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         pass
#
#     def __str__(self):
#         pass
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         pass
#
#     def __str__(self):
#         pass
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         pass
#
#     def find_student(self, last_name):
#         pass
#
#     def __str__(self):
#         all_students = ''
#         ...
#         return f'Number:{self.number}\\n {all_students} '
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!

# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Gender: {self.gender}, Age: {self.age}, Name: {self.first_name} {self.last_name}"
#         print(f"gender: {self.gender}, age: {self.age}, first name is: {self.first_name}, last name is: {self.last_name}")
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#        return super().__str__() + f", Record book: {self.record_book}"
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#         else:
#             print(f"Student with last name {last_name} not found.")
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = '\n'.join([str(student) for student in self.group])
#         return f'Group Number: {self.number}\nStudents:\n{all_students}'
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!
#


####
# hw_13.2
# Клас "Цифровий лічильник"
# Створити клас цифрового лічильника. У класі реалізувати методи:
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму.
# При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ
# метод step_down зменшує лічильник на 1.
# Метод можна викликати до тих пір, поки значення не досягне мінімуму.
# При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра класу.
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass
# class Counter:
#
#    def __init__(self, current=1, min_value=0, max_value=10):
#        self.current = current
#        self.min_value = min_value
#        self.max_value = max_value
#
#    def set_current(self, start):
#        self.current = start
#
#    def set_max(self, max_max):
#         pass
#
#    def set_min(self, min_min):
#        pass
#
#    def step_up(self):
#        pass
#
#    def step_down(self):
#        pass
#
#    def get_current(self):
#        return self.current
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e) # Достигнут максимум
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e) # Достигнут минимум
# assert counter.get_current() == 7, 'Test4'

class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       if self.min_value <= start <= self.max_value:
           self.current = start
       else:
           raise ValueError(f"Start value must be between {self.min_value} and {self.max_value}")

   def set_max(self, max_max):
       if max_max > self.min_value:
           self.max_value = max_max
       else:
           raise ValueError(f"Max value must be greater than min value {self.min_value}")



   def set_min(self, min_min):
       if min_min < self.max_value:
           self.min_value = min_min
       else:
           raise ValueError(f"Min value must be less than max value {self.max_value}")


   def step_up(self):
       if self.current < self.max_value:
           self.current += 1
       else:
           raise ValueError(f"You have reached the maximum! Maximum is: {self.max_value}")

   def step_down(self):
       if self.current > self.min_value:
           self.current -= 1
       else:
           raise ValueError(f"You have reached the minimum! Minimum is: {self.min_value}")

   def get_current(self):
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'

