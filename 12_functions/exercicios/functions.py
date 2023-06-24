def menor(n1,n2,n3):
    if n1<n2 and n1<n3:
        return n1
    elif n2<n3:
        return n2
    else:
        return n3

def fatorial (n):
    soma = 1
    for i in range(n,0,-1):
        soma *= i
    return soma

def vertical(palavra):
    for i in range(len(palavra)):
        print(f'{palavra[i]}')

vertical('joaozinho')

