from jproperties import Properties
import psycopg2

# Config of reading properties from dbconfig.properties using psycopg2.
configs = Properties()
with open('dbconfig.properties', 'rb') as config_file:
    configs.load(config_file)

# Database credentials are stored in dbconfig.properties with the file listed in .gitignore
credentials = [
    configs.get("db.database").data,
    configs.get("db.host").data,
    configs.get("db.username").data,
    configs.get("db.password").data,
    configs.get("db.port").data
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

cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cursor.fetchall():
    print(table)
    
# Closes the connection    
connection.close()
