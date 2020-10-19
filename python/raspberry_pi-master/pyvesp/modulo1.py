"""Modulo """

def NomeModulo():
    """Imprime nome do modulo atual """
    print("O nome desse modulo e %s" % __name__)



if __name__ == "__main__":
   print(__name__)
   NomeModulo()
   print("zzzzz")
