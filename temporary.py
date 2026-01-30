def stable_noise_func(alpha: float, beta: float, size: int = 1) -> np.ndarray:
    """
    Generates a stable noise function.

    Parameters:
    alpha (float): The parameter controlling the shape of the noise.
    beta (float): The parameter controlling the shift of the noise.
    size (int, optional): The number of samples to generate. Defaults to 1.

    Returns:
    np.ndarray: The generated noise.

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
        X = np.sin(U + beta * np.pi / 2)

    return X