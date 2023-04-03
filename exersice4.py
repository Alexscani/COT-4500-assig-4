# for L and U matrix using scipy lib

import pprint
import scipy
import scipy.linalg

A = scipy.array([ [1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1] ])
P, L, U = scipy.linalg.lu(A)


print('\n Base matrix ')
pprint.pprint(A)
print('\n Matrix determinant: ')
pprint.pprint(P)
print('\n L matrix : ')
pprint.pprint(L)
print('\n U matrix : ')
pprint.pprint(U)
