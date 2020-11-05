from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from functions.retrieve_data import retrieve_reviews, retrieve_unapproved_reviews, retrieve_review, retrieve_new_reviews, retrieve_user_data
from functions.insert_data import insert_user, update_user, update_review, insert_review
from functions.twitter import tweet

def webserver():
    app = Flask(__name__)
    auth = HTTPBasicAuth()
    role = 0
    user_id = 0

    # Test api to see if server works
    @app.route('/')
    #@auth.login_required
    def server_return_test():
        test_list = ["hello there","general kenobi"]
        test_list_2 = [["test1_0","test1_1"],["test2_0","test2_1","test2_2"]]
        return jsonify(test_list_2)

    # List with all reviews
    @app.route('/reviews/list')
    @auth.login_required
    def server_return_list():
        return jsonify(retrieve_reviews())

    # List with all upaproved reviews
    @app.route('/reviews/list/unapproved')
    @auth.login_required
    def server_return_unapproved_list():
        return jsonify(retrieve_unapproved_reviews())

    # Insert new review
    @app.route('/reviews/insert', methods=['POST']) 
    #@auth.login_required
    def server_insert_reviews():
        get_consent = request.form['consent']
        get_review = request.form['review']
        get_name = request.form['name']
        if get_consent == "True" or get_consent == "Ja" or get_consent == "ja":
            consent = True
        else:
            consent = False
            
        data = ["reviews",get_name, get_review, consent]
        
        insert_review(data)
        return(jsonify(data))

    # Update review as mod
    @app.route('/reviews/update', methods=['POST'])
    #@auth.login_required
    def server_update_review():
        if role == 1 or 2:
            get_id = int(request.form['user_id'])
            get_approval = int(request.form['approval'])
            comment = request.form['comment']
            
            if get_approval == 0:
                approval = True
                tweeted = True
                tweet(retrieve_review(get_id))
            else:
                approval = False
                tweeted = False
                
            
            listje = [user_id, comment, approval, tweeted, get_id]
            print(listje)
            update_review(listje)
            
            return jsonify(retrieve_review(get_id))

    # Insert new user with role
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

    # Update the user based on id.
    @app.route('/users/update', methods=['POST'])
    @auth.login_required
    def server_update_user():
        if role == 1 or 2:
            get_user_id = int(request.form['user_id'])
            get_role_id = int(request.form['role_id'])
            get_user_email = request.form['email']
            get_user_password = request.form['password']
            
            user_hash = generate_password_hash(get_user_password)
    
            data = [get_user_email, user_hash, get_role_id, get_user_id]
        
            update_user(data)
            return(jsonify(data))

    # Authenticate given email and password
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

    # Authentication for app
    @app.route('/auth')
    @auth.login_required
    def server_auth():
        if role == 1 or 2:
            return jsonify(True)

    app.run()
