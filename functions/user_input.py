# simple function to ask for user review.
def user_review():
    user_input = input("Hoe was uw dag?,beschrijf dit in 140 of minder characters. \n")
    user_input_length = len(user_input)

    print(user_input_length)
    if user_input_length <= 140:
        print("Goede lengte")
    elif user_input_length >= 140:
        print("Uw bericht is te lang")

