# -*- coding: utf-8 -*-
import json
import redis
import time
from classifier import SentimentClassifier

########################################################################
# COMPLETAR AQUI: Crear conexion a redis y asignarla a la variable "db".
########################################################################
db = redis.Redis(host='redis', port=6379, db=0)
########################################################################

########################################################################
# COMPLETAR AQUI: Instanciar modelo de análisis de sentimientos.
# Use classifier.SentimentClassifier de la libreria
# spanish_sentiment_analysis ya instalada
########################################################################
model = SentimentClassifier()
########################################################################


def sentiment_from_score(score):
    """
    Esta función recibe como entrada el score de positividad
    de nuestra sentencia y dependiendo su valor devuelve uno
    de las siguientes clases:
        - "Positivo": Cuando el score es mayor a 0.55.
        - "Neutral": Cuando el score se encuentra entre 0.45 y 0.55.
        - "Negativo": Cuando el score es menor a 0.45.

    Attributes
    ----------
    score : float
        Porcentaje de positividad.

    Returns
    -------
    sentiment : str
        Una de las siguientes etiquetas: "Negativo", "Neutral" o "Positivo".
    """
    ####################################################################
    # COMPLETAR AQUI
    ####################################################################
    #print(round(score, 4))
    if score < .45:
        sentiment = "Negativo"
    if score > .55:
        sentiment = "Positivo"
    if score > 0.45 and score < 0.55:
        sentiment = "Neutral"

    #sentiment = None
    #raise NotImplementedError
    ####################################################################

    return sentiment


def predict(text):
    """
    Esta función recibe como entrada una oración y devuelve una
    predicción de su sentimiento acompañado del score de positividad.

    Attributes
    ----------
    text : str
        Sentencia para analizar

    Returns
    -------
    sentiment : str
        Una de las siguientes etiquetas: "Negativo", "Neutral" o "Positivo".
    score : float
        Porcentaje de positividad.
    """
    sentiment = None
    score = None

    ####################################################################
    # COMPLETAR AQUI: Utilice el clasificador instanciado previamente
    # ("model") para obtener el score de positividad.
    # Luego utilice la función "sentiment_from_score" de este módulo
    # para obtener el sentimiento ("sentiment") a partir del score.
    ####################################################################
    #raise NotImplementedError
    ####################################################################
    score = model.predict(text)
    sentiment = sentiment_from_score(score)
    
    return sentiment, score


def classify_process():
    """
    Obtiene trabajos encolados por el cliente desde Redis. Los procesa
    y devuelve resultados.
    Toda la comunicación se realiza a travez de Redis, por ello esta
    función no posee atributos de entrada ni salida.
    """
    # Iteramos intentando obtener trabajos para procesar
    while True:
        ##################################################################
        # COMPLETAR AQUI: Obtenga un batch de trabajos encolados, use
        # lrange de Redis. Almacene los trabajos en la variable "queue".
        ##################################################################
        queue = db.lrange('service_queue', 0, 9)
        ##################################################################

        # Iteramos por cada trabajo obtenido
        for q in queue:
            ##############################################################
            # COMPLETAR AQUI:
            #     - Utilice nuestra función "predict" para procesar la
            #       sentencia enviada en el trabajo.
            #     - Cree un diccionario con dos entradas: "prediction" y
            #       "score" donde almacenara los resultados obtenidos.
            #     - Utilice la funcion "set" de Redis para enviar la
            #       respuesta. Recuerde usar como "key" el "job_id".
            #
            ##############################################################
            #raise NotImplementedError
            ##############################################################
            # q = "{'text': 'hoy es un lindo dia', 'id': '2342342342'}"

            #processing
            q = json.loads(q.decode('utf-8'))
            job_id = q['id']
            
            sentiment, score = predict(q['text'])
            # output
            response = {'prediction':sentiment, 'score':score} 
            db.set(job_id, json.dumps(response))
        ##### #############################################################
        # COMPLETAR AQUI: Use ltrim de Redis para borrar los trabajos ya
        # procesados. Luego duerma durante unos milisengundos antes de
        # pedir por mas trabajos.
        ##################################################################
        #raise NotImplementedError
        ##################################################################

        db.ltrim('service_queue', len(queue), -1)
        time.sleep(2)

if __name__ == "__main__":
    print('Launching ML service...')
    classify_process()