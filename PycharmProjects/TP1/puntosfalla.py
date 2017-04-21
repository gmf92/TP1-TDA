import digrafo
from time import time

def Puntos_Falla(arch):
	
	# abre un archivo con datos
	archivo = open(arch,'r')
	
	# obtiene cantidad de vertices y aristas
	cant_v = int(archivo.readline())
	cant_a = int(archivo.readline())
	
	# crea un grafo vacío
	grafo = digrafo.Digrafo(cant_v)
	
	# obtiene las aristas y las agrega al grafo
	for i in range(cant_a):		
		o, d = archivo.readline().split(" ")
		grafo.agregarArista(int(o), int(d))
	
	# cierra el archivo
	archivo.close()
	
	# para medir la ejecucion
	inicio = time()
	
	# marca todos los vertices como no visitados
	visitado = [False] * (cant_v)
	
	# inicializa momentos de descubrimiento
	descubrimiento = [float] * (cant_v)
	
	# inicializa valores bajo
	bajo = [float] * (cant_v)
	
	# inicializa ancestros
	ancestro = [-1] * (cant_v)
	
	# inicializa puntos de articulacion
	puntos = [False] * (cant_v)
	
	# inicializa momento del descubrimiento
	momento = 0
	
	# cantidad de puntos de articulacion
	cant_p = 0
	
	# llama al metodo recursivo para cada vertice
	for i in range(cant_v):			
		if visitado[i] == False:				
			PADFS(grafo, i, visitado, puntos, ancestro, bajo, descubrimiento, momento)
			
	# para medir la ejecucion
	fin = time()
			
	# cuenta los puntos de articulación	
	for i in range(cant_v):	
		if puntos[i] == True:
			#print(i)
			cant_p += 1
	
	# muestra el resultado y el tiempo utilizado	
	print('Archivo: ', arch)
	#print(grafo.obtenerGrafo())
	print('Cantidad de vertices: ', cant_v)
	print('Cantidad de aristas : ', cant_a)
	print("Cantidad de puntos de articulacion: ", cant_p)
	print('Tiempo de ejecucion: ', (fin - inicio) * 1000, 'milisegundos\n')


# metodo recursivo para encontrar puntos de articulacion
def PADFS(grafo, a, visitado, descubrimiento, ancestro, puntos, bajo, momento):

	# inicializa contador de hijos del nodo actual
	cant_h = 0

	# marca el nodo actual como visitado
	visitado[a] = True

	# inicializa momento de descubrimiento y valor bajo
	descubrimiento[a] = momento
	bajo[a] = momento
	
	# incrementa el momento
	momento += 1

	# recorre los adyacentes del nodo actual
	for v in grafo.adyacentes[a]:
		
		# si v no fue visitado, se agrega como hijo del actual, y se visita
		if visitado[v] == False:
			ancestro[v] = a
			cant_h += 1
			PADFS(grafo, v, visitado, descubrimiento, ancestro, puntos, bajo, momento)

			# asigna al vertice actual el valor bajo minimo
			bajo[a] = min(bajo[a], bajo[v])
				
			# si el nodo actual es raiz y tiene dos o mas hijos, es punto de articulacion
			if ancestro[a] == -1 and cant_h > 1:
				puntos[a] = True

			# si el nodo actual no es raiz, y el valor bajo del hijo es mayor o igual
			# al momento de descubrimiento del actual, el nodo actual es punto de articulacion 
			if ancestro[a] != -1 and bajo[v] >= descubrimiento[a]:
				puntos[a] = True
				
		# si ya fue visitado y es distinto al ancestro del actual, 
		# se actualiza el valor bajo del actual 
		elif v != ancestro[a]: 
			bajo[a] = min(bajo[a], descubrimiento[v])

# -----------------------------------------

# cantidad de archivos a procesar
cant_arch = 6

for i in range(cant_arch):
	Puntos_Falla('g' + str(i+1) + '.txt')

# -----------------------------------------

