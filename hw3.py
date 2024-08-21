# hw_3.1
# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма,
# виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!
print("Please, enter first number: ")
a = int(input())
print("Please, enter second number: ")
b = int(input())
print("Please, enter number of action : ")
print(" 1) Addition \n 2) Deletion \n 3) Multiplication \n 4) Division")
action = int(input())
match action:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        if b == 0:
            print("Ouups! Division by zero is impossible!")
        else:
            print(a/b)
    case _:
        print("Invalid option, please, try again")
