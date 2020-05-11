"""
1. Construct two symmetric 2x2 matrices **A** and **B**.
   *Hint: a symmetric matrix can be constructed easily from a square matrix
   as **Asym** = **A** + **A**^T*
2. Calculate the matrix product **C** = **A** * **B** using `numpy.dot()`.
3. Calculate the eigenvalues of matrix **C** with `numpy.linalg.eigvals()`.
"""

import numpy as np

A = np.random.random((2,2))

B = np.random.random((2,2))

A = A + A.T

B = B + B.T

C = A @ B

print(np.linalg.eigvals(C))