def funcion(x):
    return x ** 2


def riemman_sum(a, b, subintervals):
    interv = (b - a) / subintervals
    base = a
    value = 0
    for j in range(subintervals):
        value += funcion(base) * interv
        base += interv
    return value


if __name__ == '__main__':
    n = int(input("Incerte el numero de intervalos que va a usar para calcular el area de x^2, entre 2 y 3: "))
    print("El area bajo la curva es: ", riemman_sum(2, 3, n))
