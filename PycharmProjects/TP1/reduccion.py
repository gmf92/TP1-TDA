from gs  import *
from rand4SM import *
import time

def ResidenciasASM(E,H,Q):
    A = []
    for i in range(len(Q)-1):
        A.append([])
        for j in range(Q[i]):
            A[i] += H[i]
    print('A',A )
    return GS(A,E)

#n = m = 100
start_time = time.clock()
E, H, Q = generarEntradasSM(10,10)
ResidenciasASM(E,H,Q)
print(time.clock() - start_time)

