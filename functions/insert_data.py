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

# Insert a new review from user
def insert_review(myList):
    cursor.execute("INSERT INTO reviews (user_name, user_review,user_consent) VALUES(%s, %s, %s)", (myList[1], myList[2], myList[3]))
    connection.commit() # <- We MUST commit to reflect the inserted data
    #cursor.close()
    
# Insert a new user
def insert_user(myList):
    cursor.execute("INSERT INTO gebruikers (user_email, role_id, hash) VALUES(%s, %s, %s)", (myList[0], myList[1], myList[2]))
    connection.commit() # <- We MUST commit to reflect the inserted data
    #cursor.close()

# Insert a new user
def update_user(myList):
    cursor.execute("INSERT INTO gebruikers (user_email, role_id, hash) VALUES(%s, %s, %s)", (myList[0], myList[1], myList[2]))
    connection.commit() # <- We MUST commit to reflect the inserted data
    #cursor.close()

# Update a review
def update_review(myList):
    cursor.execute("UPDATE reviews SET mod_id = {}, mod_comment='{}', mod_review_date = current_date, mod_review_time = current_time, mod_approval = {} WHERE review_id = {};".format(1,2,3,4))
    connection.commit()
