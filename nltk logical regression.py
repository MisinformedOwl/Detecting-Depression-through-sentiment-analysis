#%%
from nltk import tokenize
import nltk
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd
import string
import random

#%%
def preprocess(Data, vec):
    # Tokenize data
    featuress = []
    labels = []
    tokens = vec.fit_transform(Data.Phrases)
    for index, row in Data.iterrows():
        label = row['depressed']
        labels.append(label)
    return tokens, labels

##############################################################################
#%%

fileData = pd.read_excel("data/data.xlsx")
training = []
testing = []
stopwords = set(stopwords.words('english'))
vec = CountVectorizer(lowercase= True, analyzer='word')

lr = LogisticRegression()

size = len(fileData)
size = round((size/100)*80)

fileData = fileData.sample(frac=1)
Text = fileData[:]

training, trainingLabels = preprocess(Text, vec)

train_x, test_x, train_y, test_y = train_test_split(training, trainingLabels)

lr = lr.fit(train_x, train_y)
    
print()
yes = 0
for test in range(test_x.shape[0]):
    res = int(lr.predict(test_x[test]))
    print(res, test_y[test], test)
    if res == test_y[test]:
        yes = yes + 1
    
print(f"Accuracy is: {yes/test_x.shape[0]*100}%")