#!/usr/bin/python
import json
from flask import Flask, request, abort, jsonify, render_template
app = Flask(__name__, static_url_path='')


@app.route('/')
def push_index():
    return render_template('index.html');

@app.route('/loading')
def push_loading():
    return render_template('loading.html');

@app.route('/results')
def push_results():
    return render_template('results.html');


@app.route('/push', methods=['POST'])
def handle_push():
    try:
        data = json.loads(request.data);
        row = (data['twitter'], data['instagram'], data['facebook']);
        print(row)
    except (ValueError, KeyError, TypeError):
        return SomeErrorResponse
    return jsonify({"status": "ok"}), 200;

if __name__ == '__main__':
    print("Listening...")
    app.run(debug=True, host='0.0.0.0', port=8085)
