# hw_6.1
# Діапазон букв
# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string
diap = input("Please, enter laters with '-': ")
letters = string.ascii_letters
first = diap[0]
last = diap[-1]
print(letters[letters.index(first):letters.index(last) + 1])



# hw_6.2
# Конвертер із числа в дату
# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години,
# хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин,
# хвилин, а те що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)
# Приклад:
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

# num = int(input("Please, enter quantity of seconds: "))
# if num < 8640000 and num >= 0:
#     days = num // 86400
#     hours = num % 86400 // 3600
#     minutes = num % 86400 % 3600 // 60
#     seconds = num % 86400 % 3600 % 60
#
#     if days < 5 and days > 1 or days < 25 and days > 31:
#         pdays = "дні"
#     elif days == 1 or days == 21 or days == 21 or days == 91:
#         pdays = "день"
#     else:
#         pdays = "днів"
#
#     days_str = str(days).zfill(2)
#     hours_str = str(hours).zfill(2)
#     minutes_str = str(minutes).zfill(2)
#     seconds_str = str(seconds).zfill(2)
#
#     print(days_str, " ", pdays, ',', " ", hours_str, ":", minutes_str, ":", seconds_str, sep="")
# else:
#     print("Ouups! incorrect value!")

# hw_6.3
# Добуток чисел
# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.
# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
# Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1
# print("Please, enter number: ")
# number = int(input())
#
# while number > 9:
#     multi1 = 1
#
#     while number > 0:
#         multi1 *= number % 10
#         number //= 10
#     number = multi1
#
# print("Result:", number)

