import flask
from flask import Flask, jsonify, send_from_directory, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
