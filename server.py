#!/usr/bin/python
import json
from flask import Flask, request, abort, jsonify, render_template
app = Flask(__name__, static_url_path='')


#Preroute definitions
@app.route('/')
def push_index():
    return render_template('index.html');

@app.route('/loading')
def push_loading():
    return render_template('loading.html');

@app.route('/results', methods=['POST'])
def push_results():
    return render_template('results.html');

@app.route('/push', methods=['POST'])
def handle_push():
    #Parse data
    try:
        #Try parsing data
        data = json.loads(request.data);
        row = (data['twitter'], data['instagram'], data['facebook']);
        #TODO: remove print
        print(row)
    except (ValueError, KeyError, TypeError):
        return SomeErrorResponse

    #TODO
    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#

    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#


    return jsonify({"status": "ok"}), 200;

if __name__ == '__main__':
    print("Listening...")
    app.run(debug=True, host='localhost', port=8081)
