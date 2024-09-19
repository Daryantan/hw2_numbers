# hw_10.1
# Генераторна функція
# Реалізуйте генераторну функцію (з використанням оператора yield),
# яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача.
# Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та
# кількість членів, що видаються послідовності (n). Генератор повинен зупинити свою роботу з досягнення n-го члена.
# Підказка: це завдання дуже схоже на нескінченний лічильник з матеріалів лекції!
# Потрібно лише обмежити кількість видаваних генератором значень!
# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     ....
#     yield begin
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')
import re


# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     curr = begin
#     for _ in range(end):
#         yield curr
#         curr = func(curr)
#
#
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')


# hw_10.2
# Знайти перше слово
# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
# При розв'язанні задачі зверніть увагу на наступні моменти:
# У рядку можуть зустрічаються крапки та / або коми.
# Рядок може починатися з літери або, наприклад, з пробілу
# або точки У слові може бути апостроф і він є частиною слова.
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
# Вихідні параметри: Рядок.

# def first_word(text):
#     """ Пошук першого слова """
#     pass
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

def first_word(text):
    """ Пошук першого слова """
    result = re.search(r"[a-zA-Z']+", text)
    if result:
        return result.group(0)
    return


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')