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
    term2 = np.cos(U) ** (-1.0 / alpha)
    term3 = np.cos(U - alpha * (U + beta * np.pi / 2))

    # Cast to complex to avoid nans due to exponentiation of negative bases
    term3c = term3 + 0j
    X = term1 * term2 * (term3c / E) ** ((1.0 - alpha) / alpha)
    X = np.real(X)
  else:
    # Special case for alpha == 1
    V = U
    # Using the Chambers-Mallows-Stuck formula for alpha == 1
    X = (2.0 / np.pi) * (
      (np.pi / 2 + beta * V) * np.tan(V)
      - beta * np.log((np.pi / 2 * E * np.cos(V)) / (np.pi / 2 + beta * V))
    )

  return X
