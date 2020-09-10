from sklearn.feature_selection import VarianceThreshold

def main():
    vt = VarianceThreshold()
    rdata = vt.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(rdata)

if __name__ == "__main__":
    main()
