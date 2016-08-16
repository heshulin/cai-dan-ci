from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['Access-Control-Allow-Origin'] = 'http://183.175.12.157/'
