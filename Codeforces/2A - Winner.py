from queue import Queue 
__author__ = 'Obriel Muga'

if __name__ == '__main__':
    people = list()
    puntajes = list()
    lista_max = list()
    rounds = int(input())
    personas_mas_puntaje = list()
    q = Queue(maxsize = rounds)
    for i in range(rounds):
        name,score = input().split()
        if name not in people:
            people.append(name)
            puntajes.append([int(score)])
            q.put((name, int(score)))
        else:
            indice = people.index(name)
            puntaje_nuevo = int(puntajes[indice][-1]) + int(score)
            puntajes[indice].append(puntaje_nuevo)
            q.put((name,puntaje_nuevo))
        if (i == rounds - 1):
            for a in puntajes:
                lista_max.append(a[-1])
    maximo = max(lista_max)
    for a in range(len(puntajes)):
        if puntajes[a][-1] == maximo:
            personas_mas_puntaje.append(people[a])
    while(not q.empty()):
        val = q.get()
        if (val[1] >= maximo and val[0] in personas_mas_puntaje):
            print(val[0])
            break

