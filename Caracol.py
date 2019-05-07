def abrir(mapa):#Abre el mapa en filas
    return [x.split() for x in open(mapa,'r')]

def columnas(mapa):#Convierte el mapa a columnas
    return [[fila[i] for fila in mapa] for i in range(len(mapa))]

def recorrer(mapa, x, y):
    print(x,y)
    print(mapa[x][y])
    if y==(len(mapa[x])-1)and x==(len(mapa)-1):
        return True
    elif y < (len(mapa[x])-1):
        return recorrer(mapa,x,y+1)
    elif x < (len(mapa)-1):
        return recorrer(mapa,x+1,0)
    else:
        return False

def rec(mapa, x):
    if x==(len(mapa)):
        return True
    elif x<(len(mapa)):
            print(mapa[x])
            return rec(mapa,x+1)
    else:
        return False

def caminar(mapa, x, y, camino):
    if len(mapa[x])==1:
        caminar.append(mapa[x][y])
        return camino
    elif len(mapa[x])==2 and len(mapa[x+1])==2:
        caminar.append(mapa[x][y])
        caminar.append(mapa[x][y+1])
        caminar.append(mapa[x+1][y])
        caminar.append(mapa[x+1][y+1])
        return camino
    elif y < (len(mapa[0])):
        derecha(mapa, x, y, camino)
    elif x < (len(mapa)):



def derecha(mapa, x, y, camino):
    if y == (len(mapa[0])):
        del mapa[0]
        return caminar(mapa, x+1, len(mapa[x])-1,camino)
    elif y < (len(mapa[0])):
        camino.append(mapa[0][y])
        return derecha(mapa,x,y+1,camino)
'''
def abajo(mapa, y, camino):
    if y == (len(mapa[len(mapa)-1])):
        del mapa[len(mapa)-1]
        return camino
    elif y < (len(mapa[len(mapa)-1])):
        camino.append(mapa[len(mapa)-1][y])
        return derecha(mapa,y+1,camino)
'''
print(caminar(abrir("mapa.txt"),0,0,[]))