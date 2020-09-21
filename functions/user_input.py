# Functie om een user review op te halen.
def user_review():
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
    
