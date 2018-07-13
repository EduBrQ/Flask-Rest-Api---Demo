import logging.config
import os
from flask import Flask, Blueprint
from rest_api_demo import settings
from rest_api_demo.api.restplus import api
from rest_api_demo.database import db
import numpy as np
from flask import Flask, abort, jsonify, request
import pickle as pickle
import numpy as np
import base64
from flask_restplus import Api, Resource, fields
from flask import Flask, request, render_template, make_response
from sklearn.externals import joblib
from io import BytesIO
from skimage import io as skio
from skimage.transform import resize
from flask import Flask, render_template
import requests
import json
import sys
from flask_restplus import Api, Resource, fields
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, SwaggerView, Schema, fields
from flasgger.utils import swag_from
from flask import render_template
from flask_bootstrap import Bootstrap 

app = Flask(__name__)
Bootstrap(app)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

db = SQLAlchemy(app)

api = Api(app, version='1.0', title='Nutes Analytics - API',
    description='A API to serve machine learning models to predict obesity and others diseases'
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


##############################################
###-CARREGO MEUS MODELOS DE APRENDIZAGEM-#####
##############################################
my_knn = pickle.load(open('PRESSAO/analytics_folder/knn.pkl', 'rb'))

diabetes_model = pickle.load(open('DIABETES/analytics_folder/diabetes.pkl', 'rb')) 
##############################################


##############################################
################ -API HOME - #################
##############################################
@app.route('/home')

def home():
	return render_template('home.html')

###############################################

# ROTA (POST) QUE RECEBE OS ATRIBUTOS ESPERADOS DO MODELO DE APRENDIZAGEM DEFINIDO E RETORNA A PREDIÇÃO FEITA POR ELE
@app.route('/pressao', methods=['POST'])

def make_predict(): #10.0.0.102
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            predict_request = [data['Batimentos'], data['Calorias']]
            
        except ValueError:
            return jsonify("Por favor, coloque um valor para batimentos e calorias: ")
        
    predict_request = np.array(predict_request)
    predict_request = predict_request.reshape(1,-1)

    y_hat = my_knn.predict(predict_request) #retorna o resulta em JSON

    output = [y_hat[0]]
    
    #return jsonify(my_knn.predict(predict_request).tolist()) #Transforma o resultado JSON em uma lista
                   
    def result(m):
        if m[0] == 0:
            return "Sua Pressao esta normal"
        
        elif m[0] == 1:
            return "Sua Pressao esta muito Baixa"
        
        elif m[0] == 2:
            return "Sua Pressao esta muito Alta"
   
    output = result(output)
    return jsonify(results=output)
###############################################


# ROTA (POST) QUE RECEBE OS ATRIBUTOS ESPERADOS DO MODELO DE APRENDIZAGEM DEFINIDO E RETORNA A PREDIÇÃO FEITA POR ELE
@app.route('/diabetes', methods=['POST'])

def make_predict2(): #10.0.0.102
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            #predict_request = [data['Pregnancies'], data['Glucose'], data['BloodPressure'], data['SkinThickness'], data['Insulin'], data['BMI'], data['DiabetesPedigreeFunction'], data['Age']]
            predict_request = [data['Glucose'], data['BloodPressure'], data['Insulin'], data['BMI'], data['Age']]
            
        except ValueError:
            return jsonify("Valores inadequados! ")
        
    predict_request = np.array(predict_request)
    predict_request = predict_request.reshape(1,-1)

    y_hat2 = diabetes_model.predict(predict_request) #retorna o resulta em JSON

    output2 = [y_hat2[0]]
    
    #return jsonify(my_knn.predict(predict_request).tolist()) #Transforma o resultado JSON em uma lista
                   
    def result(m):
        if m[0] == 0:
            return "Sem Diabetes"
        
        elif m[0] == 1:
            return "Diabetes"
      
   
    output2 = result(output2)
    return jsonify(results=output2)
#######################################################################


###############################################
################# -HANIOT DATA- ###############
###############################################

# A route to return all of the available entries in our catalog.
@app.route('/hanUser', methods=['GET'])
def api_all():
    params = {
    'api_key': '{eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1YWNjYjZkYTM3MzNjZDAwMTQ5MTZjNTAifQ.1gJH3Y0u9vmXcYQsMx-OmqqFL2rQfTZlYF9L4r9bXO0}',
  }
    r = requests.get('https://haniot-api.herokuapp.com/api/v1/measurements/types/3?period=3w', headers={'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1YWNjYjZkYTM3MzNjZDAwMTQ5MTZjNTAifQ.1gJH3Y0u9vmXcYQsMx-OmqqFL2rQfTZlYF9L4r9bXO0'})
    #r = get_json(r.text)
    r = r.text

    return r
############################################################

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    #api.add_namespace(blog_posts_namespace)
    #api.add_namespace(blog_categories_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)
	
############################################################
############################################################
############################################################
############################################################


def main():
    initialize_app(app)
    log.info('>>>>> INICIANDO O SERVIDOR EM -> http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()


# PARA TORNAR ESSE SERVIDOR PÚBLICO #
#if __name__ == '__main__':
#    app.run(host= '0.0.0.0', port=33)