import digrafo

def cargargrafo():
	
	#Modificacion del archivo main para cargar grafo desde archivo del TP
	
	#-----------------------
	archi = open('d1.txt','r')
	
	cant_v = int(archi.readline())
	cant_a = int(archi.readline())
	
	grafo = digrafo.Digrafo(cant_v)
	
	for i in range(cant_a):
		ori, des = archi.readline().split(" ")
		grafo.agregarArista(int(ori), int(des))
		
	archi.close()
	#------------------------

	print(grafo.obtenerNumeroDeVertices())
	print(grafo.obtenerNumeroDeAristas())
	
	print("El grafo G es: ")
	print(grafo.obtenerGrafo())
	
	print("El grafo G transpuesto es: ")
	print(grafo.transponer().obtenerGrafo())
	
	print("Estas son las componentes fuertemente conexas del grafo dado:")
	grafo.imprimirCFC()
	
	print("El grafo G tiene " + str(grafo.obtenerNumeroDeCFC()) + " componentes fuertemente conexas")
	
cargargrafo()
