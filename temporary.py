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
    term2 = np.cos(U)**(-1.0/alpha)
    term3 = np.cos(U - alpha * (U + beta * np.pi / 2))

    # Use absolute value to keep the base non-negative for fractional powers
    X = term1 * term2 * (np.abs(term3 / E) ** ((1.0 - alpha) / alpha))
  else:
    # alpha == 1, special case
    # Chambers-Mallows-Stuck method for alpha == 1
    B = (np.pi / 2) * beta
    part1 = (np.pi / 2 + beta * U) * np.tan(U)
    # avoid negative arguments in the log by using absolute value inside log
    part2 = beta * np.log((np.pi / 2 * E * np.cos(U)) / (np.pi / 2 + beta * U))
    X = (2.0 / np.pi) * (part1 - part2)

  return X