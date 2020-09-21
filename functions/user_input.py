# simple function to ask for user review.
def test_insert(table_name, user_name, user_review, user_consent):
    print("Tabel naam:",table_name)
    print("Gebruikers naam: ",user_name)
    print("Review: ")
    print(user_review)
    print("Toestemming voor Tweet:",user_consent)
 
def user_review():
    user_input = input("Hoe was uw dag? Beschrijf dit in 140 of minder characters. \n")
    user_input_length = len(user_input)

    print(user_input_length)
    if user_input_length <= 140:
        print("Goede lengte")
    elif user_input_length >= 140:
        print("Uw bericht is te lang")

    user_name = input("Wat is uw naam? \n") 
    user_permission = input("Hebben we toestemming om uw review mogelijk te Tweeten? (Ja/Nee) \n")
    table_name = "reviews"
    test_insert(table_name, user_name, user_input, user_permission)
   
