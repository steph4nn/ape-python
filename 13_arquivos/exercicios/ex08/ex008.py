file = open('CADASTRO.TXT', 'w')
n = int(input())
for i in range(n):
    name = input()
    sex = input()
    age = int(input())
    file.write(f'{name},{sex},{age}'+ '\n')
file.close()