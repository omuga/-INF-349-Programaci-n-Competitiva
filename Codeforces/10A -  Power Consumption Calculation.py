
def power_time(P1,P2,P3,T1,T2,intervalo):
    if (intervalo == 0):
        return 0
    else:
        if (intervalo <= T1):
            return intervalo*P1
        elif (intervalo <= T1 + T2):
            return (T1*P1 + (intervalo-T1)*P2)
        else:
            return (T1*P1 + T2*P2 + (intervalo - (T1 + T2))*P3)
    


if __name__ == '__main__':
    tiempos_mode = list()
    lista_intervalos = list()
    lista_tiempos = list()
    power_consumption = 0
    power_consumption_rest = 0
    n,P1,P2,P3,T1,T2 = list(map(int,input().strip().split()))
    for i in range(n):
        inicial,final = list(map(int,input().strip().split()))
        tiempos_mode.append(final - inicial)
        lista_intervalos.append((inicial,final))
    power_consumption = sum(tiempos_mode)*P1
    rango = len(lista_intervalos) - 1
    for i in range(rango):
        val = lista_intervalos[i+1][0] - lista_intervalos[i][1]
        power_consumption_rest += power_time(P1,P2,P3,T1,T2,val)
    print(power_consumption_rest + power_consumption)
        
        
        
        
    
