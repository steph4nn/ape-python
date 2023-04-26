n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
rest = n1%n2

print(n1, n2)

while n1%n2 != 0:
    n1 = n2
    n2 = rest
    rest = n1%n2
    print(n2)