from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from clasePersona import clasePersona
import json

personas = []
app = Flask(__name__)


#datos totales
@app.route('/')
def rutainicial():
     return render_template('PruebaCS.html')
   
if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)