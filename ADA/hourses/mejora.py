def horse_2 (n,x,y):
  from time import time 
  t = [];
  N = n;
  NCUAD = N*N;
  pos_en_x = x;
  pos_en_y = y;

  filas = N;
  columnas = N;
  #_kmoves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)) 
  h = [ 2, 1, -1, -2, -2, -1,  1,  2];
  v = [ 1, 2,  2,  1, -1, -2, -2, -1];
  '''def knightmoves(board, P, boardsize=boardsize):
      Px, Py = P
      kmoves = set((Px+x, Py+y) for x,y in _kmoves)
      kmoves = set( (x,y)
                    for x,y in kmoves
                    if 0 <= x < boardsize
                      and 0 <= y < boardsize
                      and not board[(x,y)] )
      return kmoves'''
  iter = [0];
  def crear_matriz(Matriz):
      for inicializar in range(filas):
          Matriz.append([0]*columnas)

      for i in range(filas):
          for j in range(columnas):
              Matriz[i][j]=0;
  crear_matriz(t);
  def camino_spirit():
      q=[False];
      t[pos_en_x][pos_en_y] = 1;
      changes(2, pos_en_x, pos_en_y, q);
      imprimir_matriz(t);
  def calculo(x,y,ops):
      for i in range(8):
          xn1 = x + h[i];
          yn1 = y + v[i];
          if (xn1 >= 0 and xn1 < N and yn1 >= 0 and yn1 < N):
              if t[xn1][yn1] == 0:
                  ops.append([0,i]);
                  for j in range(8):
                      xn2 = xn1 + h[j];
                      yn2 = yn1 + v[j];
                      if xn2 >= 0 and xn2 < N and yn2 >= 0 and yn2 < N:
                          if t[xn2][yn2] == 0:
                              ops[len(ops)-1][0] +=1;
      for i in range(1000):
        i+=2
      ops.sort();
  def changes(i,x,y,q):
      ops = [];
      calculo(x,y,ops);
      m=0;
      q[0]=0;
      while (~q[0]==-1) and (m < len(ops)):
          xn = x + h[ops[m][1]];
          yn = y + v[ops[m][1]];
          if (xn < N) and (yn < N):
              if t[xn][yn] == 0:
                  t[xn][yn] = i;
                  if i < NCUAD:
                      changes(i + 1, xn, yn, q);
                      if ~q[0] == -1:
                          t[xn][yn] = 0;
                  else:
                      q[0] = 1;
          m +=1;
          iter[0] +=1; 
  def imprimir_matriz(Matriz): 
      print("     ", end="");
      print();
      for i in range(len(Matriz)):
          for j in range(len(Matriz[0])):
              print("%5d " % (Matriz[i][j]), end="");
          print(); 
  #if _name_ == '_main_':
      #while 1:                   
  def Main():
      t_ini = time(); 
      camino_spirit();
      t_final = time();
      return t_final - t_ini;
     # return t_print
  return Main();
print(horse_2(10,1,1));
