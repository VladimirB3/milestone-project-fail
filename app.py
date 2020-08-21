import pymongo
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://puika:Meta7gear@myfirstcluster.lzacf.mongodb.net/videogames?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_games')
def get_tasks():
    return render_template("games.html", games=mongo.db.games.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
