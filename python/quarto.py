from matriz import Matriz


if __name__ == "__main__":
   a = Matriz(2,2)
   for i in range(a.linhas):
      for j in range(a.colunas):
         a[i][j] = i

   print(a.matriz)