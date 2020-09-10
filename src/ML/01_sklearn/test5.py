from sklearn.preprocessing import MinMaxScaler


def main():
    mm = MinMaxScaler(feature_range=(0,1))
    rdata = mm.fit_transform(
        [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(mm.feature_range)
    print(rdata)


if __name__ == "__main__":
    main()
