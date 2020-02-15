#!/usr/bin/python
import json
from flask import Flask, request, abort, jsonify, render_template
app = Flask(__name__, static_url_path='', static_folder="static")


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

@app.route('/pushLoading/', methods=['POST'])
def push_loading():
    #TODO: return only when done loading help
    #PROCESS DATA HERE:--------------------------

    #PROCESS DATA HERE:--------------------------
    print("printLoading recieved")
    return jsonify({"status": "ok"}), 200

@app.route('/pushMain/', methods=['POST'])
def handle_push():
    #Parse data
    try:
        #Try parsing data
        data = json.loads(request.data);
        row = (data['twitter'], data['instagram'], data['facebook']);
        my_query = query_db(row, (3,))
        json_output = json.dumps(my_query)

        #TODO: remove print
        print(row)
    except (ValueError, KeyError, TypeError) as e:
        return e

    #TODO
    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#

    #----------------Whoever should deal cache(Google postgresql), do it here-----------------#

    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    print("Listening...")
    app.run(debug=True, host='localhost', port=8081)

def db(database_name='data base'):
    return psycopg2.connect(database=database_name)

def query_db(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r
