import digrafo
import random

def aleatorio():
	
#Para generar aleatoriamente grafos de v vertices y a aristas sin loops
	
	#diferentes cantidades de vertices
	cantidades = [10, 100, 1000, 10000]
	
	#proporcion de aristas con respecto a vertices
	factor = 2.5
	
	#genera un grafo por cada valor en la lista cantidades
	for v in cantidades:
		
		grafo = digrafo.Digrafo(v)
		
		a = int(v * factor)
		
		for i in range(a):
			ori = random.randint(0,v-1)
			des = ori
			while (des == ori) or (des in grafo.adyacentes[ori]):
				des = random.randint(0,v-1)
			grafo.agregarArista(ori, des)
		
		print("Numero de vertices: " + str(grafo.obtenerNumeroDeVertices()))
		print("Numero de aristas: " + str(grafo.obtenerNumeroDeAristas()))	
		#print("El grafo es: ")
		#print(grafo.obtenerGrafo())
		print("\n")
	
	
aleatorio()
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
