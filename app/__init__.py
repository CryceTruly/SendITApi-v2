from project.views.parcels import ap
from project.auth.views import auth
from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

app.register_blueprint(ap)
app.register_blueprint(auth)
