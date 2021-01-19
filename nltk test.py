from nltk import tokenize, ngrams, NaiveBayesClassifier
import nltk
from nltk.corpus import stopwords
import pandas as pd
import string
import random

def preprocess(Data):
    # Tokenize data
    featuress = []
    for index, row in Data.iterrows():
        tokens = tokenize.word_tokenize(row['Phrases'].lower().strip())
        label = row['Depressed']
        features = {}
        featurelist = ()
        for token in tokens:
            if token not in string.punctuation:
                if token not in features.keys():
                    features.update({token : 1})
                else:
                    features.update({token : (features.get(token)+1)})
                    
        if label == 1:
            featuress.append((features, "depressed"))
        else:
            featuress.append((features, "normal"))
    
    featurelist = featuress
    return featurelist

##############################################################################

def testprocess(sentence):
    tokens = tokenize.word_tokenize(sentence.lower().strip())
    features = {}
    for token in tokens:
        if token not in string.punctuation:
            if token not in features.keys():
                features.update({token : 1})
            features.update({token : (features.get(token)+1)})
    return features
        

##############################################################################

def test(data, normalText):
    count = 0
    text = []
    for x, y in normalText.iterrows():
        text.append(y['Phrases'])
    for T,L in data:
        count += 1

##############################################################################

fileData = pd.read_excel("data/data.xlsx")
training = []
testing = []
stopwords = set(stopwords.words('english'))

size = len(fileData)
size = round((size/100)*80)

fileData = fileData.sample(frac=1)
trainingText = fileData[:size]
testingText = fileData[size:]

print("training")
print(trainingText)
print("testing")
print(testingText)

training = preprocess(trainingText)
testing = preprocess(testingText)

nb = NaiveBayesClassifier.train(training)

    
print()
print(f"Naive bayes accuracy: %{(nltk.classify.accuracy(nb, testing))*100}")
print(nb.most_informative_features(5))

print()
test(testing, testingText)