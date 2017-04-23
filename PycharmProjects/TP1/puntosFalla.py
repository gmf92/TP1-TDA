import sys
from time import time
import digrafo


# Llamar a la funcion Puntos_Falla con parametro por linea de comando
# Lleva un solo parametro, a elegir entre: g1, g2 , g3, g4
# Ejemplo: puntosFalla.py g1

def Puntos_Falla():
	
	# abre un archivo con datos
	arch = str(sys.argv[1])
	archivo = open(arch + ".txt",'r')
	
	# obtiene cantidad de vertices y aristas
	cant_v = int(archivo.readline())
	cant_a = int(archivo.readline())
	
	# crea un grafo con cant_v vertices, sin aristas
	grafo = digrafo.Digrafo(cant_v)
	
	# obtiene las aristas y las agrega al grafo
	for i in range(cant_a):		
		o, d = archivo.readline().split(" ")
		grafo.agregarArista(int(o), int(d))
		grafo.agregarArista(int(d), int(o))
	
	# cierra el archivo
	archivo.close()

	# ---------------------------------

	# para medir la ejecucion
	inicio = time()
	
	# marca todos los vertices como no visitados
	visitado = [False] * (cant_v)
	
	# inicializa momentos de descubrimiento
	descubrimiento = [0] * (cant_v)
	
	# inicializa valores bajo
	bajo = [0] * (cant_v)
	
	# inicializa ancestros
	ancestro = [-1] * (cant_v)
	
	# inicializa puntos de articulacion
	puntos = [False] * (cant_v)
	
	#inicializa cantidad de hijos para cada vertice
	cant_h = [0] * (cant_v)
	
	# inicializa momento del descubrimiento
	momento = 0
	
	# contador de puntos de articulacion encontrados
	cant_p = 0

	sys.setrecursionlimit(50000)

    # llama al metodo recursivo para cada vertice
	for i in range(cant_v):		
		if visitado[i] == False: 
			visitado[i] = True				
			PADFS(grafo, cant_h, i, visitado, bajo, descubrimiento, momento, cant_p, ancestro, puntos)
			
	# para medir la ejecucion
	fin = time()

	print("\nPuntos de falla, version recursiva")
	# muestra el resultado y el tiempo utilizado	
	print('Archivo: ',arch,".txt",sep="")
	#print(grafo.obtenerGrafo())
	
	# cuenta y muestra los puntos de articulación encontrados
	print('Cantidad de vertices: ', cant_v)
	print('Cantidad de aristas : ', cant_a)
	print("Puntos de articulacion : ",)
	for index, value in enumerate (puntos):
		if value == True:
			print(index, " ",end="")
			cant_p += 1
	print("\nCantidad de puntos de articulacion: ", cant_p)
	print('Tiempo de ejecucion: ', (fin - inicio) * 1000, 'milisegundos\n')


# funcion recursiva para encontrar puntos de articulacion
def PADFS(grafo, cant_h, a, visitado, descubrimiento, bajo, momento, cant_p, ancestro, puntos):
	# inicializa el nodo actual
	cant_h[a] = 0
	descubrimiento[a] = momento
	bajo[a] = momento

	# recorre los adyacentes del nodo actual
	for v in grafo.adyacentes[a]:
		# si v no fue visitado, lo visita
		if visitado[v] == False:
			visitado[v] = True
			ancestro[v] = a
			cant_h[a] += 1
			momento += 1
			#llama a la funcion recursiva
			PADFS(grafo, cant_h, v, visitado, descubrimiento, bajo, momento, cant_p, ancestro, puntos)

			# asigna al vertice actual el valor bajo minimo
			bajo[a] = min(bajo[a], bajo[v])
			
			# si el nodo actual es raiz y tiene dos o mas hijos, es punto de articulacion
			if (ancestro[a] == -1) and (cant_h[a] > 1):
				if puntos[a] == False: puntos[a] = True

			# si el nodo actual no es raiz, y el valor bajo del hijo es mayor o igual
			# al momento de descubrimiento del actual, el nodo actual es punto de articulacion 
			if ancestro[a] != -1 and bajo[v] >= descubrimiento[a]:
				if puntos[a] == False: puntos[a] = True
						
		# si ya fue visitado y es distinto al ancestro del actual, 
		# se actualiza el valor bajo del actual 
		elif v != ancestro[a]: 
			bajo[a] = min(bajo[a], descubrimiento[v])

# -----------------------------------------

Puntos_Falla()

# -----------------------------------------

