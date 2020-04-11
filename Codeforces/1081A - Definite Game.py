__author__ = 'Obriel Muga'

def resolve(valor_inicial, valor_actual):
    if (valor_actual == 1):
        return 1
    elif (valor_actual == 2):
        return 2
    else:
        for i in range(valor_actual - 1, 1 , -1):
            if (valor_inicial % i != 0):
                return resolve(valor_inicial,valor_actual - i)


if __name__ == "__main__":
    n = int(input())
    print(resolve(n,n))
