import modulo1 as md
import fibo as fib


md.NomeModulo()

ret = fib.fib2(10)
print(ret)


print(__name__)

# Exceções

a =[ 1,2,3]


 
try:
    print(a[5])
except IndexError:
    print("erro de Indece")
finally:
    print("finalmente")

print("OK")

# escrevendo o arquivo  w ,r w+ , r+ , a, a+  
arq = open('arq1.txt', 'a+')  #rb  wb
arq.write("linha1 \n")
arq.write("linha2 \n")
arq.close()

# escrevendo em bytes
arq2 = open('arq1b.txt', 'wb')  #rb  wb
for letra in "linha1 \n":
    arq2.write(letra.encode())
arq2.write(bytes([13]))
arq2.write(bytes([10]))
arq2.write(bytes([65]))
arq2.write(bytes([66]))
arq2.close()

arq3 = open('arq1.txt', 'r')
for linha in arq3:
    print(linha)
arq3.close()
    

