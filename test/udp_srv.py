#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from socketserver import BaseRequestHandler, UDPServer
# import time

# class TimeHandler(BaseRequestHandler):
#     def handle(self):
#         # print('Got connection from', self.client_address)

#         # Get message and client socket
#         msg, sock = self.request
#         print('Data: ', msg)
#         resp = time.ctime()
#         sock.sendto(resp.encode('ascii'), self.client_address)

# if __name__ == '__main__':
#     serv = UDPServer(('', 9800), TimeHandler)
#     serv.serve_forever()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 8089))
print('Bind UDP on 8089...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)