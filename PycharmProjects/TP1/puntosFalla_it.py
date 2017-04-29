import sys
from time import time
import digrafo

# Version iterativa
# Llama a la funcion Puntos_Falla con parametro por linea de comando
# Lleva un solo parametro, a elegir entre: g1, g2 , g3, g4, g5, g6

# Ejemplo de linea de comando: puntosFalla_it.py g1

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
	
	# lista para guardar los visitados
	visitado = []
	
	# marca todos los vertices como no visitados
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
	
	# crea e inicializa la pila y pila_aux
	pila = []
	pila.append(0)
	
	pila_aux = set()
	pila_aux.add(0)
	
	# contador de puntos de articulacion
	cant_p = 0
	
	# momento de descubrimiento
	momento = 0
	
	# para medir la ejecucion
	inicio = time()
	
	# visita los nodos del grafo usando DFS, creando las listas de
	# visitados, descubrimiento, bajo, cantidad de hijos y ancestros
	while pila:
		v = pila.pop()
		if visited[v] == False:			
			visited[v] = True
			visitado.append(v)
			descubrimiento[v] = momento
			bajo[v] = momento
			momento += 1
			
			# agrega a la pila los adyacentes del nodo no visitados,
			for i in grafo.adyacentes[v]:
				if (visited[i] == False) and (i not in pila_aux):
					pila_aux.add(i)
					pila.append(i)
					cant_h[v] += 1
					ancestro[i] = v
					bajo[v] = min(bajo[v], bajo[i])
	
	# recorre visitados, obtiene puntos de articulacion
	while visitado:
		v = visitado.pop()		
		a = ancestro[v]
		
		# si el nodo es raiz y tiene dos o mas hijos, 
		# el nodo es punto de articulacion
		if (a == -1) and (cant_h[v] >= 2): 
			puntos[v] = True

		# si el nodo no es raiz, y su valor bajo es mayor o igual
		# al momento de descubrimiento de su ancestro, 
		# entonces el ancestro es punto de articulacion 
		if (a != -1)  and (bajo[v] >= descubrimiento[a]): 
			puntos[a] = True	
			      
	fin = time()
	
	#---------------------------
	
	# muestra el resultado y el tiempo utilizado
	print("\nPuntos de falla, version iterativa")
	print('Archivo: ',arch,".txt")
	print('Cantidad de vertices: ', cant_v)
	print('Cantidad de aristas : ', cant_a)
	print("Puntos de articulacion : ",end="")
	for index, value in enumerate (puntos):
		if value == True:
			print(index,end=" ")
			cant_p += 1
	print("\nCantidad de puntos de articulacion: ", cant_p)
	print('Tiempo de ejecucion: ', (fin - inicio) * 1000, 'milisegundos\n')
	
# -----------------------------------------

Puntos_Falla()

# -----------------------------------------


