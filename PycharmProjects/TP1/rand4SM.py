from random import shuffle, randint

def generarEntradasSM(n,m):
    
    E, H, Q = [],[],[]
    for i in range(n):
        aux = list(range(m))
        shuffle(aux)
        E.append(aux)    
    vacantesTotales = 0
    for i in range(m):
        aux = list(range(n))
        shuffle(aux)
        H.append(aux)
        vacantes = randint(1,n//m)
        vacantesTotales += vacantes
        if (i == m-1 and vacantesTotales < n):
            Q.append(n-vacantes)
            break
        Q.append(vacantes)

    return E,H,Q

    
    
