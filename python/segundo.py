import sys
'''
Comentario de bloco 

Estruturas de controle 

'''

print("alo")
i = 10
while i > 1:   
    if i%2 == 0:
        i = i - 1
        continue
    print(i)
    i = i - 1
    
# list comprehensios
pares = [i for i in range(100) if (i%2) == 0]
print (pares)
impares = [i for i in range(100) if (i%2) != 0]
print (impares)

#Generator python2.7 
pares = (i for i in range(100) if (i%2) == 0)
print (pares)
print(sys.version_info)
versao = sys.version_info
print (versao.major)
for i in range(10):
    if versao.major==3:
       print(next(pares))  # pyton 3
    else:  
       print("ooo %d"% pares.next()) # python 2

## funcoes e procedimentos
 #  return  -> procedimento
 #  
 #  return experessao -> funcao.

def exemplo(a,b,c):
     ### soma tres valores
     return a+ b + c 

a = exemplo(5,1,3)     
print(a)

def changer(x,y):
    x = 2  # localmente
    y[0] = 'h' # modifica objeto compartilhado
'''
alo = 'teste'
val = 10
changer(val, alo)
print (alo)    
'''

# definindo valores default
def func(a, b, c=100, d=10):
    print(a,b,c,d)

func(1,2,3,4)
func(1,2)
func(c=1000, b=3, a=4)

func(1000,3,4)

func(c=1000, 
     b=3, 
     a=4)

# o valor default somente e avaliado uma vez 

def f(a, L=[]):
    L.append(a)
    return L

print (f(1))
print (f(2))

def f2(a, L2=None):
    if L2 is None:
        L2 = []
    L2.append(a)
    return L2

print(f2(1))        
print(f2(2))        
print(__name__)


