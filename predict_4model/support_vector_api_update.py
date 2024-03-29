import pandas as pd
import numpy as np
import pickle
from sklearn.externals import joblib
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
""" SVM API """

def support_vector_api(tweet):
    with open('support_vector.model', 'rb') as f:
        text_clf_svm = pickle.load(f)
    return text_clf_svm.predict([tweet])[0]

def call_api(tweet):
    ret = ""
    val_predict = support_vector_api(tweet)
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

if __name__ == "__main__":
    pass