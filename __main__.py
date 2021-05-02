#!/usr/bin/python3

from server import server
from client import client
from parser import parser
from en import cr

import hashlib

def main():

    f = parser()
    arguments = f.parse()
    password = str(arguments["key"])
    key = hashlib.sha256(password.encode('UTF-8')).digest()
    l= cr(key)

    if arguments["option"] == False:
        k = server(arguments["host"], arguments["port"], l)
        k.initialize()
        k.start_f()

    elif arguments["option"] == True:
        k = client(arguments["host"], arguments["port"], l)
        k.initialize()
        k.start_f()

#veni vidi vici
if __name__ == "__main__":
    main()
