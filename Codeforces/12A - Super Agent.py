__author__ = 'Obriel Muga'

if __name__ == '__main__':
    linea_1 = input()
    linea_2 = input()
    linea_3 = input()
    A = linea_1.replace('X',"1")
    A = A.replace('.',"0")
    B = linea_2.replace('X',"1")
    B = B.replace('.',"0")    
    C = linea_3.replace('X',"1")
    C= C.replace('.',"0")
    A = A + B[0]
    C = B[2] + C
    if (A == C[::-1]):
        print("YES")
    else:
        print("NO")
        

