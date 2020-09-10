from sklearn.preprocessing import StandardScaler

def main():
    stdv = StandardScaler()
    rdata = stdv.fit_transform( [[ 1., -1., 3.], [ 2., 4., 2.], [ 4., 6., -1.]])
    print(rdata)

if __name__ == "__main__":
    main()