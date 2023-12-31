import os, json

from flask import Flask
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi
from werkzeug.middleware.proxy_fix import ProxyFix

from .routes import rest_api

app = Flask(__name__) # app instantiation
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('api.config.BaseConfig') # app settings
rest_api.init_app(app) # instantiating flask restx


@app.after_request
def after_request(response):
    ''' Sends back a custom error with {"success", "msg"} format '''
       
    if int(response.status_code) >= 400:
        response_data = json.loads(response.get_data())
        if "errors" in response_data:
            response_data = {"success": False,
                             "msg": list(response_data["errors"].items())[0][1]}
            response.set_data(json.dumps(response_data))
        response.headers.add('Content-Type', 'application/json')
    return response

# @app.errorhandler(500)
# def error500():
#     pass

# converting our WSGI App to ASGI
asgi_app = WsgiToAsgi(app)