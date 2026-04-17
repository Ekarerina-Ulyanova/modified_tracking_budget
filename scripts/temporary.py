import numpy as np


def stable_noise_func(alpha, beta, size=1):
  """
  Generate stable noise using the specified parameters.

  Args:
  - alpha: Exponent parameter for the noise function. Must be in the range (0, 2].
  - beta: Scaling parameter for the noise function. Must be in the range [-1, 1].
  - size: Number of samples to generate (default is 1).

  The method generates stable noise values based on the provided alpha and beta parameters. It uses a stable noise generation algorithm that involves random sampling and mathematical computations. The alpha parameter controls the shape of the noise distribution, while the beta parameter scales the noise values. The size parameter determines the number of noise samples to generate.

  The method handles special cases for different alpha values to ensure accurate noise generation. It returns the generated noise values as a NumPy array unless only one value is generated, in which case it returns a scalar for convenience.
  """

  if not 0 < alpha <= 2:
    raise ValueError("alpha must be in the range (0, 2]")
  if not -1 <= beta <= 1:
    raise ValueError("beta must be in the range [-1, 1]")

  U = np.random.uniform(-np.pi/2, np.pi/2, size=size)
  E = np.random.exponential(1, size=size)

  if alpha != 1:
    B = beta * np.pi / 2
    term1 = np.sin(alpha * (U + B))
    term2 = np.cos(U)**(-1/alpha)
    term3 = np.cos(U - alpha * (U + B))

    # Cast to complex to avoid nans due to exponentiation
    X = term1 * term2 * np.abs((term3 / E) ** ((1 - alpha) / alpha))
  else:
    # alpha == 1 special case (Chambers-Mallows-Stuck)
    B = beta * np.pi / 2
    denom = (np.pi / 2) + beta * U
    X = (2 / np.pi) * (denom * np.tan(U) - beta * np.log((np.pi/2 * E * np.cos(U)) / denom))

  # return scalar when appropriate
  if np.size(X) == 1:
    return np.squeeze(X)
  return X
