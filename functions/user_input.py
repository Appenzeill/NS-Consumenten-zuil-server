from getpass import getpass
from werkzeug.security import generate_password_hash
from functions.retrieve_data import retrieve_user

# Functie om een user review op te halen.
def user_review_terminal():
    review_list = []
    print("Wat is uw mening over het openbaar vervoer vandaag? Beschrijf dit in 140 of minder characters")
    while True:
        user_review = input()
        if len(user_review) <= 140:
            break
        elif len(user_review) >= 140:
            print("Te lang, probeer het opnieuw met 140 of minder characters.")
            
    print("Wat is uw naam?")
    while True:
        user_name = input()
        if len(user_name) != "":
            break
        elif len(user_name) == "":
            print("Te lang, probeer het opnieuw met 50 of minder characters.")
            
    print("Hebben wij toestemming om dit te Tweeten? (Ja/Nee)")
    while True:
        user_permission = input()
        if (user_permission == "Ja") or (user_permission == "ja") or (user_permission == "Nee") or (user_permission == "nee"):
            break
        else:
            print("Geen geldige input, probeer Ja, ja, Nee en nee als input.")
 
    
    if (user_permission == "Ja") or (user_permission == "ja"):
        user_consent = "1"
    elif (user_permission == "Nee") or (user_permission == "nee"):
        user_consent = "0"
        
    table_name = "reviews"
    review_list = [table_name, user_name, user_review, user_consent] 
    
    return(review_list)
    
def user_create_terminal():    
    while True:
        user_email = input("Email: ")
        validation = retrieve_user(user_email)
        if '@' in user_email and validation == False:
            break
        elif not '@' in user_email:
            print("Geen geldige email")
        elif validation == True:
            print("Email bestaat al in database")
            
    print("Rollen:")
    print("1) Moderator")
    print("2) Administrator")
    
    while True:
        user_role = input("rol: ")
        if 1 or 2 in user_role:
            break
        else:
            print("Geen geldige rol, probeer het opnieuw")
    user_password = getpass("Wachtwoord: ")
    user_hash = generate_password_hash(user_password)
    
    user_list = [user_email,user_role,user_hash]

    return user_list


