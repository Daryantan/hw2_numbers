# hw_7.1
#  Вітання
# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int).Функція має повернути рядок.
# Замініть pass на Ваше рішення.
# def say_hi(name, age):
#   pass
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

# def say_hi(name, age):
#   return f"Hi. My name is {name} and I'm {age} years old"
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')



# hw_7.2
# Модифікувати рядок
# На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так,
# щоб вони завжди починалися з великої літери та закінчувалися крапкою.
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою
# Вхідні аргументи: string.
# Вихідні аргументи: string.
# Замість pass необхідно написати Ваше рішення.
# def correct_sentence(text):
#      pass
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')


def correct_sentence(text):
  if text[-1] == ".":
    text = text[0].upper() + text[1:]
    res = f"{text}"
  else:
    text = text[0].upper() + text[1:]
    res = f"{text}."
  return res

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')