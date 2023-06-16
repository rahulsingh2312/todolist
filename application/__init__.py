from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)
app.config["SECRET_KEY"]="hiimasectretkey"
app.config["MONGO_URI"] ="mongodb+srv://rahulol:rw7vApAxCFw6LXMn@todolist.hxpy9gt.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient('mongodb+srv://rahulol:rw7vApAxCFw6LXMn@todolist.hxpy9gt.mongodb.net/?retryWrites=true&w=majority')

# setup mongo
mongodb_client = PyMongo(app)
db = client['db']
collection = db['todo_flask']


from application import routes


