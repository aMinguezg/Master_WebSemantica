import sklearn
import json

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()
features = []
categories = []
alcoholic = []
adiction = []
stopgaming = []
stopsmoking = []

with open('positivos.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')       
        features.append(texto)

with open('reddit.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')       
        features.append(texto)     

for i in range(0,30):
    categories.append("Depress")

for x in range(0,100):
    categories.append("NoDepress")


X_train_counts = count_vect.fit_transform(features)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


clf = MultinomialNB().fit(X_train_tfidf, categories)

with open('alcoholism.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')       
        alcoholic.append(texto)



X_new_counts = count_vect.transform(alcoholic)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

print("PREDICTION DE ALCOHOL")
print(predicted)
print(" ")

with open('adiction.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')       
        adiction.append(texto)



X_new_counts = count_vect.transform(adiction)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

print("PREDICTION DE ADICTION")
print(predicted)
print(" ")

with open('stopsmoking.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')       
        stopsmoking.append(texto)



X_new_counts = count_vect.transform(stopsmoking)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

print("PREDICTION DE STOP SMOKING")
print(predicted)
print(" ")


with open('stopgaming.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')       
        stopgaming.append(texto)



X_new_counts = count_vect.transform(stopgaming)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

print("PREDICTION DE STOP GAMING")
print(predicted)
print(" ")