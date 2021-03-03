file1 = open('number3.1.txt')
file2 = open('123.txt', 'w')

for s in file1:
    numbers = list(s.split())
    fizz = int(numbers[0])
    buzz = int(numbers[1])
    number = int(numbers[2])

    i =1
    while i <= number:
        if i % fizz == 0 and i % buzz == 0:
         file2.write("FB")
        elif i % fizz == 0:
            file2.write("F")
        elif i % buzz == 0:
            file2.write("B")
        else:
            file2.write(str(i))
        i += 1
    file2.write("")
file1.close()