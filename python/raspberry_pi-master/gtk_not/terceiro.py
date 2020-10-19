'''
Funcoes e procedimentos

def nome (arg1, arg2, ...):
    """ Documentacao """
    return # procedimento
    return expressao # caso isso se uma funcao

'''

def soma(a,b,c):
    """ Soma tres valoes"""
    return a+b+c

val = soma(1,3,5)
print(val)    

def proc2(x, y):
    x = x + 2
    ret = x + y
   # y[0] = ret
    return ret

x = 0
y = 2
val = proc2(x,y)    
print (x,y,val)

def func( a, b, c = 10, d = 100):
    print(a ,b, c, d)

func(1,2,3,4)
func(1,2)
func(1,2,d=3)
# nomeando as variaveis
func(d=4,a=2,b=3)

def f(a, L=[]):
    L.append(a)
    return L 

print( f(1) )    
print( f(2) )    
print( f(3) )    

def f2(a, L1=None):
    if L1 is None:
        L1 = []
    L1.append(a)
    return L1

print( f2(1) )    
print( f2(2) )    
print( f2(3) )    


