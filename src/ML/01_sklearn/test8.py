from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import requests

def test():
    pass


def main():
    pca = PCA(n_components=0.9)
    rdata = pca.fit_transform([[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]])
    np.random
    print(rdata)

if __name__ == "__main__":
    main()