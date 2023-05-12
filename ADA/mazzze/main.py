import time

class Nodo:
    def __init__(self,x,y):#constructor
        self.x = x
        self.y = y
        self.dist = 1

    def __eq__(self, other):
        return self.x == other.x and self.y==other.y

    def __str__(self):
        return str(self.x)+"\t"+str(self.y)

def solvemaze(maze,ini,fin,paso=1):
    togo=[]
    secondchance=[]
    if ini==fin:
        maze[fin.x][fin.y]='Y'
        printm(maze)
        return True
    posiblemovements=[(-1,1),(-1,-1),(1,-1),(1,1),(0,1),(1,0),(-1,0),(0,-1)]
    mini=ini
    for item in posiblemovements:
        nexti=ini.x+item[1]
        nextj=ini.y+item[0]
        if(nexti>=0 and nextj>=0)and nexti<len(maze) and nextj<len(maze[0]):
            if maze[nexti][nextj]=='0':
                nextpos=Nodo(nexti,nextj)
                nextpos.dist=dista(nextpos,fin)
                if nextpos.dist<mini.dist:
                    mini=nextpos
                togo.append(nextpos)
    for a in togo:
        if(a.dist<=ini.dist):

            maze[a.x][a.y]=str(paso+1)
            if solvemaze(maze,a,fin,paso+1): return True
        else:
            secondchance.append(a)
    
    for a in secondchance:
        maze[a.x][a.y]=str(paso+1)
        if(solvemaze(maze,a,fin,paso+1)): return True

def dista(a,b):
    return (a.x-b.x)**2+(a.y-b.y)**2

def printm(maze):
    
    for a in maze:
        toprint=""
        for b in a:
            '''
            if b=='1':
                toprint+="-\t"
            else:
                toprint+=str(b)+"\t"
            '''
            if b=='0':
                toprint+="-\t"
            elif b=='X'or b=='x':
              toprint+="X\t"
            elif b=='Y' or b=='y':
              toprint+="Y\t"
            elif b=='1':
                toprint+="1\t"
            else:
                toprint+="*\t" 
        print(toprint)
    

def maze_2():
    start=time.time()
    maze=[]
    posini=0
    posfin=0

    mazes=[]
    puntos=[]
    try:
        for group in range(1,7):
            with open("maze_"+str(group)+".txt") as f:
                for i,line in enumerate(f):
                    linea=line.split('\n')[0].split('\t')
                    for it,a in enumerate(linea):
                        if a=='X':
                            posini=(i,it)
                        if a=='Y' or a=='y':
                            posfin=(i,it)
                            linea[it]='0'
                    maze.append(linea)
                puntos.append((Nodo(posini[0],posini[1]),Nodo(posfin[0],posfin[1])))
                mazes.append(maze[:])
                maze.clear()
    except:
        print(" ")

    for i in range(100):
      i = i*1
      if i%2==1:
        i=i*2
    for it,item in enumerate(mazes):
        ini,fin=puntos[it]
        fin.dist=0
        ini.dist=dista(ini,fin)
        if(not solvemaze(item,ini,fin)):
            print("no se encontró solucion")
            print("")
    end=time.time()-start
    return end
print(maze_2())

