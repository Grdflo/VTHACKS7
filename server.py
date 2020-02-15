#!/usr/bin/python
import json
from flask import Flask, request, abort, jsonify, render_template
app = Flask(__name__, static_url_path='', static_folder="static")

#parseInputs
pIs = [];
cordX = 0;
cordY = 0;
cords = [];



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

@app.route('/pushLoading/', methods=['POST'])
def push_loading():
    #TODO: return only when done loading help
    #PROCESS DATA HERE:--------------------------
    #pIs[0][1]

    print(pIs);




    #Update the coordiantes here
    global cords;
    cords = [];
    cords.append(1);
    cords.append(2);
    #PROCESS DATA HERE:--------------------------
    return jsonify({"status": "ok"}), 200

@app.route('/pushMain/', methods=['POST'])
def handle_push():
    #Parse data
    try:
        #Try parsing data
        data = json.loads(request.data);
        row = (data['twitter'], data['instagram'], data['facebook']);

        #TODO: remove print
        print(row)
    except (ValueError, KeyError, TypeError) as e:
        return e

    #TODO
    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#
    pIs.append(row);

    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#

    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    print("Listening...")
    app.run(debug=True, host='localhost', port=8081)


