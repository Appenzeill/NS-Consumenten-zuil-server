from functions.user_input import user_review, test_insert
from functions.user_help import user_help

import getopt
import sys
 
argv = sys.argv[1:]
if argv:
    if argv[0] == "review":
        user_review()
    elif argv[0] == "test":
        test_insert()
    elif argv[0] == "--help":
        user_help()
    else:
        print("Zie --help voor opties.")
else:
    user_help()
