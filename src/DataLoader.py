from models import BinaryLinearProgramming, SetCover
import numpy as np


class DataLoader:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.A = None

    def loadFromCSV(self, filename: str):
        """
        Load data form CSV file
        """
        with open(filename, 'r') as f:
            raw = f.readlines()
        raw = raw[1:]
        raw = raw[:-1]
        print(raw[-1])
        self.A = np.array([[float(cost)
                          for cost in line.split(',')[1:]] for line in raw]).T
        self.m, self.n = self.A.shape

    def generateBLP(self) -> BinaryLinearProgramming:
        """
        Generate a Binary Linear Programming problem
        """
        A = np.copy(self.A)
        A[A > 0] = 1
        A[A < 0] = 0
        print(A)
        return BinaryLinearProgramming(A, np.ones(self.m), np.ones(self.n))

    def generateSC(self) -> SetCover:
        """
        Generate a Set Cover problem
        """
        U = {i for i in range(self.m)}
        V = {i: set() for i in range(self.n)}
        for i in range(self.m):
            for j in range(self.n):
                if self.A[i, j] > 0:
                    V[j].add(i)
        return SetCover(U, V)
