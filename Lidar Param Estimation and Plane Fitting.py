import numpy as np

def sph_to_cart(epsilon, alpha, r):
    """
    Transform sensor readings to Cartesian coordinates in the sensor frames.
    """
    p = np.zeros(3)  # Position vector

    # Convert spherical to Cartesian coordinates
    p[0] = r * np.cos(alpha) * np.cos(epsilon)
    p[1] = r * np.sin(alpha) * np.cos(epsilon)
    p[2] = r * np.sin(epsilon)

    return p

def estimate_params(P):
    """
    Estimate parameters from sensor readings in the Cartesian frame.
    Each row in the P matrix contains a single measurement.
    """
    param_est = np.zeros(3)

    one_mat = np.ones((len(P), 1))
    print(one_mat.shape)

    x = P[:, 0].reshape(-1, 1)
    print(x.shape)

    y = P[:, 1].reshape(-1, 1)
    print(y.shape)

    z = P[:, 2].reshape(-1, 1)
    print(z.shape)

    B = z
    A = np.hstack((one_mat, x, y))
    print(A.shape)

    params = np.linalg.inv(A.T @ A) @ A.T @ B

    param_est[0] = params[0, 0]
    param_est[1] = params[1, 0]
    param_est[2] = params[2, 0]

    return param_est

# Example usage
print(sph_to_cart(5, 10, 4))
P = np.random.rand(20, 3)
q = estimate_params(P)
print(q)
