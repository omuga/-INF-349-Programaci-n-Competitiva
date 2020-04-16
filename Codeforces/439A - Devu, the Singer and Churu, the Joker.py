if __name__ == "__main__":
    nn = input()
    n,tiempo = nn.strip().split()
    canciones = input()
    canciones = canciones.strip().split()
    check = len(canciones) - 1
    valor = 0
    for cancion in canciones:
        valor = valor + int(cancion)
    final = valor + check*10
    if (final > int(tiempo)):
        print(-1)
    else:
        chistes = (int(tiempo) - valor)/5
        print(int(chistes))
        
        
        
    
