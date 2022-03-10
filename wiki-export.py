from json.tool import main
from pprint import *
import sys
import rl_api

# https://github.com/bekaertruben/wikilists

LG_NAME = sys.argv[1]
LG_PASSWORD = sys.argv[2]

# log in and ensure the account supports reading lists:
rl_api.clientlogin(LG_NAME, LG_PASSWORD)
try:
    rl_api.setup()
    print("set up reading lists for account")
except rl_api.ApiException as e:
    if e.code == "readinglists-db-error-already-set-up":
        print("account already has reading lists")
    else:
        raise e


# example 1: create a new list, update it to change the description, then add the page Runes to it
list_id = rl_api.create(
    "testlist", description="this was made using my bot thingy")['id']
rl_api.update(
    list_id, description="this was totally not made using my bot thingy")
rl_api.create_entry(list_id, "Runes")

# example 2: for every list in the users reading lists, print all titles
lists = rl_api.readinglists()
for lst in lists:
    # print(lst['name'], ":")
    pprint(lst)
    print()
    entries = rl_api.readinglistentries(lst['id'])
    for entry in entries:
        # print("  ", entry['title'])
        # print(entry)
        pprint(entry)
