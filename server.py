#!/usr/bin/python
import json
from flask import Flask, request, abort, jsonify, render_template
app = Flask(__name__, static_url_path='', static_folder="static")
from scraper import getSocialMediaText
from learn import locationRecommend, latLong

#parseInputs
cordX = 0
cordY = 0
cords = []
location = ''
website = {'facebook': '' ,'instagram': '', 'twitter': ''}
restuarants = ''
attractions = ''



#Preroute definitions
@app.route('/')
def push_index():
    return render_template('index.html')

@app.route('/loading/')
def push_loading_screen():
    return render_template('loading.html')

@app.route('/results/')
def push_results():
    return render_template('results.html')

@app.route('/curCords', methods=['POST'])
def getCoords():
    global cords;
    return {"X" : cords[0], "Y" : cords[1]}, 200;

@app.route('/curLoc', methods=['POST'])
def getLocations():
    global location;
    return {"location": location};
    

@app.route('/pushLoading/', methods=['POST'])
def push_loading():
    global location
    global website
    #TODO: return only when done loading help
    #PROCESS DATA HERE:-------------------------
    bigPost =  getSocialMediaText(website) #put in websites as a dictionary to handle
    location = locationRecommend(bigPost)

    #Update the coordiantes here
    global cords;
    cords = latLong(location)


    #PROCESS DATA HERE:--------------------------
    return jsonify({"status": "ok"}), 200

@app.route('/pushRestaurants/', methods=['POST'])
def push_restaurants():
    global restaurants

    restaurants = nearPlace(cords[0], cords[1], 'food')
    return jsonify({"status": "ok"}), 200

@app.route('/pushAttractions/', methods=['POST'])
def push_attractions():
    global attractions

    attractions = nearPlace(cords[0], cords[1], 'tourism')
    return jsonify({"status": "ok"}), 200

@app.route('/curRestaurants', methods=['POST'])
def getRestuarants():
    global restaurants
    return {"rest", restaurants}

@app.route('/curAttractions', methods=['POST'])
def getAttractions():
    global attractions
    return {"att", attractions}

@app.route('/pushMain/', methods=['POST'])
def handle_push():
    #Parse data
    try:
        #Try parsing data
        data = json.loads(request.data);
        website['twitter'] = data['twitter']
        website['instagram'] = data['instagram']
        website['facebook'] = data['facebook']
    except (ValueError, KeyError, TypeError) as e:
        return e

    #TODO
    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#
 

    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#

    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    print("Listening...")
    app.run(debug=True, host='localhost', port=8081)


