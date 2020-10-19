from matriz import Matriz

def sub(self, b):
    c = Matriz(self.linhas, self.colunas)
    for i in range(self.linhas):
        for j in range(self.colunas):
            c[i][j] = self[i][j] - b[i][j]
    return c

def getItem(self, n):
    return "nao implementado"

def getItem2(self):   
    return "nao implementado ainda -> "


if __name__=="__main__":
    print(Matriz.nome())
    a = Matriz(2,2)
    b = Matriz(2,2)
    print(a.nome_da_classe)
    print(a.getTeste())
    for i in range(a.linhas):
        for j in range(a.colunas):
            a[i][j] = i   
            b[i][j] = j   

    print(a.nome())
    
    print(a[1])
    try:
        print(a[2])
    except :
        print("erro de indice")


    c = a + b
    
    print(a.matriz)
    print(b.matriz)
    print(c.matriz) 

##  Monkey patch

    Matriz.__sub__ = sub

    c = a - b
    
    print(a.matriz)
    print(b.matriz)
    print(c.matriz) 

    Matriz.__getitem__ = getItem
    print(a[1])
    print(b[1])

    Matriz.getTeste = getItem2
    print(a.getTeste())
