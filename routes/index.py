from app import app
from flask import make_response

@app.route('/')
def home():
  return make_response({ "message": "hiwder api ngub" }, 200)