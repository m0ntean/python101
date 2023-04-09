while True:
    try:
        
        x = int(input('Enter number1:'))
        a = int(input('Enter number2:'))
        b = int(input('Enter number3:'))
        c = int(input('Enter number4:'))
        e = int(input('Enter number5:'))
        print('We got', [x, a, b, c, e,] )
        break
    except:
        print('Try again')