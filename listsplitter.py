print('Please enter the size of the list')
size = int(input())

print('Please enter the list you want to split it into a string')
List = []

n = 0
while n < size:
    print('Pleae enter input: ' + str(n))
    List.insert(n, input())
    n+=1

print('The list you have entered is')
print(List)

def s(l):
    string = ''
    check = all(isinstance(item, int) for item in l)
    if check == 'False':
        print('Your list contains numerical values')
    else:
        length = 0
        while length < len(l) - 2:
            string+= l[length] + ' , '
            length+= 1
        string+= l[-2] + ' and '
        string+= l[-1] + '.'
        
    return(string)        

print(s(List))
