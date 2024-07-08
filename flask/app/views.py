from flask import Flask
from app.views import *


app = flask(_name__)


#rutas
app.route('/', methods=['GET'])