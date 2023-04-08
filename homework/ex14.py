from sys import argv

def celcius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f



print(argv)
print(type(argv))
script, first = argv
x = float(first)
y = celcius_to_fahrenheit(x)
print("The script is called:", script)
print(f"{x}C = {y}F")
