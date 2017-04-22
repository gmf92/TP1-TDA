
class Digrafo:
    """Grafo dirigido con un número fijo de vértices.

      Los vértices son siempre números enteros no negativos. El primer vértice es 0.

      El grafo se crea vacío, se añaden las aristas con agregarArista(). Una vez
      creadas, las aristas no se pueden eliminar, pero siempre se pueden añadir
      nuevas aristas."""

    def __init__(self, v):
        self.vertices = v
        self.aristas = 0
        self.adyacentes = dict()
        for i in range(v):
            self.adyacentes[i] = []

    def __str__(self):
        return str(self.adyacentes)

    def obtenerNumeroDeVertices(self):
        return self.vertices

    def obtenerNumeroDeAristas(self):
        return self.aristas

    def agregarArista(self, verticeOrigen, verticeDestino):
        self.adyacentes[verticeOrigen].append(verticeDestino)
        self.aristas += 1

    def adyacentesAlVertice(self, v):
        return self.adyacentes[v]

    def transponer(self):
        transpuestaDelGrafo = Digrafo(self.vertices)
        for i in self.adyacentes:
            for j in self.adyacentes[i]:
                transpuestaDelGrafo.agregarArista(j,i)
        return transpuestaDelGrafo

    #Imprime cada vertice con sus aristas
    def obtenerGrafo(self):
        s = "Vertice -> Adyacentes\n"
        for i in self.adyacentes:
            s += str(i) + " -> "
            for j in self.adyacentes[i]:
                s += str(j) + " "
            s += "\n"
        return s

