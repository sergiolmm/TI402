print ("alo")


num = 10
print(num)
num_int = 30
print(num_int)
num_real = 13.0
print(num_real)
print (num + num_real)
# -> comentario de linha
#
'''
Comentario de bloco
Strings -> imutaveis

'''
str = "alo" + " Mundo " + " Cruel "
print(str)
print(str*3)

print(str[0])
print("Alo"[0])
str = "Acordem meus alunos"
print(str[-1])
print(str[-2])

print(str[8:-6])
print(len(str))
print(len("Oi turma"))
print( "m" in str)  # busca do caracter m em str 
# dividir a string criando um vetor de palavars

print(str)
str2 = str.split()
print(str2)
print("os alunos e os prof estao cansados")
print("os alunos e os prof estao cansados".count('os'))
print('/'.join(str2))

# Lista e tuplas
tupla = ('SP', 'Sao Paulo')
print (tupla[1])

# listas
# arrays flexiveis
a = [98,"Vesperino dorme na minha aula",12,["na", "minha", "aula"] ]
print(a)
print(a*3)
print(a[0])
print(a[-1])
del a[2]
print(a)
'''
a = range(10)
print (a)
a.append(11)
print (a)
a.insert(0,100)
print (a)
a.reverse()
print (a)
a.sort()
print (a)
'''
# Dicionarios
estoque = { 'peras': 5, 'laranja': 10, 'macas': 2 }
print(estoque)
print(estoque['peras'])
estoque['peras'] = 3
print (estoque['peras'])
str = estoque.get('peras','Falta')
print(str)
str = estoque.get('melancia','Falta')
print(str)
str = estoque.get('melancia',0)
print("estoque %s de items" % str)

res = 'uvas' in estoque
print(res)
# print (estoque.has_key('uvas')) # so existe na versao 2.7
print(estoque.items())

# variaveis
spam = 'Spam' #basico
spam ,ham = 'yum', 'YUM' # tupla
print(spam,ham)
spam = ham = 'Texto' # multiplo
print(spam,ham)

# atribuições
a = [1,2,3]
b = a
a.append(4)
print(b)
a.append(4)
print(b)
a = 2
print(a)
print(b)

str1 = 'valores'
v1 = 10
v2 = 20

print("Os %s sao %d e %05d" % (str1, v1, v2) )

# estruturas de controle

if v1 < v2:
    print('menor')

if v1 > v2:
    print('aaaa')
else:
    print('bbbb')

v1 = v2 

if v1 > v2:
    print('a')
elif v1 < v2:
    print('b')
elif v1 == v2:
    print('c')
        









