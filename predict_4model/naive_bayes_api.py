from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pickle

def naive_bayes_api(tweet):
    with open('naive_bayes.model', 'rb') as f:
        mod = pickle.load(f)
        dtmvector = pickle.load(f)
        
    tfidf_transformer = TfidfTransformer()

    Xtest2 = dtmvector.transform([tweet])
    tfidfv_t2 = tfidf_transformer.fit_transform(Xtest2)

    return mod.predict(tfidfv_t2)[0]

def call_api(tweet):
    val_predict = naive_bayes_api(tweet)
    ret = ""
    if val_predict == 1:
        ret = "기쁨"
    elif val_predict == 2:
        ret = "슬픔"
    elif val_predict == 3:
        ret = "화남"
    elif val_predict == 5:
        ret = "중립"
    else:
        ret = str(val_predict[0]) + "잘못된 분류값입니다."
    return ret
