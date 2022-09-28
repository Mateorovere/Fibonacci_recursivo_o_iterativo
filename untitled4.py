#secuencia de fibonacci de manera recursiva vs de manera iterativa
def fib_recursivo(n):
  """ Funcion que devuelve el numero de Fibonacci numero n, siempre y cuando sea n <= 0 de manera recursiva"""
  if n == 0 or n == 1:
    return n
  return fib_recursivo(n-1) + fib_recursivo(n-2)

def fib_iterativo(n):
  """ Funcion que devuelve el numero de Fibonacci numero n, siempre y cuando sea n <= 0 de manera iterativa"""
  if n == 0 or n == 1:
    return n
  ant1 = 1
  ant2 = 0
  for i in range(2, n+1):
    fibn = ant1 + ant2
    ant2 = ant1
    ant1 = fibn
  return fibn
#en este ejercicio si agarramos n muy altos de manera recursiva va a ser menos eficiente que en el caso iterativo

