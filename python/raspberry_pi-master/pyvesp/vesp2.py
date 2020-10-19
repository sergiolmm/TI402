'''
laços de controle e outros

'''

for letra in "Alo mundo":
    if letra == 'o':
        print ("Achei\r\n")

i = 10
while i > 2:
    i -= 1
    print(i)        


while True:
    for letra in "Turma com sono":
        if letra == "c":
            print("achou c")
            break    
        if letra == "u":
            print("achou u")
            continue
    break


'''
List comprehension e Generators

'''
# List
pares = [ i for i in range(100) if (i%2) == 0 ]
print(pares)
impares = [ i for i in range(100) if (i%2) != 0 ]
print(impares)

#generators
pares2 = (i for i in range(100) if (i%2)==0)
print(pares2)
print(next(pares2))
print(next(pares2))
soma_pares = sum(i for i in range(10) if (i%2)==0)
print(soma_pares)


'''
Funcoes e procedimentos

'''
def soma_tres(a, b, c):
    """ Soma tres valores"""
    return a + b + c

resp = soma_tres(1,2,3)
print(resp)


def func( a, b, c= 10, d=1000):
    print(a,b,c,d)

func(12,13,14,15)
func(12,13)
func(d=10, c= 100, b = 1, a=3)
func(12,13,14)
func(12,13)

def f1(a, L=[]):
    L.append(a)
    return L
print(f1(1))
print(f1(2))

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f2(1))

Le = f2(2)
print(Le)
print(f2(3,Le))

print(__name__)