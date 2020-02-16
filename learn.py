import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from pathlib import Path
import string
import re
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDJxtj9236MbEc16B_D8zDpSIBxXAhmR54')

def locationRecommend(post):
    out = open('output.txt', 'w+')

    location = ['Belize', 'Paris', 'Berlin', 'Las Vegas', 'Istanbul', 'Bangkok', 'Venice', 'Amsterdam','Tokyo',
    'Seoul', 'Milan', 'Budapest', 'Taipei', 'Marrakesh', 'Prague', 'Honolulu', 'Cairo', 'Cape Town', 'London', 'Moscow']

    fileTxt = ['Belize.txt', 'Paris.txt', 'Berlin.txt', 'Las_Vegas.txt', 'Istanbul.txt', 'Bangkok.txt', 'Venice.txt', 'Amsterdam.txt',
    'Tokyo.txt','Seoul.txt','Milan.txt', 'Budapest.txt', 'Taipei.txt', 'Marrakesh.txt', 'Prague.txt', 'Honolulu.txt', 'Cairo.txt', 'Cape_Town.txt', 'London.txt', 'Moscow.txt']

    out.write('class,text\n')
    count  = 0
    for text in fileTxt:
        with open('./' + text, 'r', encoding="utf8") as myfile:
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

    
    predict = [post]
    predict_vec = vec.transform(predict)
    res = clf.predict(predict_vec)
    print(predict[0], '=>', res[0])
    
    print (predict_vec)
    return (res[0])

def latLong(place):
    #given a place - find the location(lat and long) and place_id
    map_result = gmaps.find_place(place, 'textquery',
                                    fields=['geometry/location', 'place_id'],
                                    location_bias='point:10,10', language = 'en-AU')
    latitude  = map_result.get('candidates')[0].get('geometry').get('location').get('lat')
    longitude  = map_result.get('candidates')[0].get('geometry').get('location').get('lng')
    print (latitude, longitude)
    return [latitude, longitude]

def nearPlace(lat, long, key):
    
    near = gmaps.places_nearby([lat, long],keyword=key,
                                  language = 'en-AU',
                                  radius = 30)
    list = ""
    arr = []
    for i in range(0,3):
        if (len(near.get('results')) > i):
            #nameRating = [near.get('results')[i].get('name')] 
            #nameRating.append(near.get('results')[i].get('rating'))
            #nameRating.append(near.get('results')[i].get('geometry').get('location').get("lat"))
            #nameRating.append(near.get('results')[i].get('geometry').get('location').get("lng"))
            #arr.append([nameRating])


            stringLat = str(near.get('results')[i].get('geometry').get('location').get("lat"))
            stringLong = str(near.get('results')[i].get('geometry').get('location').get("lng")) 
            stringRating =  str(near.get('results')[i].get('rating'))
            print(type(stringLat))
            print(type(stringLong))

            list = list+near.get('results')[i].get('name')+","+stringRating+","+stringLat+","+stringLong+'\n'
            
        
    
    #print(near)
    print('')
    return list

l = latLong('Fairfax City')
#places = nearPlace(l[0],l[1], 'tourism')
#print (places)
# locationRecommend("rework")
#type(places[0][0])