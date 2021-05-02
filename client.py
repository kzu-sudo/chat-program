#!/usr/bin/python3

import socket

from threading import Thread
from datetime import datetime
from en import cr

class client(object):

    def __init__(self, host, port, en):
        self.host = host
        self.port = port
        self.en = en
        self.kw = "<SEP>"
        self.s = socket.socket()
        self.name = ''

    def initialize(self):
        print(f"[*] Connecting to {self.host}:{self.port}...")
        self.s.connect((self.host, self.port))
        print("[+] Connected.")
        self.name = input("Enter your name: ")

    def kfm(self):
        while True:
            message = self.s.recv(1024)
            if len(message) > 0:
                message = self.en.d_de(message)
                message = message.decode()
                message = message.replace(self.kw, ": ")
                print("\n" + message)

    def start_f(self):
        t = Thread(target=self.kfm)
        t.daemon = True
        t.start()
        #this runs in the main thread
        while True:
            to_send =  input()
            if to_send.lower() == 'q':
                break
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            to_send = f"[{date_now}] {self.name}{self.kw}{to_send}"
            to_send = self.en.d_en(to_send)
            self.s.send(to_send)
        self.s.close()


