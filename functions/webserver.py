from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from functions.retrieve_data import retrieve_reviews, retrieve_new_reviews, retrieve_user_data
from functions.insert_data import insert_user, update_user, update_review, insert_review

def webserver():
    app = Flask(__name__)
    auth = HTTPBasicAuth()
    role = 0
    user_id = 0
    
    @app.route('/list')
    @auth.login_required
    def server_return_list():
        return jsonify(retrieve_reviews())

    @app.route('/review', methods=['POST']) 
    @auth.login_required
    def server_insert_reviews():
        get_consent = request.form['consent']
        get_review = request.form['review']
        get_name = request.form['name']
        if get_consent == "True":
            consent = True
        else:
            consent = False
            
        data = ["reviews",get_name, get_review, consent]
        
        insert_review(data)
        return(jsonify(data))
    
    @app.route('/update', methods=['POST'])
    @auth.login_required
    def server_update_review():
        if role == 1 or 2:
            get_id = int(request.form['user_id'])
            get_approval = bool(request.form['approval'])
            comment = request.form['comment']
            
            listje = [get_id, get_approval, user_id,comment]
            print(listje)
            return jsonify(listje)

    @app.route('/users/insert', methods=['POST']) 
    @auth.login_required
    def server_insert_user():
        if role == 1 or 2:
            get_role_id = int(request.form['role_id'])
            get_user_email = request.form['email']
            get_user_password = request.form['password']
            
            user_hash = generate_password_hash(get_user_password)
    
            data = [get_user_email, get_role_id,user_hash]
        
            insert_user(data)
            return(jsonify(data))

    @app.route('/users/update', methods=['POST'])
    @auth.login_required
    def server_update_user():
        if role == 1 or 2:
            get_user_id = int(request.form['user_id'])
            get_role_id = int(request.form['role_id'])
            get_user_email = request.form['email']
            get_user_password = request.form['password']
            
            user_hash = generate_password_hash(get_user_password)
    
            data = [get_user_email, get_role_id,user_hash]
        
            update_user(data)
            return(jsonify(data))


    @auth.verify_password
    def server_authenticate(username,password):
        if username and password:
            userData = []
            userData = retrieve_user_data(username)
            if userData:
                if check_password_hash(userData[2],password) == True:
                    user_id = userData[0]
                    role = userData[3]
                    
                    return True
                else:
                    return False
                return False

    
    app.run()
