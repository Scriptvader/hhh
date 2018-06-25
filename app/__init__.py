import os
from flask import Flask

# Initialize application
app = Flask(__name__, static_folder=None)

# Import the application views
from app import views
