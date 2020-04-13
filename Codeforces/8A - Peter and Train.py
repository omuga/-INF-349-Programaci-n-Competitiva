__author__ = 'Obriel Muga'

if __name__ == '__main__':
    banderas = input()
    primera = input()
    segunda = input()
    banderas_vuelta  = banderas[::-1]
    index = 0
    forward = False
    backward = False
    #forward_primera
    if (primera in banderas):
        seccion = banderas.find(primera)
        banderas_siguiente = banderas[seccion + len(primera):]
        if (segunda in banderas_siguiente):
            forward = True
    if (primera in banderas_vuelta):
        seccion = banderas_vuelta.find(primera)
        banderas_siguiente = banderas_vuelta[seccion + len(primera):]
        if (segunda in banderas_siguiente):
            backward = True
    if (backward and forward):
        print("both")
    elif (backward and not forward):
        print("backward")
    elif (forward and not backward):
        print("forward")
    else:
        print("fantasy")
        

    
    
    



    
