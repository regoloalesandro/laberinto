import subprocess
import sys
#TomarEntrada En el Tp se recibira un archivo en el cual se indicaran las especificaciones del laberinto a resolver
#Este programa lo recibe y ejecuta el programa de C para generar un laberinto el cual luego se resolvera
#El laberinto se representara como una matriz bidimensional de chars, las coordenas se representaran como una tupla de
#enteros
#El archivo con las especificaciones debera llamarse Entrada.txt
#TomarEntrada: File -> List -> ((int, int), (int,int))
#La funcion toma como entrada un archivo que es el que contendra la matriz que representa el laberinto
#creado por el programa en C y lo va leyendo y pasando a la matriz Array.
#A su vez se identifica conde es que esta la posicion de inicio y el final, que es lo que la funcion devolvera en forma de
#tupla
def TomarEntrada(ArchivoEntrada,Array):
    iteradorLineas = 0
    Entrada = open(ArchivoEntrada,"r")
    Lineas = Entrada.readlines()
    Entrada.close()
    for linea in Lineas :
        linea = list(linea)
        Array.append(linea[:-1])
        if linea.count("I") != 0:
            xInicio = linea.index("I")
            yInicio = iteradorLineas
        if linea.count("X") != 0:
            xObjetivo = linea.index("X")
            yObjetivo = iteradorLineas
        iteradorLineas += 1
    return (yInicio , xInicio ), (yObjetivo , xObjetivo )
# resolverLarinto: List -> set -> List -> Dict -> (int, int) -> Dict
# La funcion toma un lista inicializada con el incio del laberinto, un Set vacio que representara 
# los lugares del laberinto ya visitados, una lista de listas que representara al laberinto 
# un diccionario en el cual se almacenara en la key un nodo y en el value de dicha key el nodo el nodo anterios
# es decir, como llegar al nodo.
# La funcion emplea el algorimo de DFS y corta cuando encuentra el fin del laberinto que es el ultimo paramtro que
# se le pasa a la funcion 
def ResolverLarinto(aVisitar, Visitadas,Array,Padres,fin):
    pila = []
    flag = 0
    inicio = aVisitar.pop(0)
    Visitadas.add(inicio)
    pila.append(inicio)
    while pila != [] and flag == 0 :
        vertice = pila.pop()
        (y,x) = vertice
        pilaAux = []
        if vertice != fin :
            pilaAux,Padres,Visitadas = Prueba(vertice,y, x-1,Array,pilaAux.copy(),Visitadas.copy(),Padres.copy())
            pilaAux,Padres,Visitadas = Prueba(vertice,y, x+1,Array,pilaAux.copy(),Visitadas.copy(),Padres.copy())
            pilaAux,Padres,Visitadas = Prueba(vertice,y-1, x,Array,pilaAux.copy(),Visitadas.copy(),Padres.copy())
            pilaAux,Padres,Visitadas = Prueba(vertice,y+1, x,Array,pilaAux.copy(),Visitadas.copy(),Padres.copy())
            # Empleo la funcion sort para ordenar los nodos de la pila, para que la forma de busqueda del DFS
            # sea un poco mas eficiente.
            pilaAux.sort(key=(lambda vecino: abs(fin[0] - vecino[0]) + abs(fin[1] - vecino[1])), reverse=True)
            pila += pilaAux        
        else:
            flag = flag + 1
    return Padres

#Pueba: (int, int) -> int -> int -> List -> List -> set -> Dict -> (List, Dict, set)
#La funcion toma como paramtros el nodo actual en el cual se esta trabajando, una coordenada de un punto 
# que es representada como los paramtereos y e x, el laberinto representado como una lista de listas
# el conjunto de nodos visitados y el diccionario en el cual se alamcenan los padres de los nodos
# La funcion se fija si los X e Y que se ingresa son validos y luego si lo son, se fija si es una pared o un 
# lugar trnasitable, si es el inicio o el fin y si no fue visiada anteriormentr. Si cumple con todo esto,
# dentro del  diccionario de padres, agraga al nodo actual como padre de la posicion pasada como argumento
# marca como visitado al nodo nuevo, agrega al nuevo nodo a
# la parde de nodos a visitar  y luego devuelve el  nuevo diccionario y lista de los nodos a vistar y el
# conjunto de los nodos ya visitados  
def Prueba(actual,y,x,Array,pila,Visitadas,Padres):
    max = len(Array)
    if( y < (max) and y >= 0 and x < (max) and x >= 0):
        if (Array[y][x] == "0" or Array[y][x] == "X" or Array[y][x] == "I" ) and (not (y,x) in Visitadas):
            pila.append((y,x))
            Visitadas.add((y,x))
            Padres[(y,x)]=actual
    
    return pila,Padres,Visitadas
def main():
    solucion = False
    error = False
    archivoEntradaC = sys.argv[1]
    archivoSalidaC = sys.argv[2]
    archivoSolucion = sys.argv[3]
    #Controlo si el laberinto que se creo es resolvible, por defeto no lo es y entra al ciclo
    while(solucion == False and error == False):
        #Llamo al programa en C con el ejecutable y el nombre del archivo con los parametros del laberinto
        respuesta = subprocess.run(["./a.exe",archivoEntradaC, archivoSalidaC]).returncode
        #si la respuesta del Main del archivo en C es 0 significa que se pudo ejecutar sin problemas
        if (respuesta == 0):
            Array = []
            PosicionInicial , Fin = TomarEntrada(archivoSalidaC,Array)
            Visitadas = set()
            PorVisitar = [PosicionInicial]
            Padres = {}
            Padres [PosicionInicial] = PosicionInicial
            Padres = ResolverLarinto(PorVisitar,Visitadas,Array,Padres,Fin)
            Abuscar = Fin
            recorrido = []
            Salida = open(archivoSolucion, "w+")
            #si el fin del laberinto posee un padre, o un nodo predecesor, entonces significa que se pudo resolver
            if(Abuscar in Padres.keys() ):
                while (Abuscar != PosicionInicial ):
                    (x,y) = Abuscar
                    x += 1
                    y += 1
                    recorrido.append((y,x))
                    Abuscar = Padres[Abuscar]
                solucion = True 
                recorrido.append(PosicionInicial)
                recorrido.reverse()
                for linea in recorrido:
                    Salida.write(str(linea) + "\n")
            else:
                solucion == False
        else :
            error == True
            print("error en el archivo de C")
if __name__ == "__main__":
    main()