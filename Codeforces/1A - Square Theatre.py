__author__ = 'Obriel Muga'

import math
def resolve(m,n,a):
    filas_largo = math.ceil(float(m/a))
    filas_ancho = math.ceil(float(n/a))
    return (filas_largo * filas_ancho)


if __name__ == '__main__':
    valores = str(input())
    valores = valores.strip().split()
    m = int(valores[0])
    n = int(valores[1])
    a = int(valores[2])
    print(resolve(m,n,a))
