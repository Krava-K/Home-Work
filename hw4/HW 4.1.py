import random #импортируем рнадом

file1 = open('number5.1.txt', 'w') #открываем файл
numbers = [i for i in range(1,(random.randint(1, 240)))] #генерируем список с раномным крайним значение в приделе от 1 до 240

print('List generated and written to file.')

file1.write(' '.join(str(e) for e in numbers)) #записываем список в файл
file1.close() #закрываем файл

file2 = open('123(5.1).txt', 'w')

fizz = (3);
buzz = (5);

i = 1
for i in numbers:
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