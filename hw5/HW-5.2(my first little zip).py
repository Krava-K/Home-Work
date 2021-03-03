
name = ['Petya', 'Vasya', 'Nikolay']
age = [25, 35, 30]

for MyZip in ((name[i], age[i]) for i in range(min(len(name), len(age)))):
    print(MyZip)