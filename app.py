#!/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Por favor, use algun dos endpoints: /write ou /get"

@app.route('/write')
def write():
    return jsonify({"version": "v1"})

@app.route('/get')
def get():
    return jsonify({"version": "v1"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')