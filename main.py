from functions.user_input import user_review_terminal, user_create_terminal
from functions.insert_data import insert_review, insert_user
from functions.user_help import user_help
from functions.webserver import webserver

import getopt
import sys

argv = sys.argv[1:]
if argv:
    if argv[0] == "review":
        myList = user_review_terminal()
        insert_review(myList)
    elif argv[0] == "user":
        userData = user_create_terminal()
        print(userData)
        insert_user(userData)
    elif argv[0] == "--help":
        user_help()
    elif argv[0] == "webserver":
        webserver()
    else:
        print("Zie --help voor opties.")
else:
    user_help()
