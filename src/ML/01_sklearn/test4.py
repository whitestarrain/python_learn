from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

def main():
    str1 = "1、今天很残酷，明天更残酷，后天很美好， 但绝对大部分是死在明天晚上，所以每个人不要放弃今天。"
    str2 = "2、我们看到的从很远星系来的光是在几百万年之前发出的， 这样当我们看到宇宙时，我们是在看它的过去。"
    str3 = "3、如果只用一种方式了解某样事物，你就不会真正了解它。 了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"
    str1_cut = jieba.cut(str1)
    str2_cut = jieba.cut(str2)
    str3_cut = jieba.cut(str3)
    str1_s = " ".join(str1_cut)
    str2_s = " ".join(str2_cut)
    str3_s = " ".join(str3_cut)
    tifid = TfidfVectorizer()
    rdata = tifid.fit_transform([str1_s, str2_s, str3_s])
    print(tifid.get_feature_names())
    print(rdata.toarray())
    print(rdata)

if __name__ == "__main__":
    main()
