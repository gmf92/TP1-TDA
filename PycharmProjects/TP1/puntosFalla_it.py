import sys
from time import time
import digrafo

# Version iterativa
# Llama a la funcion Puntos_Falla con parametro por linea de comando
# Lleva un solo parametro, a elegir entre: g1, g2 , g3, g4, g5, g6

# Ejemplo de linea de comando: puntosfallait.py g1

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
	
	#---------------------------------
	
	# para medir la ejecucion
	inicio = time()
	
	# marca todos los vertices como no visitados
	visitado = []
	visited = [False] * (cant_v)
	
	# inicializa momentos de descubrimiento
	descubrimiento = [0] * (cant_v)
	
	# inicializa valores bajo
	bajo= [0] * (cant_v)
	
	# inicializa ancestros
	ancestro = [-1] * (cant_v)
	
	# inicializa puntos de articulacion
	puntos = [False] * (cant_v)
	
	#inicializa cantidad de hijos para cada vertice
	cant_h = [0] * (cant_v)
	
	#inicializa la pila
	pila = []
	pila.append(0)
	
	# contador de puntos de articulacion
	cant_p = 0
	
	# momento de descubrimiento
	momento = 0
	
	# lista auxiliar
	ext = []
	
	# visita los nodos del grafo, crea las listas de visitados,
	# momentos de descubrimiento, valores bajo, cantidad de hijos,
	# y ancestros de los nodos visitados
	while pila:
		v = pila.pop()
		if visited[v] == False:
			visited[v] = True
			visitado.append(v)
			descubrimiento[v] = momento
			bajo[v] = momento
			momento += 1
			for i in grafo.adyacentes[v]:
				if visited[i] == False:
					ext.append(i)
			pila.extend(ext)
			cant_h[v] = len(ext)
			for w in ext:
				ancestro[w] = v
				bajo[v] = min(bajo[v], bajo[w])
			ext.clear()
	
	# recorre la lista visitados, obteniendo los
	# puntos de articulacion
	while visitado:
		# obtiene un nodo y su ancestro
		v = visitado.pop()		
		a = ancestro[v]
		
		# si el nodo es raiz y tiene dos o mas hijos, 
		# el nodo es punto de articulacion
		if (a == -1) and (cant_h[v] > 1): 
			puntos[v] = True

		# si el nodo no es raiz, y su valor bajo es mayor o igual
		# al momento de descubrimiento de su ancestro, 
		# el ancestro es punto de articulacion 
		if (a != -1)  and (bajo[v] >= descubrimiento[a]): 
			puntos[a] = True	
			      
	# para medir la ejecucion
	fin = time()
	
	#---------------------------
	
	# muestra el resultado y el tiempo utilizado
	print("\nPuntos de falla, version iterativa")
	print('Archivo: ',arch,".txt")
	print('Cantidad de vertices: ', cant_v)
	print('Cantidad de aristas : ', cant_a)
	print("Puntos de articulacion : ")
	for index, value in enumerate (puntos):
		if value == True:
			print(index, " ",end="")
			cant_p += 1
	print("\nCantidad de puntos de articulacion: ", cant_p)
	print('Tiempo de ejecucion: ', (fin - inicio) * 1000, 'milisegundos\n')
	
# -----------------------------------------

Puntos_Falla()

# -----------------------------------------

