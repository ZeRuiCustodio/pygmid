import numpy as np

def invq(Z):
    # Evaluates y so that Z = 2 * (y - 1) + log(y)
    # Z may be a scalar, a vector, or a matrix
    
    m = np.shape(Z)
    m1, m2 = m[0], m[1]

    if m1 == 1:
        if m2 > 1:
            Z = np.transpose(Z)
            m3 = 1
        else:
            Z = Z
            m3 = m2
    else:
        Z = Z
        m3 = m2

    k = 0
    xx = np.zeros_like(Z)
    
    while k < m3:
        y = Z[:, k]
        a1, b1 = np.where(y <= 0.1)
        Y = y[a1]
        e = 1
        u = Y + 2
        
        while np.max(np.abs(e)) >= 1e-8:
            d = Y - 2 * (np.exp(u) - 1) - u
            e = d / (2 * np.exp(u) + 1)
            u = u + e

        x = np.exp(u)

        a2, b2 = np.where(y > 0.1)
        Y = y[a2]
        e = 1
        X = 1e-4 * b2
        
        while e >= 1e-4:
            z = 2 * (X - 1) + np.log(X)
            u = X * (1 + (Y - z) / (2 * X + 1))
            e = np.max(np.abs((u - X) / X))
            X = u
        
        if len(a2) == 0:
            xx[:, k] = x
        else:
            xx[a2, k] = X
        
        k += 1

    if m1 == 1:
        if m2 > 1:
            y = np.transpose(xx)
        else:
            y = xx
    else:
        y = xx

    return y

# Example usage
# Replace Z with your actual data
Z = np.array([[0.5, 1.0, 2.0], [0.8, 1.2, 0.2]])

result = invq(Z)
print(result)
