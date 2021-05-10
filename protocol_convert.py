from can_driver import *
from stewart_model import *
import struct

class ProtoConvt():
	def __init__(self):
		self.can_driver_ = CanDriver()
		self.sm_ = StewartModel()
		self.lead_ = 10 # 导程: 10mm
		self.pul_per_cycle_ = 20000 # 每转脉冲数

	# 单位：mm和°
	def send_location(self, x, y, z, roll, pitch, yaw):
		print('send location:\nx:%f\ty:%f\tz:%f\troll:%f\tpitch:%f\tyaw:%f'%(x,y,z,roll,pitch, yaw) )

		legs_extention = self.sm_.get_inv_solution(x, y, z, roll/180*3.14, pitch/180*3.14, yaw/180*3.14)
		print('legs extention: axis1:%f\taxis2:%f\taxis3:%f\taxis4:%f\taxis5:%f\taxis6:%f'%
			(legs_extention[0],legs_extention[1],legs_extention[2],legs_extention[3],legs_extention[4],legs_extention[5]))
		# 将伸长量mm转换为脉冲数，最小0，最大60000
		pul_output = np.maximum((legs_extention / self.lead_ * self.pul_per_cycle_), 0).astype(int)
		pul_output = np.minimum(pul_output, 300 / self.lead_ * self.pul_per_cycle_).astype(int)
		
		for i in range(6):
			data = bytes()
			data += struct.pack("<B", 0x01)  # write
			data += struct.pack("<B", 0x05)  # send data
			data += struct.pack('<L', pul_output[i]) # position
			data += struct.pack('<H', 1500) # velocity
			node_id = 0x601 + i
			ret = self.can_driver_.send(node_id, data)
			print('send data: %s-%s %s'%(hex(node_id), data.hex('-'), 'succeed!' if ret else'failed!'))
			# print(hex(node_id))
			# for j in range(8):
			# 	print(hex(data[j]))
		# print(hex(pul_output[0]))
		# print(data)

if __name__ == '__main__':
	pc = ProtoConvt()
	pc.send_location(-28,9,121,-9,-9,-9)
	# print(struct.unpack('<L', b'\xB0\x8f\x06\x00'))
	# print(struct.unpack('<H', b'\xDC\x05'))
	# print(struct.unpack('<L', b'\x40\x9c\x00\x00'))