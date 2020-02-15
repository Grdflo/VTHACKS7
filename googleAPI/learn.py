import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from pathlib import Path
import string
import re








out = open('output.txt', 'w+')

location = ['Belize', 'Paris', 'Hong Kong', 'Las Vegas', 'Istanbul', 'Bangkok', 'Venice', 'Amsterdam','Tokyo',
'Seoul']#, 'Milan', 'Budapest', 'Taipei', 'Marrakesh', 'Prague', 'Honolulu', 'Cairo', 'Cape Town', 'London', 'Moscow']

fileTxt = ['Belize.txt', 'Paris.txt', 'Berlin.txt', 'Las_Vegas.txt', 'Istanbul.txt', 'Bangkok.txt', 'Venice.txt', 'Amsterdam.txt',
'Tokyo.txt','Seoul.txt'] 
#,'Milan.txt', 'Budapest.txt', 'Taipei.txt', 'Marrakesh.txt', 'Prague.txt', 'Honolulu.txt', 'Cairo.txt', 'Cape_Town.txt', 'London.txt', 'Moscow.txt']

out.write('class,text\n')
count  = 0
for text in fileTxt:
    with open(text, 'r') as myfile:
        #array of all lines in an array
        lines = myfile.readlines()
    
    for line in lines:
        #regex to strip a string of punctuation
        if (line == '\n'):
            continue
        lineNoPunct = re.sub('[^A-Za-z0-9]+', ' ', line)
        output_str = location[count] +',               '+ lineNoPunct +'\n'
        out.write(output_str)

    count+=1

out.close()



data = pd.read_csv('output.txt')
print(data)

# create the vector space model
vec = TfidfVectorizer(stop_words='english')

# 'transform' the words into vectors
x = vec.fit_transform(data['text'])
y = data['class']
print(y)

# create the naive bayes classifier
clf = MultinomialNB().fit(x, y)

# let's try to predict some sentences:
predict = ['thisfan tastic', 'this movie sucks please just be different', 'the police negotiator is the person with the entirely unenviable job of going into ground zero and attempting to talk a dangerous criminal out of doing whatever he or she intends to do    lives are often at stake   and the criminal is usually armed and most likely mentally unstable']
predict_vec = vec.transform(predict) # transform our prediction into a vector
res = clf.predict(predict_vec)

# print out predictions
#for k, v in zip(predict, res):
#    print(k, '=>', v)

while True:
    predict = [input()]
    predict_vec = vec.transform(predict)
    res = clf.predict(predict_vec)
    print(predict[0], '=>', res[0])
    print (predict_vec)


