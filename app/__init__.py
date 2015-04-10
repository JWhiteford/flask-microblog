from flask import Flask

# Second import is after to avoid circular dependancy
app = Flask(__name__)
app.config.from_object('config') # Use the config file

from app import views
