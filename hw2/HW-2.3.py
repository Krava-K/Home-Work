print ("Введите три числа!")
number1 = int(input("Число 1"))
number2 = int(input("Число 2"))
number3 = int(input("Число 3"))
i = 1

while i <= number3:
    if i % number1 == 0 and i % number2 == 0:
        print ("FB")
    elif i % number1 == 0:
        print("F")
    elif i % number2 == 0:
        print ("B")
    else:
        print(i)
    i = i + 1
