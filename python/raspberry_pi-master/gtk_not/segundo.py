'''
Aula de python - lacos de controle e outros

'''
a = 10
b = 20
print (a,b)

if a < b: print(a)  # funciona mas deve ser evitado

if a < b: 
  print(a) 
  print("funciona com  no minimo 1 espaco  alo mundo")

if a > b:
    print(a)
else:
    print(b)    

if a> b:
    print('maior')
elif a == b:
    print('igual')
else:
    print("menor")        

# for em contagems e for em arrays
for num in range(10):
    print(num)

str = "Alo mundo etc..."    
for letra in str:
    print(letra)

for letra in "frase":
    print(letra)    

# range de maneira diferente

for num in range(2,9,3):
    print(num)

# while
a = 20
while a > 10:
    print(a)
    a = a - 1
a = 20
while a > 10:
    print(a)
    if a == 16:
        a = a -3 
        continue
    a = a - 1
a = 20    
while a > 10:
    print(a)
    if a == 16:
        break
        
    a = a - 1

for letra in "Nos vamos dominar":
    if letra == 'd':
        break    
    print (letra)


# list comprehensions
print('pares')
pares = [i for i in range(100) if (i%2) == 0 ]
print(pares)
impares = [i for i in range(50) if (i%2) != 0 ]
print(impares)
matriz = [ [ 0 for j in range(3)] for i in range(3)]
print(matriz)
pares = (i for i in range(100) if (i%2) == 0 )
print (pares)
#print (pares.next())
# print (pares.next())
soma_impares = sum(i for i in range(50) if (i%2)!= 0)
print(soma_impares)

# funce
