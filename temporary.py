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
    phi = np.arctan(beta * np.tan(np.pi * alpha / 2.0)) / alpha
    term1 = np.sin(alpha * (U + phi))
    term2 = np.cos(U) ** (-1.0 / alpha)
    term3 = np.cos(U - alpha * (U + phi)) / E

    # Use absolute value for the fractional power to avoid invalid values
    X = term1 * term2 * (np.abs(term3) ** ((1.0 - alpha) / alpha))
  else:
    # alpha == 1 special case
    # Formula for alpha == 1
    numerator = (np.pi / 2.0) + beta * U
    X = (2.0 / np.pi) * (numerator * np.tan(U) - beta * np.log((np.pi / 2.0 * E * np.cos(U)) / numerator))

  return X
