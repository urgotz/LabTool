#include "stm32f4xx.h" 
// tri-fun param struct
typedef struct
{
	u8 enable;
	float ap;
	float fr;
	float pha;
} tri_param_stru;

// data frame struct
typedef struct  
{
	u8 cmd_type;
	u8 pos[6][4];
	u8 vel[2];
	tri_param_stru params[6]; //x, y, z, roll, pitch yaw
	u32 cnt;	// �˶�ʱ��
	u32 z0;  //��λ�߶�
} data_frame_t;

#define SEND_INTERVAL 2
#define CAN_SEND_INT ((SEND_INTERVAL)*1000/6)
