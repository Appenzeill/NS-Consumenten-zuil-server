from functions.user_input import user_review
from functions.insert_data import insert_review
from functions.user_help import user_help

import getopt
import sys
 
argv = sys.argv[1:]
if argv:
    if argv[0] == "review":
        myList = user_review()
        insert_review(myList)
    elif argv[0] == "test":
        test_insert()
    elif argv[0] == "--help":
        user_help()
    else:
        print("Zie --help voor opties.")
else:
    user_help
