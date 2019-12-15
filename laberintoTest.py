import laberinto
# Casos de test (pytest) para el trabajo final.
# Se testea el retorno del inicio y el objetivo de los laberintos leidos,
# y la matriz modificada por referencia
# Por test, en el archvo de los resultados tenemos el inicio como una tupla de int,
# el objetivo como una tupla de int y el laberinto como una lista de lista de chars
def test_TomarEntradaTest():
    laberinto1 = []
    laberinto2 = []
    laberinto3 = []
    laberintoTest1 = "laberintoTest1.txt"
    laberintoTest2 = "laberintoTest2.txt"
    laberintoTest3 = "laberintoTest3.txt"
    Entrada1 = open("test1-1.txt", "r")
    lineas = Entrada1.readlines()
    inicio1 = eval(lineas[0])
    objetivo1 = eval(lineas[1])
    matriz1 = eval(lineas[2])
    inicio2 = eval(lineas[3])
    objetivo2 = eval(lineas[4])
    matriz2 = eval(lineas[5])
    inicio3 = eval(lineas[6])
    objetivo3 = eval(lineas[7])
    matriz3 = eval(lineas[8])
    assert laberinto.TomarEntrada(laberintoTest1, laberinto1) == (inicio1, objetivo1)
    assert laberinto1 == matriz1
    assert laberinto.TomarEntrada(laberintoTest2, laberinto2) == (inicio2, objetivo2)
    assert laberinto2 == matriz2
    assert laberinto.TomarEntrada(laberintoTest3, laberinto3) == (inicio3, objetivo3)
    assert laberinto3 == matriz3

def test_ResolverLaberintoTest():
    Entrada1 = open("test2-1.txt","r")
    lineas = Entrada1.readlines()
    laberinto1 =  eval(lineas[0])
    Avisitar1 = eval(lineas[1])
    visitadas1 = set()
    Padres1 = dict()
    fin1 = eval(lineas[2])
    laberinto2 = eval(lineas[3])   
    Avisitar2 = eval(lineas[4])
    visitadas2 = set()
    Padres2 = dict()
    fin2 = eval(lineas[5])
    laberinto3 = eval(lineas[6])
    Avisitar3 = eval(lineas[7])
    visitadas3 = set()
    Padres3 = dict()
    fin3 = eval(lineas[8])
    Entrada2 = open("test2-2.txt", "r")
    lineas2 = Entrada2.readlines()
    padres1 = eval(lineas2[0])
    padres2 = eval(lineas2[1])
    padres3 = eval(lineas2[2])
    assert laberinto.ResolverLarinto(Avisitar1, visitadas1,laberinto1,Padres1,fin1) == padres1
    assert laberinto.ResolverLarinto(Avisitar2, visitadas2,laberinto2,Padres2,fin2) == padres2
    assert laberinto.ResolverLarinto(Avisitar3, visitadas3,laberinto3,Padres3,fin3) == padres3
def test_PruebaTest():
    actual1 = (3,3)
    x1 = 3
    y1 = 4
    laberinto1 = [['1','1','1','1','0','0','0','0'],['0','I','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','1','0','0'],['0','0','0','1','0','0','0'],['0','1','0','0','0','0','0','X']]
    pila1 = []
    visitadas1 = set()
    padres1 = dict()
    actual2 = (0,0)
    x2 = 0
    y2 = -1
    laberinto2 = [['1','1','1','1','0','0','0','0'],['0','I','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','1','0','0'],['0','0','0','1','0','0','0'],['0','1','0','0','0','0','0','X']]
    pila2 = []
    visitadas2 = set()
    padres2 = dict()    
    actual3 = (3,3)
    x3 = 3
    y3 = 4
    laberinto3 = [['1','1','1','1','0','0','0','0'],['0','I','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','1','0','0'],['0','0','0','1','0','0','0'],['0','1','0','0','0','0','0','X']]
    pila3 = []
    visitadas3 = {(3,4)}
    padres3 = dict()
    Entrada1 = open("test3-2.txt", "r")
    lineas = Entrada1.readlines()
    pilatest1 = eval(lineas[0])
    Padretest1 = eval(lineas[1])
    visitadastest1 = eval(lineas[2])
    pilatest2 = eval(lineas[3])
    Padretest2 = eval(lineas[4])
    visitadastest2 = eval(lineas[5])
    pilatest3 = eval(lineas[6])
    Padretest3 = eval(lineas[7])
    visitadastest3 = eval(lineas[8])
    assert laberinto.Prueba(actual1,x1,y1,laberinto1,pila1,visitadas1,padres1) == (pilatest1,Padretest1,visitadastest1)
    assert laberinto.Prueba(actual2,x2,y2,laberinto2,pila2,visitadas2,padres2) == (pilatest2,Padretest2,visitadastest2)
    assert laberinto.Prueba(actual3,x3,y3,laberinto3,pila3,visitadas3,padres3) == (pilatest3,Padretest3,visitadastest3)
    