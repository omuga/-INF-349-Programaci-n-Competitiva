import math

__author__ = 'Obriel Muga'

def raising_bacteria(x):
    binario = '{0:b}'.format(x)
    num = 0
    for i in binario:
        if i == '1':
            num = num + 1
    return num

if __name__ == "__main__":
    x = int(input())
    print(raising_bacteria(x))
