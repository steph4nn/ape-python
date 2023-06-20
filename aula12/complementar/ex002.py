from calendar import prmonth


def primo(inteiro):
    for i in range(2,inteiro):
        if inteiro%i==0:
            return False
        else:
            return True

for i in range(1,101):
    if primo(i) == True:
        print(i)