__author__ = 'Obriel Muga'

if __name__ == '__main__':
    n,m = list(map(int,input().strip().split()))
    flag = list()
    result = False
    result_f = False
    for i in range(n):
        fila = input()
        val = fila[0]
        flag.append(val)
        contador = fila.count(val)
        if (contador != m):
            result = True
            break
    if (result):
        print("NO")
    else:
        for i in range(len(flag)-1):
            if (flag[i] == flag[i+1]):
                result_f = True
                break
        if (not result_f):
            print("YES")
        else:
            print("NO")
                
        
