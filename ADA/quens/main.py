import time
global num
num=[]
global row
row= [None]*100
global rdiag
rdiag=[None]*100
global ldiag
ldiag=[None]*100

def printmatriz(matriz,N):
    for fila in range(N):
        for valor in range(N):
            if(matriz[fila][valor]== 1):
                print('Q', end=" ") 
            if(matriz[fila][valor]== 0):
                print('*', end=" ")
        print()

def creaMatriz(n):
    matriz = []
    for i in range(n):
        a = [0]*n
        matriz.append(a)
    return matriz

def solucion(matriz,N,var):
    tmp1=None
    tmp2=None
    if(var==N-1):
        return 1
    for i in range (N):
        tmp1=num[var] - i +N
        tmp2=num[var] + i
        if(not(row[i]) and not(rdiag[tmp1]) and not(ldiag[tmp2])):
            matriz[i][num[var]]=1
            row[i]=1
            rdiag[tmp1]=1
            ldiag[tmp2]=1
            if(solucion(matriz,N,var+1)):
                return 1
            matriz[i][num[var]]=0
            row[i]=0
            rdiag[tmp1]=0
            ldiag[tmp2]=0
    return 0
    
def NQueens(matriz,N,x,y):
    matriz[x][y]=1
    row[x]=1
    rdiag[y-x+N]=1
    rdiag[x+y]=1
    if(not solucion(matriz,N,0)):
        return 0
    return 1


def nqueens_2(N,x,y):
    #Tamaño 
    #N=8
    #Posicion de la primera Reyna 
    #x=1
    #y=1
    
    matriz=creaMatriz(N)
    for i in range (N):
        if(i==y):
            continue
        num.append(i)
    
    inicio=time.time()
    NQueens(matriz,N,x,y)
    printmatriz(matriz,N)
    fin=time.time()
    return fin-inicio

print(nqueens_2(16,5,3))




''''
list = list(range(8))
perms = itertools.permutations(list)

num_comb = 0

for perm in perms:
    if put_queen(perm[0], 0) == True:
        if put_queen(perm[1], 1) == True:
            if put_queen(perm[2], 2) == True:
                if put_queen(perm[3], 3) == True:
                    if put_queen(perm[4], 4) == True:
                        if put_queen(perm[5], 5) == True:
                            if put_queen(perm[6], 6) == True:
                                if put_queen(perm[7], 7) == True:
                                    print_table()
                                    num_comb += 1
                                    print(f"solution{num_comb}")
                                    print(" ")
    table = [[0] * 8 for _ in range(8)]'''