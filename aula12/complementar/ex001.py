from re import U


# def vogal (vogal):
#     if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal=='o' or vogal =='u':
#         return True
#     else:
#         return False

def vogal(letra):
    if letra in 'aeiouAEIOU':
        return True
    return False

letra = input()
print(vogal(letra))

frase = input('frase: ')
cont = 0 
for letra in range(len(frase)):
    if vogal(frase[letra]) == True:
        cont +=1
print(cont)