# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    request,
    jsonify,
    render_template, json
)

import csv

from middleware import model_predict
import middleware

router = Blueprint('app_name',
                   __name__,
                   template_folder='templates')


@router.route('/', methods=['GET', 'POST'])
def index():
    """
    Esta función renderiza un frontend donde podemos ingresar
    sentencias y obtener una prediccion de su sentimiento.
    """
    context = {
        'text': None,
        'prediction': None,
        'score': None,
        'success': False
    }
    # Obtiene la sentencia ingresada por el usuario en el frontend
    text_data = request.form.get('text_data')

    prediction = None
    score = None

    if text_data:
        #################################################################
        # COMPLETAR AQUI: Envie el texto ingresado para ser procesado
        # por nuestra función middleware.model_predict.
        # Luego con los resultados obtenidos, complete el diccionario
        # "context" para mostrar la predicción en el frontend.
        #################################################################
        #raise NotImplementedError
        
        prediction, score = middleware.model_predict(text_data)
        #################################################################

    return render_template('index.html', context={
        'text': text_data,
        'prediction': prediction,
        'score': score,        
    })


@router.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """
    [Práctico 2 - No completar]
    Esta función nos permitirá darle feedback a nuestra API
    para los casos en los que clasificamos una oración
    con un sentimiento erroneo.
    """

    text_data = request.form.get('report')

    with open('./feedback/feedback.csv', mode='a') as feedback_file:

        feedback_writer = csv.writer(feedback_file, 
                                    delimiter=',',
                                    quotechar='"', 
                                    quoting=csv.QUOTE_MINIMAL)

        feedback_writer.writerow([text_data])


    context = {
        'text': "Feedback registrado",
        'prediction': "",
        'score': "0",
        'success': True
    }

    print(context)

    return render_template('index.html', context=context)


@router.route('/predict', methods=['POST'])
def predict():
    """
    Método POST que permite obtener predicciones de analisis de
    sentimiento a partir de oraciones.
    """
    # Respuesta inicial
    rpse = {
        'success': False,
        'prediction': 'None',
        'score': None
    }

    # Nos aseguramos que el método sea correcto y tengamos datos
    # para procesar
    if request.method == 'POST':
        try:
            if request.args.get('text'):
                #################################################################
                # COMPLETAR AQUI: Extraiga la sentencia a procesar y utilice la
                # función middleware.model_predict para obtener el sentimiento
                # de la misma. Complete los campos de "rpse" con los valores
                # obtenidos.
                #################################################################
                #raise NotImplementedError
                text_data = request.args.get('text')
                #################################################################

                prediction = None
                score = None

                if text_data:
                    prediction,score = model_predict(text_data)
                
                    rpse = {
                    'success': True,
                    'prediction':prediction,
                    'score': score
                    }   
                
                return jsonify(rpse)

        except Exception as e:
            print({
                'Error': str(e),
                'Desde': "request.args.get(text)"
            })


    else:
        print({
            'request_status': 400,
            'request_message': 'Bad Request'
        })

    return jsonify(rpse), 400


@router.route('/prediction', methods=['POST'])
def prediction():
    """
    Método POST que permite obtener predicciones de analisis de
    sentimiento a partir de oraciones.
    """
    # Respuesta inicial
    rpse = {
        'success': False,
        'prediction': 'None',
        'score': None
    }

    # Nos aseguramos que el método sea correcto y tengamos datos
    # para procesar
    if request.method == 'POST':
        
        try:

            obj = request.get_json()
            # print(obj)
            
            text_data= obj['text']

            prediction = None
            score = None

            if text_data:
                prediction,score = model_predict(text_data)
            
                rpse = {
                'success': True,
                'prediction':prediction,
                'score': score
                }   
            
            else:
                print({'Error': "sin text_data"})

            return jsonify(rpse)

        
        except Exception as e:
            print({
                'Error': str(e),
                'Desde': "request.args.get(text)"
            })


    else:
        #print('no entro al if de post')
        #print(request.args.get('text'))
        pass

    return jsonify(rpse), 400


@router.route('/prediction_auth', methods=['POST'])
def prediction_auth():
    """
    Método POST que permite obtener predicciones de analisis de
    sentimiento a partir de oraciones.
    """
    # Respuesta inicial
    rpse = {
        "success": False,
        "login": "Error",
    }

    # Nos aseguramos que el método sea correcto y tengamos datos
    # para procesar
    if request.method == 'POST':
        
        try:

            obj = request.get_json()
            # print(obj)
            
            usuario = obj['user']

            if usuario is not None and usuario == 'usuario':
                
                rpse = {
                    "success": True,
                    "login": "OK",
                }

                print(json.dumps(rpse))
                print(json.dumps({
                    "request_status": 200,
                    "request_message": "Success"
                }))
                return jsonify(rpse), 200

            else:
                print(json.dumps({
                    "request_status": 401,
                    "request_message": "Unauthorized"
                }))                
                return jsonify(rpse), 401
        
            
        except Exception as e:
            print({
                'Error': str(e),
                'Desde': "request.get_json()"
            })
        
    print(json.dumps({
        "request_status": 400,
        "request_message": "Bad Request"
    }))

    return jsonify(rpse), 400
