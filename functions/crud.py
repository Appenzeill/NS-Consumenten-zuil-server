from flask import Flask, jsonify, request
from functions.insert_data import insert_review

def crud(reviewList):
    app = Flask(__name__)
    @app.route('/review', methods=['POST']) 
    def insert_reviews():
        get_consent = request.form['consent']
        get_review = request.form['review']
        get_name = request.form['name']
        if get_consent == "True":
            consent = True
        else:
            consent = False
            
        data = ["reviews",get_name, get_review, consent]
        
        #data = [request.form['name'],request.form['review']]
        #print(jsonify(data))
        #print(data)
        #insert_review(postList)
        #print("succes {}".format(data))
        #return jsonify(data)
        insert_review(data)
        return(jsonify(data))
    app.run()
