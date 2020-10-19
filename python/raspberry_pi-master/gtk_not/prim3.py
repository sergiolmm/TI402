print("Ola")

str = "tudo bem"
print(str)
str = 4
print(str)
num_int = 13
num_int_long = 13000000
num_real = 13.0
'''
print num_int
print num_int_long
print num_real

str = "Alo 4 semestre"
print str[0]
print "Alo 4 semestre"[0]
# de tras para frente
print str[-2]
print "Alo 4 semestre"[-1]
# parte da string
print str[2:6]
print "Alo 4 semestre"[7:9]
print "Alo 4 semestre"[2:-2]
print len(str)

print "hello" < "julho"

print "e" in str
print "u" in str
print str.upper()
print str.lower()

print str.count('4')
# contar a quantidade de e na frase
print str.count("e")

print str.split()
arr = str.split()
print arr[0]
print arr[2]
print ""
str2 = str.split()
print "/".join(str2)

#criando uma tupla   
tupla = ('MG','Simonesia')
print tupla[1]

tupla2 = ('MG','Simonesia',3)
print tupla2[2]
#tupla2[2] = 30 nao suporta
print tupla2[2]

tupla2 = ("MG","Simonesia",3)
print tupla2[2]
#tupla2[1] = "alo"
print tupla2[1]


# Arrays flexives
a = [98, "grarrafa de cerveja",["on","the","wall"]]

print a[0]
print len(a)
print a[2]
del a[-2]
a[0] = 100
print a[0]
a.append("teste")
a.reverse()
print a
a.sort()
a.insert(1,"alo")
print a

# dicionarios
#  armazena pares de chaves/valor de forma desordenada 
#

estoque = {'codigo' : 1, "descr": "parafuseo"}
#print estoque.codigo
print estoque['codigo']
print 'valor' in estoque

print estoque.has_key('codigo')
print estoque.items()
 
#variaveis

teste = 'teste'  # basica
print teste
valor, qtd = 100, 10  # viraq uma tupla
print valor

#  x = y -> nao copia conteudo e sim uma faz uma referencia
a = [1,2,3]
b = a
a.append(4)
print b

# normal ja esperado
a1 = 1
b1 = a1
a1 = 2
print a1, b1

#formatar a saida
print "numero %d  e %05d " % (1,2)
print "numero %f  e %.3f  - %.5f " % (121.001 ,2.123856 ,2.123456)
print " frase = %s" % str

var = "%.4f" % (2.123856)
print var[0:-1]
var2 = ("%.4f" % (2.123856))[0:-1]
print var2
'''
import base64
v = base64.b64decode('UGVyZ3VudGFzPw==')
v2 = v.decode('ascii')
print(v2)
print(base64.b64decode('T2JyaWdhZG8=').decode('ascii'))

