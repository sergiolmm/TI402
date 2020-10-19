

arq = open('arquivo.txt', 'w+') # cria ou sobre escreve arquivo
arq.write('linha3 \n')
arq.write('linha3 \n')
arq.close()


arq1 = open('arquivo2.txt', 'a+') # cria ou apenda escreve arquivo
arq1.write('linha5 \r\n')
arq1.write('linha6 \r\n')
for i in range(10):
    arq1.write("linha %d \r\n" % i)
arq1.flush()
arq1.close()

# ler arquivos

arq2 = open('arquivo2.txt', 'r')  #rb
for linha in arq2:
    print(linha)

arq2.close()

arq2 = open('arquivo2.txt', 'rb')  #rb
for linha in arq2:
    for c in linha:
        print (c)
arq2.close()


arq2 = open('arquivo2.txt', 'rb')  #rb

c1 = arq2.read(20)
print (c1)
for c in c1:
        print (c)
arq2.close()

p_count = {}
arq2 = open('arquivo2.txt', 'rb')  #rb
for linha in arq2:
    palavras = linha.split()
    for palavra in palavras:
        p_count[palavra] = p_count.get(palavra,0) + 1
arq2.close()

palavras = p_count.keys()

for palavra in palavras:
    print('palavra %s, qtd %05i' % (palavra, p_count[palavra]))