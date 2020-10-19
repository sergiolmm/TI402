
class Matriz(object):

    nome_da_classe = "Matriz - h"

    def __init__(self, n, m):
        self.matriz = [[None for j in range(m)] for i in range(n)]
        self.linhas = n
        self.colunas = m


    def __getitem__(self, i):
        return self.matriz[i]


    @staticmethod
    def nome():
        print(Matriz.nome_da_classe)

if __name__ == "__main__":
    a = Matriz(2,3)
    print(a)
    for i in range(a.linhas):
        for j in range(a.colunas):
            a[i][j] = i

    print(a.matriz)
    print('---')
    Matriz.nome()
    a.nome()