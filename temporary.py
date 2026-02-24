import numpy as np

def stable_noise_func(alpha, beta, size=1):

  if not 0 < alpha <= 2:
    raise ValueError("alpha must be in the range (0, 2]")
  if not -1 <= beta <= 1:
    raise ValueError("beta must be in the range [-1, 1]")

  U = np.random.uniform(-np.pi/2, np.pi/2, size=size)
  E = np.random.exponential(1, size=size)

  if alpha != 1:
    term1 = np.sin(alpha * (U + beta * np.pi / 2))
    term2 = np.cos(U)**(-1/alpha)
    term3 = np.cos(U - alpha * (U + beta * np.pi / 2))

    # Cast to complex to avoid nans due to exponentiation
    base = term3 / E
    base = base.astype(np.complex128)
    X = term1 * term2 * (base) ** ((1 - alpha) / alpha)
    return np.real(X)
  else:
    # alpha == 1 special case (Chambers-Mallows-Stuck formula)
    phi = U
    part1 = (np.pi / 2) + beta * phi
    X = (2 / np.pi) * (part1 * np.tan(phi) - beta * np.log((np.pi / 2 * E * np.cos(phi)) / part1))
    return X
