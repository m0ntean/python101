input = open("data.txt")
for line in input:
    print(line)
input.close()

file = open('test.txt', 'w')
file.write('This is the first line.\n')
file.close()