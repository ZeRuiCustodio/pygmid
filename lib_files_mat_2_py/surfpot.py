import numpy as np

def surfpot(p, V, VG):
    # Computes the surface potential of MOS transistors
    
    # p is the technology vector p = pMat(T, N, tox)
    # V and VG may be scalars or equal-length column vectors
    
    # Voltage matrix
    H = [len(V), len(VG)]
    Y, I = max(enumerate(H), key=lambda x: x[1])
    M = [Y + 1 - H[0], Y + 1 - H[1]]
    Z = np.column_stack([np.ones(M[0]) * V, np.ones(M[1]) * VG])

    # Surface potential
    precision = 1e-8
    m = p.shape
    n = 0

    y = np.zeros((Y, m[1]))

    while n < m[1]:
        phi = p[0, n]
        Gamma = p[1, n]
        Gamsq = Gamma**2
        UT = p[2, n]

        k = 0
        while k < Y:
            U = Z[k, 0]
            UG = Z[k, 1]

            psi = (-Gamma/2 + np.sqrt(Gamsq/4 + UG))**2

            if U < (psi - 2*phi - 0.05):
                x = U + 0.5
                ps = psi

                while abs((x - ps) / x) > precision:
                    ps = x
                    A = ((ps - UG)**2 - Gamsq*ps) / (Gamsq*UT)
                    B = 2*(ps - UG)/Gamsq - 1
                    C = B/A
                    x = (2*phi + U + UT*np.log(A) - C*ps) / (1 - C)
            else:
                x = U + 0.5
                ps = psi

                while abs((x - ps) / x) > precision:
                    ps = x
                    A = np.exp((ps - 2*phi - U) / UT)
                    B = np.sqrt(ps + UT*A)
                    C = -Gamma * (1 + A) / (2*B)
                    x = (UG - Gamma*B - C*ps) / (1 - C)

            y[k, n] = np.real(x)
            k += 1

        n += 1

    return y

# Example usage
# Replace p, V, VG with your actual data
p = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
V = np.array([0.1, 0.2, 0.3])
VG = np.array([0.5, 0.6, 0.7])

result = surfpot(p, V, VG)
print(result)
