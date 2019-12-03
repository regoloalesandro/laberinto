import subprocess

def TomarEntrada(ArchivoEntrada):
    Entrada = open(ArchivoEntrada,"r")
    Lineas = Entrada.readlines()
    Entrada.close()
    Valores = []
    Fin = (1,1)
    PosicionInial = (1,1)
    fila = 1
    for linea in Lineas :
        columna = 1
        for Valor in linea :
            if Valor  == "0" :
                Valores.append((fila,columna))
            elif( Valor == "X"):
                Valores.append((fila, columna))
                Fin = (fila,columna)
            elif ( Valor == "I"):
                Valores.append((fila,columna))
                PosicionInial = (fila,columna)
            columna +=1
        fila +=1 
    return Valores,Fin,PosicionInial
def resolverLarinto(aVisitar, Visitadas,Valores,Padres,fin):
    pila = []
    flag = 0
    inicio = aVisitar.pop(0)
    Visitadas.add(inicio)
    pila.append(inicio)
    while pila != [] and flag == 0 :
        vertice = pila.pop(0)
        (y,x) = vertice
        if vertice != fin :
            pila,Padres,Visitadas = Prueba(vertice,y, x-1,Valores,pila.copy(),Visitadas.copy(),Padres.copy())
            pila,Padres,Visitadas = Prueba(vertice,y, x+1,Valores,pila.copy(),Visitadas.copy(),Padres.copy())
            pila,Padres,Visitadas = Prueba(vertice,y-1, x,Valores,pila.copy(),Visitadas.copy(),Padres.copy())
            pila,Padres,Visitadas = Prueba(vertice,y+1, x,Valores,pila.copy(),Visitadas.copy(),Padres.copy())
                    
        else:
            flag = flag + 1
    return Padres


def Prueba(actual,y,x,Valores,pila,Visitadas,Padres):
    if ((y,x) in Valores) and (not (y,x) in Visitadas):
        pila.append((y,x))
        Visitadas.add((y,x))
        Padres[(y,x)]=actual
    return pila,Padres,Visitadas
def main(archivo):

    Valores, Fin, PosicionInicial = TomarEntrada(archivo)
    Visitadas = set()
    PorVisitar = [PosicionInicial]
    Padres = {}
    Padres [PosicionInicial] = PosicionInicial
    Valores.sort(key=(lambda vecino: abs(Fin[0] - vecino[0]) + abs(Fin[1] - vecino[1])), reverse=True)
    Padres = resolverLarinto(PorVisitar,Visitadas, Valores,Padres,Fin)
    Abuscar = Fin
    recorrido = []
    result = False
    if(Abuscar in Padres.keys() ):
        while (Abuscar != PosicionInicial ):
            recorrido.append(Abuscar)
            Abuscar = Padres[Abuscar]
    else:
        while not result :
            response = subprocess.run(["./a.exe", "a.txt"])
            if (response == 0):
                result = True
                main("salida.txt")
            else:
                print("error")

    recorrido.append(PosicionInicial)
    recorrido.reverse()
    print(recorrido)
main("salida.txt")