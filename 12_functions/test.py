def compareTriplets(a, b):
    result=[0]*2
    for i in range(3):
        if a[i]>b[i]:
            result[0]+=1
        elif b[i]>a[i]:
            result[1]+=1
        else:
            None
    return result
            
a=[10,5,20]
b=[12,3,8]
print(compareTriplets(a,b))