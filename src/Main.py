from DataLoader import DataLoader
from dwave.system import LeapHybridCQMSampler
import numpy as np


def main():
    # m: num of products
    # n: num of suppliers

    # Debug dataset
    # m, n = 5, 3
    # Small dataset
    # m, n = 20, 10
    # Medium dataset
    # m, n = 100, 40
    # Large dataset
    # m, n = 200, 80

    filename = "data/SMALL-DATASET.csv"

    # Load data and maps the SC problem to a BLP problem
    dl = DataLoader()
    dl.loadFromCSV(filename)
    blp = dl.generateBLP()
    print(f"num of suppliers {dl.n}")
    print(f"num of products {dl.m}")

    # Construct CQM and sample
    blp.constructCQM()
    blp.sample(LeapHybridCQMSampler())
    outcome = blp.processOutcome()
    print(f"num of suppliers selected {np.sum(outcome)}")


main()
