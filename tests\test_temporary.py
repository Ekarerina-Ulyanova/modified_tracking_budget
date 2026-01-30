```python
import pytest
import numpy as np
from temporary import stable_noise_func

@pytest.fixture
def alpha_beta_values():
    return [
        (0.5, 0.5),
        (1.0, 0.0),
        (1.5, -0.5),
        (2.0, 1.0),
        (0.0, 0.0),  # invalid alpha value
        (3.0, 0.0),  # invalid alpha value
        (-1.0, 0.0),  # invalid beta value
        (1.0, -2.0)  # invalid beta value
    ]

def test_stable_noise_func_valid_alpha_beta(alpha_beta_values):
    for alpha, beta in alpha_beta_values:
        with pytest.raises(ValueError):
            stable_noise_func(alpha, beta)

def test_stable_noise_func_invalid_alpha(alpha_beta_values):
    for alpha, beta in alpha_beta_values:
        if not 0 < alpha <= 2:
            with pytest.raises(ValueError):
                stable_noise_func(alpha, beta)

def test_stable_noise_func_invalid_beta(alpha_beta_values):
    for alpha, beta in alpha_beta_values:
        if not -1 <= beta <= 1:
            with pytest.raises(ValueError):
                stable_noise_func(alpha, beta)

def test_stable_noise_func_alpha_1():
    X = stable_noise_func(1.0, 0.0)
    assert X.shape == (1,)  # default size is 1

def test_stable_noise_func_alpha_1_size_10():
    X = stable_noise_func(1.0, 0.0, size=10)
    assert X.shape == (10,)  # size is 10

def test_stable_noise_func_alpha_1_beta_0():
    X = stable_noise_func(1.0, 0.0)
    assert np.allclose(X, np.sin(np.linspace(-np.pi/2, np.pi/2, 100)))

def test_stable_noise_func_alpha_1_beta_1():
    X = stable_noise_func(1.0, 1.0)
    assert np.allclose(X, np.sin(np.linspace(-np.pi/2, np.pi/2, 100) + np.pi/2))

def test_stable_noise_func_alpha_1_beta_minus1():
    X = stable_noise_func(1.0, -1.0)
    assert np.allclose(X, np.sin(np.linspace(-np.pi/2, np.pi/2, 100) - np.pi/2))

def test_stable_noise_func_alpha_2():
    X = stable_noise_func(2.0, 0.0)
    assert np.allclose(X, np.sin(2.0 * np.linspace(-np.pi/2, np.pi/2, 100)))

def test_stable_noise_func_alpha_0_5():
    X = stable_noise_func(0.5, 0.0)
    assert np.allclose(X, np.sin(0.5 * np.linspace(-np.pi/2, np.pi/2, 100)) * np.cos(np.linspace(-np.pi/2, np.pi/2, 100))**(-2))

def test_stable_noise_func_alpha_0_5_beta_0_5():
    X = stable_noise_func(0.5, 0.5)
    assert np.allclose(X, np.sin(0.5 * np.linspace(-np.pi/2, np.pi/2, 100) + 0.5 * np.pi) * np.cos(np.linspace(-np.pi/2, np.pi/2, 100))**(-2))

def test_stable_noise_func_alpha_0_5_beta_minus0_5():
    X = stable_noise_func(0.5, -0.5)
    assert np.allclose(X, np.sin(0.5 * np.linspace(-np.pi/2, np.pi/2, 100) - 0.5 * np.pi) * np.cos(np.linspace(-np.pi/2, np.pi/2, 100))**(-2))
```