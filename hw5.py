# hw_5.1
# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

text = '_'
# text = '__'
# text = '___'
# text = 'x'
# text = 'get_value'
# text = 'get value'
# text = 'get!value'
# text = 'some_super_puper_value'
# text = 'Get_value'
# text = 'get_Value'
# text = 'getValue'
# text = '3m'
# text = 'm3'
# text = 'assert'
# text = 'assert_exception'

is_valid = True

if text in keyword.kwlist:
    is_valid = False

if text[0].isdigit():
    is_valid = False

for sgn in text:
    if sgn == ' ':
        is_valid = False


for char in text:
    if char in string.punctuation.replace('_', ''):
        is_valid = False
    if char.isupper():
        is_valid = False

if '__' in text or '___' in text:
    is_valid = False
print(is_valid)


# hw_5.2
# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

# while True:
#     print("Do you want to continue?")
#     print("Please, enter Yes, if you want, or No to exit.")
#     answer = input().lower()
#
#     if answer == 'yes' or answer == 'y':
#         print("Please, enter first number: ")
#         a = int(input())
#         print("Please, enter second number: ")
#         b = int(input())
#         print("Please, enter number of action: ")
#         print(" 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division")
#         action = int(input())
#
#         if action == 1:
#             print("Result:", a + b)
#         elif action == 2:
#             print("Result:", a - b)
#         elif action == 3:
#             print("Result:", a * b)
#         elif action == 4:
#             if b == 0:
#                 print("Oops! Division by zero is impossible!")
#             else:
#                 print("Result:", a / b)
#         else:
#             print("Invalid option, please, try again.")
#
#     elif answer == 'no' or answer == 'n':
#         print("Exiting the calculator. Goodbye!")
#         break
#
#     else:
#         print("Invalid option, please, try again.")

# hw_5.3
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
# 't!e@s#t t%e^s&t' => #TestTest

# #my_str = "Python Community"
# my_str = "i like python community!"
# #my_str = "Should, I. subscribe? Yes!"
# #my_str = "t!e@s#t t%e^s&t"
# nstr = ''
# my_str = my_str.title()
#
#
# i = 0
# for let in my_str:
#     if let !='!' and let !=',' and let !='@' and let !='.' and let !='?' and let !='#' and let !='^' and let !='%' and let !='&' and let !=' ':
#         nstr = nstr + let
#         i += 1
# if len(nstr)<140:
#     print("#" + nstr, sep='')
# else:
#     len(nstr)//2
#     print("#" + nstr, sep='')