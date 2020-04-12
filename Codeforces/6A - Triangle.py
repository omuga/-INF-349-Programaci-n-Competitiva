from itertools import combinations

def NT(l):
    a,b,c = l[0],l[1],l[2]
    if ((a < b +c) and (b < a + c) and (c < a + b)):
        return True
    else:
        return False

def DT(l):
    a,b,c = l[0],l[1],l[2]
    if ((a <= b +c) and (b <= a + c) and (c <= a + b)):
        return True
    else:
        return False    

if __name__ == '__main__':
    triangles = input()
    lista_revision = list()
    triangles = list(map(int,triangles.strip().split()))
    listas = combinations(triangles,3)
    deg = False
    tri = False
    for perm in listas:
        if (NT(perm)):
            print('TRIANGLE')
            tri = True
            break
        elif (DT(perm)):
            deg = True
    if(not tri):
        if (deg):
            print("SEGMENT")
        else:
            print("IMPOSSIBLE")
        
