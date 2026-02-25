import numpy as np

def stable_noise_func(alpha, beta, size=1):

  if not 0 < alpha <= 2:
    raise ValueError("alpha must be in the range (0, 2]")
  if not -1 <= beta <= 1:
    raise ValueError("beta must be in the range [-1, 1]")

  U = np.random.uniform(-np.pi/2, np.pi/2, size=size)
  E = np.random.exponential(1, size=size)

  if alpha != 1:
    B = beta * np.pi / 2
    term1 = np.sin(alpha * (U + B))
    term2 = np.cos(U) ** (-1.0 / alpha)
    term3 = np.cos(U - alpha * (U + B))

    # Avoid NaNs when raising possibly-negative values to a fractional power
    magnitude = np.power(np.abs(term3 / E), (1.0 - alpha) / alpha)

    X = term1 * term2 * magnitude
  else:
    # Special case for alpha == 1
    # Use the standard CMS formula for alpha == 1
    B = beta * np.pi / 2
    denom = (np.pi / 2) + beta * U
    # Avoid division by zero in denom
    denom = np.where(denom == 0, np.finfo(float).eps, denom)
    X = (2.0 / np.pi) * (denom * np.tan(U)) - beta * np.log((np.pi / 2.0 * E * np.cos(U)) / denom)

  return X
