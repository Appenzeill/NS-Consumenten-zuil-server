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
        time = "{}".format(row[5])
        user = " ".join(row[1].split())
        review = " ".join(row[2].split()) 
        appendList = [user,review,row[3],row[4],time]
        reviewList.append(appendList)

    return(reviewList)
