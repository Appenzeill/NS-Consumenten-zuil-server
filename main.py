from functions.user_input import user_review
from functions.user_help import user_help

import getopt
import sys
 
argv = sys.argv[1:]

if argv[0] == "review":
    user_review()
elif argv[0] == "test":
    print("goede test")
elif argv[0] == "--help":
    user_help()

