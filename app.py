from flask import Flask, request, make_response

app = Flask(__name__)

from routes import index, route

if __name__ == "__main__":
    app.run(debug=True)