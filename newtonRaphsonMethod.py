# Funcion a calcular sus raices
def f(x):
    return x**3 + 3

# Derivada de la funcion
def fd(x):
    return 3*x**2

# Metodo de NewtonRapson 1 - (f(x)/f'(x))
def newtonRapson(n):
    num = f(n)
    den = fd(n)
    return n - num/den

# Cantiadad de interaciones del metodo de Newton, con 11 iteraciones
def iterations(n):
    i = 0
    result = 1
    while i < n:
        result = newtonRapson(result)
        i += 1
    return result


if __name__ == '__main__':
    while True:
        n = input('Numero de iteraciones con las que desea calcular la raiz de x^3 + 3 (letra para salir): ')
        try:
            print(iterations(int(n)))
        except ValueError:
            print("Ha presionado una letra, ha salido del programa, gracias por usar.")
            break