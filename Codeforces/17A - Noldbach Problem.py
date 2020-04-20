def divisor(n):
    lista = []
    for i in range(1,n+1):
        if  n%i == 0:
            lista.append(i)
    return lista


def numeros_primos(k):
    lista = [2]
    for i in range(1,k+1,2):
        if (len(divisor(i)) == 2):
            lista.append(i)
    return lista

def problem(numero):
    primos = numeros_primos(numero)
    for i in range(0,len(primos)-1):
        if (primos[i] + primos[i+1] + 1 == numero):
            return True
    return False
        



            

if __name__ == '__main__':
    n,k = list(map(int,input().strip().split()))
    lista_primos = numeros_primos(n)
    contador = 0
    final = True
    for num in lista_primos:
        if (problem(num)):
            contador += 1
            if (contador == k):
                final = False
                print("YES")
                break
    if (k == 0):
        print("YES")
    elif (final):
        print("NO")
    
    
