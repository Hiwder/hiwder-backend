from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
  return make_response({ "message": "hiwder api ngub" }, 200)


if __name__ == "__main__":
    app.run(debug=True)