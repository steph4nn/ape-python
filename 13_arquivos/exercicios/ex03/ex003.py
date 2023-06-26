filename = input()
string = input()

file = open(filename,'a+' )
file.write(string)
file.seek(0)
print(file.read())

file.close()

