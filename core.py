import sympy as sp
import scipy as si
import numpy as np


class Udk:

    def __int__(self):
        pass

    def Constraint_Parameters(self, f, *symbols, **flags):
        r"""
            symbolically solves for A and b matrix for the udwadia kalaba theory."""

        pass

    def ideal_Constraint_force(self, m, q, A, b):
        B = A @ si.linalg.fractional_matrix_power(m, -1 / 2)
        a = si.linalg.inv(m) @ q
        Msqrt = si.linalg.fractional_matrix_power(m, 1 / 2)
        e = b - A @ a  # the error vector
        Bplus = np.linalg.pinv(B.astype(np.float64))
        K = Msqrt @ Bplus  # weighted Moore-Penrose generalized inverse of the weighted constraint matrix A
        return K @ e
