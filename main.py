# lesson_1
# print("Hello world!")

# lesson_2
# Змінна – це абстрактне місце зберігання даних у мові програмування, що має імʼя.
# type - функция, которая показывает тип переменной



# lesson_3

is_valid = False
print(is_valid)
print(not is_valid) # not -> інверсія, якщо значення False стане True, і навпаки

print("hello" in "hello, world!") # проверяет, есть ли слово в предложении, и если да, то выводит true, иначе false

user_select = int(input())
match user_select:
    case 1:
        print("Starting game...")
    case 2:
        print("Settings")
    case 3:
        print("Saved game")
    case 4:
        print("Exit")
    case _:
        print("Invalid input, please try again")