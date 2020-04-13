import math

__author__ = 'Obriel Muga'

if __name__ == '__main__':
    list_matrix  = list()
    rows = 0
    col = 0
    for i in range(8):
        linea = input()
        linea = linea.replace("W","0")
        linea = linea.replace("B","1")
        lista = list(linea)
        lista = list(map(int,lista))
        if (sum(lista)== 8):
            rows = rows + 1
        else:
            col = sum(lista)
    print(rows + col)
