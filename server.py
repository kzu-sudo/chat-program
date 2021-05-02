#!/usr/bin/python3

import socket
from  threading import Thread

from en import cr

class server(object):
    def __init__(self, host, port, en):
        self.host = host
        self.port = port
        self.en = en
        self.client_sockets = set()
        self.s = socket.socket()


    def initialize(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(5)
        print(f"listening: {self.host} {self.port}")

    def kfm(self, cs):

        while True:
            try:
                msg = cs.recv(1024)
                msg = self.en.d_de(msg)

            except Exception as e:
                print(f"[!] Error: {e}")
                self.client_sockets.remove(cs)

            for client_socket in self.client_sockets:
                tmp = ''
                tmp = self.en.d_en(msg)
                print(tmp)
                client_socket.send(tmp)

    def start_f(self):
        while True:
            kj, client_address = self.s.accept()
            print(client_address)
            self.client_sockets.add(kj)
            t = Thread(target=self.kfm, args=(kj,))
            t.daemon = True
            t.start()

        for cs in self.client_sockets:
            cs.close()

        s.close()
