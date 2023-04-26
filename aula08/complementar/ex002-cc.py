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
        print(f'{i}')