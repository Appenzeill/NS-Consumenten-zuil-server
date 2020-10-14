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

def retrieve_reviews():
    retrieve_reviews_query = "select * from reviews"
    cursor.execute(retrieve_reviews_query)
    mobile_records = cursor.fetchall() 
    reviewList = []
    for row in mobile_records:
        #appendList = "{" + "'id': '{}', user_name': '{}', 'user_review': '{}', 'user_consent': '{}', 'review_date': '{}'".format(row[0], row[1].strip(), row[2].strip(), row[3], row[4]) + "}"
        #appendList = "{"name":"John","age":30,"cars":[ "Ford", "BMW", "Fiat" ]}"
        #appendList = ['test','test'],['test','test','test']
        appendList = [row[1],row[2],row[3]]
        reviewList.append(appendList)

    return(reviewList)
