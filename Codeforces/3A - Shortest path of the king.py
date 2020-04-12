__author__ = 'Obriel Muga'

columnas = ['a','b','c','d','e','f','g','h']

def ajedrez(posicion_actual,posicion_final,lista_final):
    c_actual,f_actual = posicion_actual
    c_final,f_final = posicion_final
    if (posicion_actual == posicion_final):
        print(len(lista_final))
        for i in lista_final:
            print(i)
        return
    elif (c_actual < c_final and f_actual < f_final):
        lista_final.append("RU")
        return ajedrez((c_actual + 1,f_actual + 1),(posicion_final),lista_final)
    elif (c_actual > c_final and f_actual > f_final):
        lista_final.append("LD")
        return ajedrez((c_actual - 1, f_actual - 1),(posicion_final),lista_final)
    elif (c_actual == c_final and f_actual < f_final):
        lista_final.append("U")
        return ajedrez((c_actual,f_actual + 1),(posicion_final),lista_final)
    elif (c_actual > c_final and f_actual < f_final):
        lista_final.append("LU")
        return ajedrez((c_actual - 1,f_actual + 1),(posicion_final),lista_final)
    elif (c_actual == c_final and f_actual > f_final):
        lista_final.append("D")
        return ajedrez((c_actual,f_actual -1),(posicion_final),lista_final)
    elif (c_actual < c_final and f_actual > f_final):
        lista_final.append("RD")
        return ajedrez((c_actual + 1, f_actual - 1),(posicion_final),lista_final)
    elif (f_actual == f_final and c_actual > c_final):
        lista_final.append("L")
        return ajedrez((c_actual - 1,f_actual),(posicion_final),lista_final)
    elif (f_actual == f_final and c_actual < c_final):
        lista_final.append("R")
        return ajedrez((c_actual + 1, f_actual),(posicion_final),lista_final)
    

if __name__ == '__main__':
    inicio = str(input())
    final = str(input())
    columna_inicial = columnas.index(inicio[0])
    columna_final = columnas.index(final[0])
    fila_inicial = int(inicio[1]) - 1
    fila_final = int(final[1]) - 1
    ajedrez((columna_inicial,fila_inicial),(columna_final,fila_final),[])
    

