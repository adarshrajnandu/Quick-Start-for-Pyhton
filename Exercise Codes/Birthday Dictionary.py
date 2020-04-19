# birthday dictionary

birthdays = {'Adarsh': 'May 8', 'R': '1993', 'Python': '1990'}

while True:
    print('Please enter the name: (to quite enter blank)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("We don't have the birthday details of " + name)
        print('Do you know the birthday of ' + name + '(type yes/no)')
        t1 = input()
        if t1 == 'yes':
            print('what is their birthday')
            bday = input()
            birthdays[name] = bday
            print('Birthday updated')  
        elif t1 == 'no':
            print('Do you want to continue: yes/no')
            t2 = input()
            if t2 == 'no':
                break
