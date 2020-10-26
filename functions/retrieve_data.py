from jproperties import Properties
import psycopg2
from psycopg2 import sql

# Config of reading properties from dbconfig.properties using psycopg2.
configs = Properties()
with open('./dbconfig.properties', 'rb') as config_file:
    configs.load(config_file)

# Database credentials are stored in dbconfig.properties with the file listed in .gitignore
credentials = [
    configs.get("db.database").data,
    configs.get("db.host").data,
    configs.get("db.username").data,
    configs.get("db.password").data,
]

# Connection with the database
connection = psycopg2.connect(
        database = credentials[0],
        host = credentials[1],
        user = credentials[2],
        password = credentials[3],
)

# Cursor for psycopg2
cursor = connection.cursor()
def retrieve_user():
    print("lmao")

    
def retrieve_reviews():
    retrieve_reviews_query = "select * from reviews"
    cursor.execute(retrieve_reviews_query)
    mobile_records = cursor.fetchall() 
    reviewList = []
    for row in mobile_records:
        time = "{}".format(row[5])
        user = " ".join(row[1].split())
        review = " ".join(row[2].split()) 
        appendList = [user,review,row[3],row[4],time]
        reviewList.append(appendList)

    return(reviewList)

def retrieve_new_reviews():
    retrieve_reviews_query = "select * from reviews where user_consent = true and mod_id is null"
    cursor.execute(retrieve_reviews_query)
    mobile_records = cursor.fetchall() 
    reviewList = []
    for row in mobile_records:
        user_id = row[0]
        time = "{}".format(row[5])
        user = " ".join(row[1].split())
        review = " ".join(row[2].split()) 
        appendList = [user_id,user,review,row[3],row[4],time]
        reviewList.append(appendList)

    return(reviewList)

def retrieve_user(myUser): 
    cursor.execute("SELECT * FROM gebruikers WHERE user_email='{}'".format(myUser))
    user = cursor.fetchall()
    validate = False
    for row in user:
        validate = True

    return validate

def retrieve_user_data(myUser): 
    cursor.execute("SELECT * FROM gebruikers WHERE user_email='{}'".format(myUser))
    user = cursor.fetchall()
    userData = []
    for row in user:
        userData = [row[0],row[1],row[2],row[3]]
        
    return userData
