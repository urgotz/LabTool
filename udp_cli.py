  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import math
import time
# from matplotlib import pyplot as plt 

PI = math.pi
loop_cnt = 0
t = 0 # unit : s
ap = 10 # unit : mm
z0 = 100 # initial value, unit: mm
fr = 0.1 # unit : Hz
delay = 1 / fr / 100 # unit : s


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# plot_z = []
# plot_t = []
while loop_cnt < 100:
	loop_cnt += 1
	z = ap * math.sin(2 * PI * fr * t) + z0
	send_str = "@A6:0,0,0,0,0," + str(round(z,1)) + ",F0#"
	print(send_str)
	target_addr = ('127.0.0.1', 9800)
	buff = bytes(send_str, encoding = "utf8")
	# plot_z.append(z)
	# plot_t.append(t)
	t += delay
	time.sleep(delay)
	# print(z)
# plt.plot(plot_t, plot_z)
# plt.show()
s.close()
exit(0)
send_str = "@A6:0,0,0,0,0,0,F0#"
target_addr = ('127.0.0.1', 9800)
buff = bytes(send_str, encoding = "utf8")
# print(buff.hex('-'))
#s.sendto(buff, target_addr)
#print(s.recv(1024).decode('utf-8'))


