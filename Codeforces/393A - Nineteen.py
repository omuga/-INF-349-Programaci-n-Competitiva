__author__ = 'Obriel Muga'

def nineteen(s):
    n = 0
    i = 0
    e = 0
    t = 0
    for letra in s:
        if (letra == 'n'):
            n = n + 1
        elif (letra == 'i'):
            i = i + 1
        elif (letra == 'e'):
            e = e + 1
        elif (letra == 't'):
            t = t + 1
    if (n < 3):
        n = int(n/3)
    else:
        n = int((n - 3)/2)+1
    i = int(i)
    t = int(t)
    e = int(e/3)
    return min([n,i,e,t])

if __name__ == "__main__":
    s = str(input())
    print(nineteen(s))



