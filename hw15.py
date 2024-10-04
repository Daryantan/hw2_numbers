# hw_15.1
# Клас Прямокутник


#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         pass
#
#     def __add__(self, other):
#         pass
#
#     def __mul__(self, n):
#         pass
#
#     def __str__(self):
#         pass
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

# import math
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.get_square() == other.get_square()
#         return False
#
#     def __add__(self, other):
#         if isinstance(other, Rectangle):
#             total_square = self.get_square() + other.get_square()
#             # Новий прямокутник зі співвідношенням сторін оригіналу r1
#             aspect_ratio = self.width / self.height
#             new_width = math.sqrt(total_square * aspect_ratio)
#             new_height = total_square / new_width
#             return Rectangle(new_width, new_height)
#         return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, (int, float)):
#             new_square = self.get_square() * n
#             aspect_ratio = self.width / self.height
#             new_width = math.sqrt(new_square * aspect_ratio)
#             new_height = new_square / new_width
#             return Rectangle(new_width, new_height)
#         return NotImplemented
#
#     def __str__(self):
#         return f"Rectangle: width={self.width:.2f}, height={self.height:.2f}, square={self.get_square():.2f}"
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
#
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'


# hw_15.2
# Клас «Правильний дріб»
# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання, віднімання та множення для екземплярів цього класу.
#
# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __mul__(self, other):
#         pass
#
#     def __add__(self, other):
#         pass
#
#     def __sub__(self, other):
#         pass
#
#     def __eq__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#     def __lt__(self, other):
#         pass
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
#
# assert f_d < f_c  # True
# assert f_d > f_e  # True
# assert f_a != f_b  # True
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2  # True
# print('OK')

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.b * other.b
            new_a = self.a * other.b + other.a * self.b
            return Fraction(new_a, common_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.b * other.b
            new_a = self.a * other.b - other.a * self.b
            return Fraction(new_a, common_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 21, 18', f"Expected 'Fraction: 21, 18', but got {str(f_c)}"


f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 6, 18', f"Expected 'Fraction: 6, 18', but got {str(f_d)}"


f_e = f_a - f_b
print(f_e)
assert str(f_e) == 'Fraction: 3, 18', f"Expected 'Fraction: 3, 18', but got {str(f_e)}"


assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True


f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
