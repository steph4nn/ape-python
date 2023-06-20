vetor = [None]*5

def Preencher(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input())

def Media(vetor):
    return sum(vetor)/len(vetor)

def Comparative(vetor, numero):
    num = 0
    for i in range(len(vetor)):
        if vetor[i] < numero:
            num+=1
    return num

Preencher(vetor)
print(vetor)
media = Media(vetor)
print(media)
print(Comparative(vetor,media))

