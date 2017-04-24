from gs  import *
from rand4SM import *
import time


def ResidenciasASM(E,H,Q):
    A = []
    for i in range(len(Q)-1):
        A.append([])
        for j in range(Q[i]):
            A[i] += H[i]
            if (len(A)==len(E)):
                return GS(A,E)
    return GS(A,E)

#n = m = 100
start_time = time.clock()
E, H, Q = generarEntradasSM(100,100)
ResidenciasASM(E,H,Q)
print(time.clock() - start_time)
#n = m = 1000
start_time = time.clock()
E, H, Q = generarEntradasSM(1000,1000)
ResidenciasASM(E,H,Q)
print(time.clock() - start_time)
#n = m = 100000
start_time = time.clock()
E, H, Q = generarEntradasSM(10000,10000)
ResidenciasASM(E,H,Q)
print(time.clock() - start_time)
#n = m = 1000000
start_time = time.clock()
E, H, Q = generarEntradasSM(100000,100000)
ResidenciasASM(E,H,Q)
print(time.clock() - start_time)


