import numpy as np

# class stewart_model():
#     self.up_plat_joints = []

pi = np.pi

class StewartModel():
	def __init__(self):
		self.init_params()
		self.calc_ori_leg_lens()

	def init_params(self):
		# up: upper platform
		# lp: lower platform
		self.up_short_edge = 100
		self.up_radius = 870/2
		self.lp_short_edge = 100
		self.lp_radius = 870/2
		self.z0 = 515
		self.p0 = np.array([0, 0, self.z0])
		self.ori_leg_lens = np.zeros(6)
		

		# 上平台：
		# 短边对应圆心角
		up_angle1r = np.arccos((self.up_radius**2 + self.up_radius**2 - self.up_short_edge**2)/(2 * self.up_radius * self.up_radius))
		up_angle1d = np.degrees(up_angle1r)
		# 长边对饮圆心角
		up_angle2r = 2*pi/3 - up_angle1r
		up_angle2d = 120 - up_angle1d
		#print('短边对应圆心角:%s, 长边对饮圆心角:%s'%(up_angle1d, up_angle2d))
		up_j1_radian = -(pi/2 + up_angle1r/2)
		up_joint1 = self.get_coordinates_from_radian(self.up_radius, up_j1_radian)
		up_j2_radian = -(pi/2 - up_angle1r/2)
		up_joint2 = self.get_coordinates_from_radian(self.up_radius, up_j2_radian)
		up_j3_radian = up_angle2r + up_angle1r/2 - pi/2
		up_joint3 = self.get_coordinates_from_radian(self.up_radius, up_j3_radian)
		up_j4_radian = up_angle1r + up_j3_radian
		up_joint4 = self.get_coordinates_from_radian(self.up_radius, up_j4_radian)
		up_j5_radian = up_j4_radian + up_angle2r
		up_joint5 = self.get_coordinates_from_radian(self.up_radius, up_j5_radian)
		up_j6_radian = pi - up_j3_radian
		up_joint6 = self.get_coordinates_from_radian(self.up_radius, up_j6_radian)
		self.up_joints = np.array([up_joint1, up_joint2, up_joint3, up_joint4, up_joint5, up_joint6])
		# print('上平台铰点坐标:\n%s\n'% up_joints)


		# 下平台：
		# 短边对应圆心角
		lp_angle1r = np.arccos((self.lp_radius**2 + self.lp_radius**2 - self.lp_short_edge**2)/(2 * self.lp_radius * self.lp_radius))
		lp_angle1d = np.degrees(lp_angle1r)
		# 长边对饮圆心角
		lp_angle2r = 2*pi/3 - lp_angle1r
		lp_angle2d = 120 - lp_angle1d

		lp_j1_radian = -(pi/2 + lp_angle2r/2)
		lp_joint1 = self.get_coordinates_from_radian(self.lp_radius, lp_j1_radian)
		lp_j2_radian = -(pi/2 - lp_angle2r/2)
		lp_joint2 = self.get_coordinates_from_radian(self.lp_radius, lp_j2_radian)
		lp_j3_radian = -(pi/2 - lp_angle2r/2 - lp_angle1r)
		lp_joint3 = self.get_coordinates_from_radian(self.lp_radius, lp_j3_radian)
		lp_j4_radian = lp_angle2r + lp_j3_radian
		lp_joint4 = self.get_coordinates_from_radian(self.lp_radius, lp_j4_radian)
		lp_j5_radian = lp_j4_radian + up_angle1r
		lp_joint5 = self.get_coordinates_from_radian(self.lp_radius, lp_j5_radian)
		lp_j6_radian = pi - lp_j3_radian
		lp_joint6 = self.get_coordinates_from_radian(self.lp_radius, lp_j6_radian)
		self.lp_joints = np.array([lp_joint1, lp_joint2, lp_joint3, lp_joint4, lp_joint5, lp_joint6])
		# print('下平台铰点坐标:\n%s\n'% lp_joints)

	def get_coordinates_from_radian(self, radius, degree):
		return np.array([radius * np.cos(degree), radius * np.sin(degree), 0])

	def get_rotation_matrix(self, rx, ry, rz):
		Rx = np.mat([[1, 0, 0], [0, np.cos(rx), -np.sin(rx)], [0, np.sin(rx), np.cos(rx)]])
		Ry = np.mat([[np.cos(ry), 0, np.sin(ry)], [0, 1, 0], [-np.sin(ry), 0, np.cos(ry)]])
		Rz = np.mat([[np.cos(rz), -np.sin(rz), 0], [np.sin(rz), np.cos(rz), 0], [0, 0, 1]])
		R = Rz * Ry * Rx
		return R

	def get_inv_solution(self, x, y, z, roll, pitch, yaw):
		p = self.p0 + np.array([x, y, z])
		R = self.get_rotation_matrix(roll, pitch, yaw)
		leg_lens = np.zeros(6)
		for i in range(6):
			leg_lens[i] = np.linalg.norm( p.reshape(3,1) + R * self.up_joints[i].reshape(3,1) - self.lp_joints[i].reshape(3,1)) - self.ori_leg_lens[i]
		# print(leg_lens)
		return leg_lens

	def calc_ori_leg_lens(self):
		self.ori_leg_lens = self.get_inv_solution(0,0,0,0,0,0)

if __name__ == '__main__':
	sm = StewartModel()
	# print(sm.get_inv_solution(-28,9,121,-9,-9,-9))
	print(sm.get_inv_solution(0,0,121,1,1,1))

