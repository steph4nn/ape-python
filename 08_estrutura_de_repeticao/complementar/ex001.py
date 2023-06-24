n = int(input('Digite um número maior 1: '))

fna = 0
fn_at = 1

print(fna)
print(fn_at)

cont = 2

while cont < n:
    fnp = fn_at + fna
    print(fnp)
    fna = fn_at
    fn_at = fnp
    cont+=1



