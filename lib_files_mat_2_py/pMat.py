import numpy as np

def pMat(T, N, tox):
    # % name : technology vector
    # % computes y = [phiB; Gamma; UT; K; Cox]
    # % versus
    # % 	T absolute temperature				�K   
    # %	N substrate (uniform) doping		cm^-3
    # %		N > 0  for P-type substrate
    # %		N < 0  for N-type substrate
    # % 	tox  oxide thickness   				nm
    # % NOTE: T, N and tox may be scalars or equal length row vectors 
    
    # Physical constants
    T0 = 300.0          # Reference temperature (K)
    UG = 1.205          # Band gap voltage (V)
    q = 1.602e-19       # Electron charge (C)
    UT0 = 0.0259        # Thermal voltage (300 K) (V)
    ni0 = 1.45e10       # Intrinsic concentration (300 K) (cm^-3)
    epsSi = 1.04e-12    # Oxide dielectric permitivity (F/cm)
    epsOx = 0.345e-12   # Silicon dielectric permitivity (F/cm)
    muno = 500.0        # N-type mobility (N = ???) (cm^2/V.s)
    mupo = 190.0        # P-type mobility (N = ???) (cm^2/V.s)
    
    # Change T, N, and tox to equal-size column vectors
    H = [len(T), len(N), len(tox)]
    Y, l = max(enumerate(H), key=lambda x: x[1])
    M = [Y + 1 - H[0], Y + 1 - H[1], Y + 1 - H[2]]
    Z = np.column_stack([T * np.ones(M[0]), N * np.ones(M[1]), tox * np.ones(M[2])])

    # Compute technology matrix
    z = np.sign(N[0])
    mu = ((z + 1) * muno - (z - 1) * mupo) / 2
    k = 0
    y = np.zeros((5, Y))

    while k < Y:
        T = Z[k, 0]
        N = np.abs(Z[k, 1])
        tox = Z[k, 2]

        # Intrinsic concentration (cm^(-3))
        ni = ni0 * np.exp((UG / (2 * UT0)) * (1 - T0 / T)) * ((T / T0) ** 1.5)
        # Thermal voltage (V)
        UT = UT0 * (T / T0)
        # Bulk potential (V)
        phiB = z * UT * np.log(N / ni)
        # Oxide capacitance per unit area (F/cm^2)
        Cox = epsOx / (tox * 1e-7)
        # Gamma (body effect coefficient) (sqrt(V))
        Gamma = np.sqrt(2 * q * epsSi * N) / Cox
        # uCox (A/V^2)
        K = mu * Cox * (T / T0) ** (-2)

        # Matrix construction
        y[:, k] = [phiB, Gamma, UT, K, Cox]
        k += 1

    return y

# Example usage
# Replace T, N, tox with your actual data
T = np.array([300.0, 310.0, 320.0])
N = np.array([1e15, 2e15, 3e15])
tox = np.array([5.0, 6.0, 7.0])

result = pMat(T, N, tox)
print(result)
