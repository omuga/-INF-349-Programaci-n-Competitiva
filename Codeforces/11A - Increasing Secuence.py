import math


__author__ = 'Obriel Muga'

if __name__ == '__main__':
    n,d = list(map(int,input().strip().split()))
    secuencia = list(map(int,input().strip().split()))
    resto = 0
    contador_op = 0
    for i in range(n-1):
        valor = ((secuencia[i+1] - secuencia[i]))
        if (valor - resto > 0):
            resto = 0
            continue
        elif (valor - resto == 0):
            contador_op += 1
            resto = d
        elif (valor - resto < 0):
            if (abs(valor - resto))%d == 0:
                agregar = math.ceil(abs(valor-resto)/d) + 1
            else:
                agregar = math.ceil(abs(valor - resto)/d)
            contador_op += agregar
            resto = agregar*d    
    print(contador_op)
