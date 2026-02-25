import numpy as np

def stable_noise_func(alpha, beta, size=1):

  if not 0 < alpha <= 2:
    raise ValueError("alpha must be in the range (0, 2]")
  if not -1 <= beta <= 1:
    raise ValueError("beta must be in the range [-1, 1]")

  U = np.random.uniform(-np.pi/2, np.pi/2, size=size)
  E = np.random.exponential(1, size=size)

  if alpha != 1:
    # Chambers-Mallows-Stuck method for alpha != 1
    b = np.arctan(beta * np.tan(np.pi * alpha / 2)) / alpha
    s = (1 + (beta * np.tan(np.pi * alpha / 2))**2)**(1/(2 * alpha))

    term1 = np.sin(alpha * (U + b))
    term2 = np.cos(U)**(-1/alpha)
    term3 = np.cos(U - alpha * (U + b))

    # Cast to complex to avoid nans due to exponentiation (use abs to keep real-valued result)
    X = s * term1 * term2 * (np.abs(term3 / E))**((1 - alpha) / alpha)
  else:
    # alpha == 1 special case
    term = (np.pi / 2) + beta * U
    X = (2 / np.pi) * (term * np.tan(U) - beta * np.log((np.pi / 2) * E * np.cos(U) / term))

  return X
