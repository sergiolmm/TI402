# comentario de linha
#
#  duas versoes 2.7 e 3 
#
'''

comentario de bloco 

'''

num = 13
num_long = 12000000
num_real = 13.0

print(num)
print(num_real)
# Strings ---- 
texto = "Alo turma como vao voces"
print(texto)
texto = texto + "  python como"
print (texto)
print(texto*3)

print(texto[0])
print(texto[-1])
print(texto[4:9])  # range 

print(len(texto))

ret = "o" in texto
print(ret)
# split()  metodo para separar a frase

print(texto.split())
print (texto.count("como"))
var2 = texto.split()
# colocar barra no lugar do espaco
print ("/".join(var2))
# listas e tuplas

tupla = ('SP', 'Campinas')
print(tupla[1])
print(tupla[0])
print(tupla)
# listas  
a = [98, "um copo de refrigerane", ["em","cima","mesa"]]
print(a)
print(a[-1])
print(a[1:])
print(a[1])  # retorna a string
print(a[1:2]) # aqui retorna como array

ret = range(5)
print (ret)
ret.append(5)
print (ret)
ret.insert(0,42)
print ret
ret.reverse()
print ret
ret.sort()
print ret

ian = [12, "alo mundo", 13.0, 11, 10, "valeu", 0.99, ("a","b"),[1,2]]
print ian

ian.sort()
print ian
del ian[1]
print ian

# dicionarios 

estoque = {'peras': 5, 'laranja': 4, 'maca': 10}
print estoque

print estoque['peras']
estoque['peras'] = 4
print estoque
print estoque.get('melancia','Em falta')
print estoque.get('maca','Em falta')

print 'uva' in estoque 

print estoque.has_key('banana')
ret2 = estoque.items()
print ret2

# variaveis
spam = 'Spam'
spam, ham = 'voce', 'tudo'
print ham

var1 = var2 = var3 = "alo"
print var2
a = [1,2,3,4]
b = a
a.append(5)
print b 
a = 1
print a
print b 

# formatando a saida em python

print "posicao 1 vo vetor b -> %d  .. %05d " % (b[1],b[2])
texto = "Acorda turma"
texto2 = " -------->>>> "
print " este texto %s %s" % (texto,texto2)

# lacos de controle 
# if
a = 10

if  a == 10:
  print("correto")
print("fim do if")

if a == 9:
    print("ok")
else:
    print("nok")

if a < 10:
  print("menor")
elif a > 10:
    print("maior")
else: 
    print("igual")  

# for trabalha com range ou arrays

for num in range(5):
    print num
for letra in texto:
    print letra    

i = 10

while i > 0:
    print i
    i = i -1



