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

import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_square = self.get_square() + other.get_square()
            # Новий прямокутник зі співвідношенням сторін оригіналу r1
            aspect_ratio = self.width / self.height
            new_width = math.sqrt(total_square * aspect_ratio)
            new_height = total_square / new_width
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_square = self.get_square() * n
            aspect_ratio = self.width / self.height
            new_width = math.sqrt(new_square * aspect_ratio)
            new_height = new_square / new_width
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __str__(self):
        return f"Rectangle: width={self.width:.2f}, height={self.height:.2f}, square={self.get_square():.2f}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

