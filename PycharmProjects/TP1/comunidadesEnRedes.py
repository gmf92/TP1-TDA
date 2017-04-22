import digrafo

def comunidadesEnFalla():

    #-----------------------
    # abre un archivo con datos
    archi = open('d1.txt','r')

    # obtiene cantidad de vertices y aristas
    cant_v = int(archi.readline())
    cant_a = int(archi.readline())

    # crea un grafo vacío
    grafo = digrafo.Digrafo(cant_v)

    # obtiene las aristas y las agrega al grafo
    for i in range(cant_a):
        ori, des = archi.readline().split(" ")
        grafo.agregarArista(int(ori), int(des))

    archi.close()
    #------------------------


    imprimirCFC(grafo)


def dfsParaCalcularTf(grafo, v, visitado, pila):
    # Marca el nodo actual como visitado
    visitado[v] = True
    # Se repite para todos los vértices adyacentes al actual
    for i in grafo.adyacentesAlVertice(v):
        if visitado[i] == False:
            dfsParaCalcularTf(grafo, i, visitado, pila)
    pila.append(v)


def dfsGrafoTranspuesto(grafo, v, visitado, componentes):
    # Marca el nodo actual como visitado y lo imprime
    visitado[v] = True

    componentes.append(v)

    # Se repite para todos los vértices adyacentes al actual
    for i in grafo.adyacentesAlVertice(v):
        if visitado[i] == False:
            dfsGrafoTranspuesto(grafo, i, visitado, componentes)


# Esta es la funcion principal que encuentra e imprime todas las CFC
def imprimirCFC(grafo):

    numeroDeCFC = 0
    componentesConexas = []
    pila = []

    # Marco todos los vertices como no visitados (DFS(G))
    visitado = [False] * (grafo.obtenerNumeroDeVertices())

    # Relleno la pila con los vertices de acuerdo con su tiempo de finalizacion
    for i in range(grafo.obtenerNumeroDeVertices()):
        if visitado[i] == False:
            dfsParaCalcularTf(grafo, i, visitado, pila)

    # Calcula la transpuesta del Grafo
    grafoTranspuesto = grafo.transponer()

    # Marco todos los vertices como no visitados (DFS(Gt))
    visitado = [False] * (grafo.obtenerNumeroDeVertices())


    aux = dict()
    # Procesa todos los vértices en el orden definido por la pila
    while pila:
        i = pila.pop()
        if visitado[i] == False:
            dfsGrafoTranspuesto(grafoTranspuesto, i, visitado, componentesConexas)
            numeroDeCFC += 1
            aux[numeroDeCFC-1] = str(componentesConexas)
            componentesConexas.clear()

    componentesConexas = aux

    print("El grafo G tiene " + str(grafo.obtenerNumeroDeVertices()) + " vertices")
    print("El grafo G tiene " + str(grafo.obtenerNumeroDeAristas()) + " aristas")

    print("El grafo G es: ")
    print(grafo.obtenerGrafo())

    print("El grafo G transpuesto es: ")
    print(grafo.transponer().obtenerGrafo())

    print("Estas son las componentes fuertemente conexas del grafo dado:")
    print(componentesConexas)

    print("El grafo G tiene " + str(numeroDeCFC) + " componentes fuertemente conexas")



#---------------------------------

comunidadesEnFalla()

#---------------------------------