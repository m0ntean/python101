while True:
    try:
        x = int(input('Please enter number:'))
        print(1 / x)
        break 
    except:
        print('error')
        print("Oops! That was no valid number. Try again")