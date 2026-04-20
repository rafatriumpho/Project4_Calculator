def add(x, y):
    answer = x + y
    print (answer)

def subtract(x, y):
    answer = x - y
    print (answer)

def multiply(x, y):
    answer = x * y
    print (answer)

def divide(x, y):
    if y == 0:
        print ('You can not divide by 0')
    else:
        answer = x / y
        print (answer)

print ('Welcome to the calculator! To start type in the number to the operator you want to use. Type "exit" to go back to menu at any time.')
while True:
    print ('\nMENU:')
    print ('1 - Add')
    print ('2 - Subtract')
    print ('3 - Multiply')
    print ('4 - Divide')
    operator = int(input('\nWhich operator do you want to use?\n'))
    if operator == 1:
        while True:
            numb1 = input('Type in a number:')
            if numb1.lower() == 'exit':
                break
            numb2 = input('Type in another number:')
            if numb2.lower() == 'exit':
                break
            else:
                numb1 = float(numb1)
                numb2 = float(numb2)
                add(numb1, numb2)
    elif operator == 2:
        while True:
            numb1 = input('Type in a number:')
            if numb1.lower() == 'exit':
                break
            numb2 = input('Type in another number:')
            if numb2.lower() == 'exit':
                break
            else:
                numb1 = float(numb1)
                numb2 = float(numb2)
                subtract(numb1, numb2)
    elif operator == 3:
        while True:
            numb1 = input('Type in a number:')
            if numb1.lower() == 'exit':
                break
            numb2 = input('Type in another number:')
            if numb2.lower() == 'exit':
                break
            else:
                numb1 = float(numb1)
                numb2 = float(numb2)
                multiply(numb1, numb2)
    elif operator == 4:
        while True:
            numb1 = input('Type in a number:')
            if numb1.lower() == 'exit':
                break
            numb2 = input('Type in another number:')
            if numb2.lower() == 'exit':
                break
            else:
                numb1 = float(numb1)
                numb2 = float(numb2)
                divide(numb1, numb2)
