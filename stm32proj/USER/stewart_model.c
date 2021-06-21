#include "stewart_model.h"
#include "usart.h"

Mat up_joints[6];
float up_joints_arr[6][3] = {
 { -50.,         -432.11688234,    0.        },
 {  50.,         -432.11688234,    0.        },
 { 399.22419751,  172.75717098,    0.        },
 { 349.22419751,  259.35971136,    0.        },
 {-349.22419751,  259.35971136,    0.        },
 {-399.22419751,  172.75717098,    0.        }};

Mat lp_joints[6];
float lp_joints_arr[6][3] = {
 {-349.22419751, -259.35971136,    0.        },
 { 349.22419751, -259.35971136,    0.        },
 { 399.22419751, -172.75717098,    0.        },
 {  50.,          432.11688234,    0.        },
 { -50.,          432.11688234,    0.        },
 {-399.22419751, -172.75717098,    0.        }};
// 旋转矩阵
Mat R;
// 初始腿长
float ori_leg_len = 620.16542994;
// 初始位置
Mat p0;
float p0_arr[3] = {0, 0, 515};



Mat res, Rx, Ry, Rz, tmp;
Mat p, tmp1,tmp2,tmp3;

void get_rotation_matrix(Mat * mat, float rx, float ry, float rz) {
	MatEye(&res);
	MatEye(&Rx);
	MatEye(&Ry);
	MatEye(&Rz);
	MatEye(&tmp);

	Rx.element[1][1] = cos(rx);
	Rx.element[1][2] = -sin(rx);
	Rx.element[2][1] = sin(rx);
	Rx.element[2][2] = cos(rx);
	Ry.element[0][0] = cos(ry);
	Ry.element[0][2] = sin(ry);
	Ry.element[2][0] = -sin(ry);
	Ry.element[2][2] = cos(ry);
	Rz.element[0][0] = cos(rz);
	Rz.element[0][1] = -sin(rz);
	Rz.element[1][0] = sin(rz);
	Rz.element[1][1] = cos(rz);
	// MatPrint(&Rx, "Rx");
	// MatPrint(&Ry, "Ry");
	// MatPrint(&Rz, "Rz");
	MatMul(&Rz, &Ry, &tmp);
	MatMul(&tmp, &Rx, &res);
	MatCopy(&res, &R);
	// MatPrint(&R, "R");
	/*
	MatDelete(&res);
	MatDelete(&Rx);
	MatDelete(&Ry);
	MatDelete(&Rz);
	MatDelete(&tmp);
	*/
	
}


void init_stewart_params(){
	int i;
	// 初始化旋转矩阵
	MatCreate(&R, 3, 3);
	MatEye(&R);
	// 初始化初始位置
	MatCreate(&p0, 3, 1);
	MatSetVal(&p0, p0_arr);
	for(i = 0; i < 6; i++) {
		MatCreate(&up_joints[i], 3, 1);
		MatCreate(&lp_joints[i], 3, 1);
		MatSetVal(&up_joints[i], up_joints_arr[i]);
		MatSetVal(&lp_joints[i], lp_joints_arr[i]);
		// MatPrint(&up_joints[i], "up_joints");
		// MatPrint(&lp_joints[i], "lp_joints");
	}
	MatCreate(&res, 3, 3);
	MatCreate(&Rx, 3, 3);
	MatCreate(&Ry, 3, 3);
	MatCreate(&Rz, 3, 3);
	MatCreate(&tmp, 3, 3);
	MatEye(&res);
	MatEye(&Rx);
	MatEye(&Ry);
	MatEye(&Rz);
	MatEye(&tmp);

	
	MatCreate(&tmp1, 3, 1);
	MatCreate(&tmp2, 3, 1);
	MatCreate(&tmp3, 3, 1);
	MatCreate(&p, 3, 1);
}

float get_norm(Mat *src) {
	int row, col;
	float res = 0;
	if (src->col != 1 && src->row != 1) {
		printf("no implement of get norm func\r\n");
		return 0;
	}
	for(row = 0 ; row < src->row ; row++){
		for(col = 0 ; col < src->col ; col++){
			res += pow(src->element[row][col], 2);
		}
	}
	return sqrt(res);
}


void get_inv_solution(const float * in, float * out) {

	float pos[3];
	int i;
	pos[0] = in[0]; // x
	pos[1] = in[1]; // y
	pos[2] = in[2]; // z
	
	MatSetVal(&p, pos);
	MatAdd(&p, &p0, &p);
	get_rotation_matrix(&R, in[3], in[4], in[5]); 
	
	for (i = 0; i < 6; i++) {
		MatMul(&R, &up_joints[i], &tmp1);
		MatAdd(&p, &tmp1, &tmp2);
		MatSub(&tmp2, &lp_joints[i], &tmp3);
		// MatPrint(&tmp3, "leg_vec");
		out[i] = get_norm(&tmp3) - ori_leg_len;
		// printf("out[%d]=%f\r\n",i, out[i]);
	}
	//MatDelete(&tmp1);
	//MatDelete(&tmp2);
	//MatDelete(&tmp3);
}
