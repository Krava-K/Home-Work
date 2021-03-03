my_file = open('number3.1.txt', 'r')
for s in my_file:
    number = list(map(int, s.split()))
    for a in number:
        fizz = int(number[0])
        buzz = int(number[1])
        c = int(number[2])
        for i in range(1, c+1 ):
            if i % fizz == 0:
                print('Fizz')
            elif i % buzz == 0:
                print('Buzz')
            elif i % fizz == 0 and 1 % buzz ==0:
                print('FizzBuzz')
            else:
                print (i)
