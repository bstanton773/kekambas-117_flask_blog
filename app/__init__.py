from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Create an instance of SQLAlchemy to connect our app to the database
db = SQLAlchemy(app)
# Create an instance of Migrate that will track our db and app
migrate = Migrate(app, db)

# Create an instance of the LoginManager which will handle all login related things
login = LoginManager(app)
# Set the login view
login.login_view = 'login'
# login.login_message = 'Hey I need to know who you are before you do that!'
login.login_message_category = 'warning'

# register the api blueprint with our app
from app.blueprints.api import api
app.register_blueprint(api)

# import all of the routes from the routes file and models from the models file into the current package
from app import routes, models
