__author__ ='Obriel Muga'

if __name__ == '__main__':
    dados = input()
    a,b = map(int,dados.strip().split())
    mayor = max(a,b)
    prob = 7 - mayor
    result_a = prob
    result_b = 6
    if (prob == 6):
        print("1/1")
    elif (prob == 2):
        print("1/3")
    elif (prob == 3):
        print("1/2")
    elif (prob == 4):
        print("2/3")
    elif (prob == 5):
        print("5/6")
    elif (prob == 1):
        print("1/6")


    
