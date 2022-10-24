from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

from routes import index, route, home, explore

if __name__ == "__main__":
    app.run()