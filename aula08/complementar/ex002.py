from operator import truediv


n = int(input('Digite um número: '))
cont = 1

while cont < n+1:
    if cont < 2:
        print(f'{cont} não é primo.') 
    elif cont%2 != 0 or n ==2:
        print(cont)
    cont+=1


qtde = int(input('Digite um número: '))

for i in range(1, qtde+1):
    if i<2:
        primo = False
    else:
        primo = True
        for k in range(2,i-1):
            if i%k==0:
                primo = False
                break
    if primo:
        print(f'{primo}')