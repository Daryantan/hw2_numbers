# hw_11.1
# Генератор простих чисел
# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа.
# Верхня межа цього діапазону визначається параметром цієї функції.
# Наприклад, виклик функції
# list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7] .
# Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд
# def prime_generator(end):
#     pass
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# # print('Ok')
# def prime_generator(end):
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     for num in range(2, end + 1):
#         if is_prime(num):
#             yield num
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
#
# print('Ok')


# # hw_11.2
# Напишіть функцію-генератор generate_cube_numbers, яка формує набір кубів чисел,
# починаючи з числа 2 до вказаної Вами величини. Тобто.
# генератор повинен працювати доти, поки генерується значення менше зазначеної величини.
# Нагадую, що вийти із генератора можна за допомогою return без параметрів.
# def generate_cube_numbers(end):
#     n = 2
#     while True:
#         cube = n ** 3
#         if cube > end:
#             return
#         yield cube
#         n += 1
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
#
# print('Ok')

# hw_11.3
# Перевірка на парність.
# Завдання ускладнюється.
# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне, або False якщо число непарне,
# але при цьому НЕ МОЖНА використовувати ділення у функції, та дії пов('язані з ним.
# Тобто. заборонено використовувати /, //, % та divmod)
# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)
# Вхідні дані: Ціле число.
# Вихідні дані: True або False
# def is_even(number):
#     pass
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'

def is_even(number):
    return (number & 1) == 0

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print('OK')
