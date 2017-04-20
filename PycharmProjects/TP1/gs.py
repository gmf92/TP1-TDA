import queue
from rand4SM import *

def generarPreferencias(E):
        """Devuelve un diccionario que contiene len(E) diccionarios. El diccionario i contiene las preferencias del elemento de índice i.
        Nótese: Menor valor indica mayor preferencia."""
        for i in range(len(E)):
                pref[i] = dict()
                for j in range(len(E[i])):
                        pref[i][E[i][j]] = j

def rangeQueue(n):
        """Devuelve una Cola con elementos de 0 a n encolados ordenadamente"""
        q = queue.Queue()
        for i in range(n):
                pendientes.put(i)
        return q

def GS(A,E):
        """E es una lista que la posición i contiene una lista de índices de la lista A en orden de preferencia para el elemento i. A análogo.
        Emparejamiento Estable. Devuelve un arreglo que indica el índice de la pareja 'a' en el respectivo índice 'e'."""
        n = len(A)
        sig_deseado = [0]*n
        H = [None]*n # H[e] indica indice de pareja 'a' para e.
        pendientes = rangeQueue(n)
        pref = generarPreferencias(E)
        
        while not pendientes.empty():
            a = pendientes.get()
            e_deseado = A[a][sig_deseado[a]]
            a_rival = H[e_deseado]
            if a_rival is None:
                H[e_deseado] = a
            elif pref[e_deseado][a] < pref[e_deseado][a_rival]:
                H[e_deseado] = a
                pendientes.put(a_rival)
            else:
                pendientes.put(a)
            sig_deseado[a] += 1
        return H

