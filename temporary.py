```python
import numpy as np

def stable_noise_func(alpha: float, beta: float, size: int = 1) -> np.ndarray:
    """
    Generates a stable noise function.

    The function uses the formula:
    X = sin(alpha * (U + beta * pi / 2)) * cos(U)^(-1/alpha) * abs(cos(U - alpha * (U + beta * pi / 2)))

    Args:
        alpha (float): The alpha parameter in the noise function formula.
        beta (float): The beta parameter in the noise function formula.
        size (int, optional): The size of the output array. Defaults to 1.

    Raises:
        ValueError: If alpha is not in the range (0, 2] or beta is not in the range [-1, 1].
    """

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
        X = term1 * term2 * np.abs(term3)

    else:
        # If alpha is 1, we can simplify the formula to avoid division by zero
        X = np.sin(U + beta * np.pi / 2)

    return X
```