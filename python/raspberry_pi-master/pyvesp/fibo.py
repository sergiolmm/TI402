""" EXEMPLO DA SERIE DE FIBONACCI """

def fib(n):
    """ Escreve a serie de Fibonacci ate n """
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a + b     #  c = b
                            #  b = a + b 
                            #  a = c  
def fib2(n):
    """ Retorna a serie de Fibonacci ate n """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b     #  c = b
    return result

if __name__ == "__main__":
   fib(10)