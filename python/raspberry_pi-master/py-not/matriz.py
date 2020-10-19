'''
Como criar classes no python

'''

class Matriz(object):

    nome_da_classe = "Matriz"
    teste = ""

    def __init__(self,n ,m):
        self.matriz = [[None for j in range(m)] for i in range(n) ] 
        self.linhas = n
        self.colunas = m 
        self.nome_da_classe = self.nome_da_classe + str(n)
        self.teste = self.nome_da_classe + str(n)
        self.teste1 = "alo"

    def getTeste(self):
        return self.teste


    def __getitem__(self, i):
        return self.matriz[i]

    def __add__(self, b):
        c = Matriz(self.linhas, self.colunas)
        for i in range(self.linhas):
            for j in range(self.colunas):
                c[i][j] = self[i][j] + b[i][j]
        return c

    @staticmethod
    def nome():
        print(Matriz.nome_da_classe)

