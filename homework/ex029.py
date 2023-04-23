while True:
    try:
        y = []
        for i in range(1, 6):
            x = float(input(f'Enter number{i}:'))
            y.append(x)
        print('We got', y )
        break
    except:
        print('Try again')