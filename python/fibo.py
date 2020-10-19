# modulo Fibonacci

def fib(n):
    """ escreve a sequencia"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b 
    print(__name__)

def fib2(n):
    """Retorna uma serie 
       Valor de teste
       Turma 402
    """
    result = []
    a, b = 0, 1
    while b< n:
        result.append(b)
        a, b = b, a+b
    return result    

def fib3(n):
    """
       Tratamento de erro
       Turma 402
    """
    vet = [1, 2, 3, 4]
    try:
        print(vet[n])
    except IndexError:
        print("posicao invalida")
    finally:
        print("imprimiu - fim do print")    


if __name__ == "__main__":
    fib(10)
