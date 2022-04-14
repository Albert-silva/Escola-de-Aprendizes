from flask import Flask
from modules.auth.rotas import auth_rotas

app = Flask(__name__)

app.register_blueprint(auth_rotas)

app.run("localhost", 5000)