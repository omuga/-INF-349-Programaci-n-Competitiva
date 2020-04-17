from math import gcd
def base_X(number,base,lista):
    if (number == 0):
        return sum(lista)
    else:
        lista.append(number % base)
        return base_X(int(number/base), base, lista)
    
def replicacion(A):
    a = 0
    for i in range(2,A):
        val = base_X(A,i,[])
        a +=(val)
    a = int(a)
    b = int(i-1)
    c = gcd(a,b)
    print(str(int(a/c)) + "/" + str(int(b/c)))

if __name__ == '__main__':
    n = int(input())
    (replicacion(n))
        

