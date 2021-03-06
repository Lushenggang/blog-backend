from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
from .socket import socketio

mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
  app = Flask(config_name)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  mail.init_app(app)
  db.init_app(app)
  socketio.init_app(app)
  from .api import api as api_blueprint
  app.register_blueprint(api_blueprint, url_prefix='/api')

  return app