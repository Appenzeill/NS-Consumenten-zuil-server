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

def insert_review(myList):
    print(myList)
    cursor.execute("INSERT INTO reviews (user_name, user_review,user_consent) VALUES(%s, %s, %s)", (myList[1], myList[2], myList[3]))
    connection.commit() # <- We MUST commit to reflect the inserted data
    cursor.close()
