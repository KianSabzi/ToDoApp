from email.charset import Charset
from encodings import utf_8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from task_api import task_api_blueprint
from category_api import category_api_blueprint
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    SQLALCHEMY_DATABASE_URI='mysql://root:12345@localhost/flask_app',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    Charset = 'utf_8mb4'
))


models.init_app(app)
models.create_tables(app)

app.register_blueprint(task_api_blueprint)
app.register_blueprint(category_api_blueprint)


# @app.route('/', methods = ['GET'])
# def welcome():
#     return jsonify({'Welcome to this api': 'Version01'})


if __name__ == "__main__":
    app.run(debug=True)
