import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)