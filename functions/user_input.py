# Functie om een user review op te halen.
def user_review():
    user_input = input("Hoe was uw dag? Beschrijf dit in 140 of minder characters. \n")
    user_input_length = len(user_input)
    review_list = []
    if user_input_length <= 140:
        print("")
    elif user_input_length >= 140:
        print("Uw bericht is te lang, deze mag maximaal 140 characters lang zijn.")

    user_name = input("Wat is uw naam? \n")
    
    user_permission = input("Mogen wij dit review Tweeten? (Ja/Nee)\n")
    
    if (user_permission == "Ja") or (user_permission == "ja"):
        user_consent = "1"
    elif (user_permission == "Nee") or (user_permission == "nee"):
        user_consent = "0"
        
    table_name = "reviews"
    review_list = [table_name, user_name, user_input, user_consent] 
    
    return(review_list)
    
