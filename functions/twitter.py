from jproperties import Properties
import twitter

# Config of reading properties from dbconfig.properties using jproperties.
configs = Properties()
with open('./dbconfig.properties', 'rb') as config_file:
    configs.load(config_file)

# Database credentials are stored in dbconfig.properties with the file listed in .gitignore
credentials = [
    configs.get("twitter.public_key").data,
    configs.get("twitter.secret_key").data,
    configs.get("twitter.acces_token").data,
    configs.get("twitter.secret_acces_token").data,
]

def tweet(tweet):
    api = twitter.Api(
        consumer_key=credentials[0],
        consumer_secret=credentials[1],
        access_token_key=credentials[2],
        access_token_secret=credentials[3]
    )
    user = tweet[0][1]
    review = tweet[0][0]

    message = """
{}
    -{}
""".format(user,review)
    api.PostUpdate(message)
