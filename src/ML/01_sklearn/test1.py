from sklearn.feature_extraction import DictVectorizer


def main():
    dictVector = DictVectorizer(sparse=False)
    rdata=dictVector.fit_transform([
        {
            "name": 1,
            "value": "value1"
        },
        {
            "name": 2,
            "value": "value2"
        },
        {
            "name": 3,
            "value": "value3"
        }, ])
    print(dictVector.get_feature_names())
    print((rdata))
    print(type(rdata))


if __name__ == "__main__":
    main()
