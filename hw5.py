


# hw_5.2
# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

# print("Please, enter first number: ")
# a = int(input())
# print("Please, enter second number: ")
# b = int(input())
# print("Please, enter number of action : ")
# print(" 1) Addition \n 2) Deletion \n 3) Multiplication \n 4) Division")
# action = int(input())
# match action:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4:
#         if b == 0:
#             print("Ouups! Division by zero is impossible!")
#         else:
#             print(a/b)
#     case _:
#         print("Invalid option, please, try again")



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

#my_str = "Python Community"
my_str = "i like python community!"
#my_str = "Should, I. subscribe? Yes!"
#my_str = "t!e@s#t t%e^s&t"
nstr = ''
my_str = my_str.title()


i = 0
for let in my_str:
    if let !='!' and let !=',' and let !='@' and let !='.' and let !='?' and let !='#' and let !='^' and let !='%' and let !='&' and let !=' ':
        nstr = nstr + let
        i += 1
if len(nstr)<140:
    print("#" + nstr, sep='')
else:
    len(nstr)//2
    print("#" + nstr, sep='')