from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return {"message":"hello there this is sol \n testing the first flask app"}