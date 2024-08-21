# hw_2.1

print("Please, enter 4-significant number: ")
number = int(input())
print(str(number))
n1 = number // 1000
n2 = number // 100 % 10
n3 = number % 100 // 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)

# hw_2.2

print("Please, enter 5-significant number: ")
number = int(input())
n1 = number//10000
n2 = number//1000 % 10
n3 = number % 1000//100
n4 = number % 100//10
n5 = number % 10
print(n5*10000+n4*1000+n3*100+n2*10+n1)
