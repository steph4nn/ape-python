ORDEM = int(input())

def gerarMatriz(ORDEM):
    matriz = [[None]*ORDEM for i in range(ORDEM)]
    return matriz

def printMatriz(matriz):
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            print(f'{matriz[linha][coluna]:4}', end='')
        print('')

def somaMatriz(matrizA, matrizB):
    matrizC =[]*len(matrizA)
    for linha in range(ORDEM):
        for coluna in range(ORDEM):
            matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
    return matrizC