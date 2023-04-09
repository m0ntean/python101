while True:
    try:
        x = input('Enter number1:')
        y = input('Enter number2:')
        x = int(x)
        y = int(y)
        print('The sum is', x + y)
    except:
        print(x, 'is not a number, try again')
        
        print(y, 'is not a number, try again')