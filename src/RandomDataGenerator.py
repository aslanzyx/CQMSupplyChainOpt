import numpy as np


def generateRandomBLP(m: int, n: int, full_coverage=False):
    if full_coverage:
        return NotImplementedError()
    else:
        return np.random.randint(0, 2, (m, n))