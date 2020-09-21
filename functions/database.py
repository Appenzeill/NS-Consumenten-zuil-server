from jproperties import Properties
import psycopg2
from psycopg2 import sql

# Config of reading properties from dbconfig.properties using psycopg2.
configs = Properties()
with open('./functions/dbconfig.properties', 'rb') as config_file:
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

def insert_review():
    cursor.execute(
        sql.SQL("insert into {} values (%s, %s)")
             .format(sql.Identifier('my_table')),
        [10, 20])

def test_insert(table_name, user_name, user_review, user_consent):
    print(table_name, user_name, review_content, user_consent)
    
