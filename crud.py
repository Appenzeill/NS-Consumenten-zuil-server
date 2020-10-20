from flask import Flask, jsonify

def crud(reviewList):
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return jsonify(reviewList)
    app.run()
