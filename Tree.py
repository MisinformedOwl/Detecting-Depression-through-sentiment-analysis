#%%
from nltk import tokenize
import nltk
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd
import string
import random
import pickle
from sklearn import svm

#%%
def export(vec, svc):
    out = open("vec.pickle", "wb")
    pickle.dump(vec, out)
    out.close()
    out = open("svc.pickle", "wb")
    pickle.dump(svc, out)
    out.close()

#%%
def processText(data):
    print()
    rows = []
    for index, row in data.iterrows():
        row = row[0].lower()
        row = row.replace("#depressed", "")
        row = row.replace("#happy", "")
        rows.append(row)
        #print(row)
    return rows, data['Depressed']

#%%
def preprocess(Data, vec):
    # Tokenize data
    featuress = []
    dataRows, labels = processText(Data)
    tokens = vec.fit_transform(dataRows)
    
    return tokens, labels

##############################################################################
#%%

fileData = pd.read_excel("data/data.xlsx")
training = []
testing = []
stopwords = set(stopwords.words('english'))
vec = CountVectorizer(lowercase= True, analyzer='word')

treeClassifier = tree.DecisionTreeClassifier()

size = len(fileData)
size = round((size/100)*80)

fileData = fileData.sample(frac=1)
Text = fileData[:]

training, trainingLabels = preprocess(Text, vec)

print(f"Training size: {training.shape[0]}")
print(f"Labels size: {len(trainingLabels)}")

train_x, test_x, train_y, test_y = train_test_split(training, trainingLabels)

svc = treeClassifier.fit(train_x, train_y)
svc._prune_tree()

print()
yes = 0
index = 0
for y in test_y:
    res = int(svc.predict(test_x[index]))
    print(res, y, index)
    if res == y:
        yes = yes + 1
    index = index +1

export(vec,svc)
    
print(f"Accuracy is: {yes/test_x.shape[0]*100}%")