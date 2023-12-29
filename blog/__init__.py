from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blog import routes
import base64

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy()
db.init_app(app)


def b64encode_binary(data):
    return base64.b64encode(data).decode('utf-8') if data else None


app.jinja_env.filters['b64encode'] = b64encode_binary
