import os
from flask import Flask
from flask-pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Videogames...'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)