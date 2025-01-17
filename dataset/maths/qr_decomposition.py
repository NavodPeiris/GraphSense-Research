import numpy as np


def qr_householder(a: np.ndarray):
    m, n = a.shape
    t = min(m, n)
    q = np.eye(m)
    r = a.copy()

    for k in range(t - 1):
        
        x = r[k:, [k]]
        
        e1 = np.zeros_like(x)
        e1[0] = 1.0
        
        alpha = np.linalg.norm(x)
        
        v = x + np.sign(x[0]) * alpha * e1
        v /= np.linalg.norm(v)

        
        q_k = np.eye(m - k) - 2.0 * v @ v.T
        
        q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), q_k]])

        q = q @ q_k.T
        r = q_k @ r

    return q, r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
