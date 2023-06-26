filename = input()
string = input()

file = open(filename, 'w')
file.write(string)
file.close()

file = open(filename, 'r')
print(file.read())
file.close()
