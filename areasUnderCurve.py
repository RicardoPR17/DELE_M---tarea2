import threading

def funcion(x):
  return x**2

def optimiz(t, n, a, b):
  if t > n or t > 50:
    print("el numero de hilos deberia ser menor a la cantidad de intervalos o el numero de hilos es mayor a 50")
  else:
    resultados = [0] * t
    threads = []
    interv =  (b - a)/n
    for i in range(t-1):
        inicio = a
        fin = inicio + interv
        thread = threading.Thread(target=riemmanSum, args=(inicio, fin, n))
        inicio += interv
        thread.start()
        threads.append(thread)
    fin = b
    value = riemmanSum(a, fin, n)
    resultados[-1] = value
    for thread in threads:
        thread.join()
    return sum(resultados)

def riemmanSum(a, b, n):
  interv = (b - a) /n
  base = a
  value = 0
  for j in range(n):
    value += funcion(base) * interv
    base += interv
  return value

n = int(input("Incerte el numero de intervalos que va a usar para calcular el area de x^2, entre 2 y 3: "))
t = int(input("numero de hilos: "))
print("El area bajo la curva es: " , optimiz(t, n, 2, 3))