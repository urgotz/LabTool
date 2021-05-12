#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        # print('Got connection from', self.client_address)

        # Get message and client socket
        msg, sock = self.request
        print('Data: ', msg)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 9800), TimeHandler)
    serv.serve_forever()