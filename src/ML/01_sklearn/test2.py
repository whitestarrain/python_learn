from sklearn.feature_extraction.text import CountVectorizer

def main():
    cv = CountVectorizer()
    rdata = cv.fit_transform(
        ["life is short,I use python", "life is too long,i don't use python"])
    print(rdata)
    print(cv.get_feature_names())
    print((rdata.toarray()))
    pass

if __name__ == "__main__":
    main()
