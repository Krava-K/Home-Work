print ("How many times a day do you eat?")
number = int(input())

if (number >= 7):
    print ("Wow, need to eat less :) ")
elif ((number > 4) and (number < 7)):
    print ("Not bad, exactly what is need")
if (number <= 4):
    print ("No no no, you need to eat more!")