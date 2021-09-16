#include "sys.h"
#include "delay.h"
#include "usart.h"
#include "led.h"
#include "key.h"
//#include "lwip_comm.h"
#include "LAN8720.h"
#include "usmart.h"
#include "timer.h"
#include "lcd.h"
#include "sram.h"
#include "rtc.h"
#include "beep.h"
#include "adc.h"
#include "temperature.h"
#include "sram.h"
#include "malloc.h"
#include "tcp_server_demo.h"
#include "httpd.h"
#include "can.h"
#include "math.h"
#include "stewart_model.h"
#include "common.h"
//#include "udp_demo.h" 

//ALIENTEK 探索者STM32F407开发板 实验55
//LWIP网络通信综合实验-库函数版本
//技术支持：www.openedv.com
//淘宝店铺：http://eboard.taobao.com  
//广州市星翼电子科技有限公司  
//作者：正点原子 @ALIENTEK

/*ALIENTEK为LWIP学习专门编写手册《ALIENTEK STM32F4 LWIP使用教程.pdf》，详细说明请参考手册。*/

extern void Adc_Temperate_Init(void);	//声明内部温度传感器初始化函数
//加载UI
//mode:
//bit0:0,不加载;1,加载前半部分UI
//bit1:0,不加载;1,加载后半部分UI
void lwip_test_ui(u8 mode)
{
	u8 speed;
	u8 buf[30]; 
	POINT_COLOR=RED;
	if(mode&1<<0)
	{
		LCD_Fill(30,30,lcddev.width,110,WHITE);	//清除显示
		LCD_ShowString(30,30,200,16,16,"Explorer STM32F4");
		LCD_ShowString(30,50,200,16,16,"Ethernet lwIP Test");
		LCD_ShowString(30,70,200,16,16,"ATOM@ALIENTEK");
		LCD_ShowString(30,90,200,16,16,"2014/8/15"); 	
	}
	if(mode&1<<1)
	{
		LCD_Fill(30,110,lcddev.width,lcddev.height,WHITE);	//清除显示
		LCD_ShowString(30,110,200,16,16,"lwIP Init Successed");
		if(lwipdev.dhcpstatus==2)sprintf((char*)buf,"DHCP IP:%d.%d.%d.%d",lwipdev.ip[0],lwipdev.ip[1],lwipdev.ip[2],lwipdev.ip[3]);//打印动态IP地址
		else sprintf((char*)buf,"Static IP:%d.%d.%d.%d",lwipdev.ip[0],lwipdev.ip[1],lwipdev.ip[2],lwipdev.ip[3]);//打印静态IP地址
		LCD_ShowString(30,130,210,16,16,buf); 
		speed=LAN8720_Get_Speed();//得到网速
		if(speed&1<<1)LCD_ShowString(30,150,200,16,16,"Ethernet Speed:100M");
		else LCD_ShowString(30,150,200,16,16,"Ethernet Speed:10M");
		LCD_ShowString(30,170,200,16,16,"KEY0:TCP Server Test");
		LCD_ShowString(30,190,200,16,16,"KEY1:TCP Client Test");
		LCD_ShowString(30,210,200,16,16,"KEY2:UDP Test");
	}
}

data_frame_t frame, rsp_frm;
u8 state; // 0: Idle 1: Busy
u8 rsp_data_send_flag;
//////////////

CanTxMsg TxMessage;
CanRxMsg RxMessage;
u8 mbox;
u8 *can_recv_buf;
u8 *tcp_rsp_buf;
u8 *ori_pos_buf;
// extern u8 udp_demo_flag;
void refresh_pos_data_from_can_recv(){
	int tmp,j;
	tmp = CAN_MessagePending(CAN1,CAN_FIFO0);
	if ( tmp > 0 ) {
//		printf("pending num:%d\r\n", tmp);
		CAN_Receive(CAN1, CAN_FIFO0, &RxMessage);//读取数据	
//		printf("data[%d]: ", RxMessage.StdId - 0x580);
//		for( j = 0; j <8 ; j ++) {
//				printf("0x%x ", RxMessage.Data[j]);
//		}
//		printf("\r\n");

		if (RxMessage.DLC != 0 && (RxMessage.Data[1] == 0x15||RxMessage.Data[1] == 0x05)){
//			printf("leg[%d]: ", RxMessage.StdId - 0x580);
//			for( j = 0; j <8 ; j ++) {
//					printf("0x%x ", RxMessage.Data[j]);
//			}
//			printf("\r\n");
			for (j = 0; j < 4; j++) {//读取四个字节的位置信息
//				printf("data:%x,",tcp_rsp_buf[(RxMessage.StdId - 0x581) *4+j]);
				tcp_rsp_buf[(RxMessage.StdId - 0x581) *4+j] = RxMessage.Data[2+j];
//				printf("data after:%x,",tcp_rsp_buf[(RxMessage.StdId - 0x581) *4+j]);
			}
		}
//		printf("[main]send data response: %s size:%d.\r\n", tcp_rsp_buf, strlen((char*)tcp_rsp_buf));
		mymemset(&RxMessage.Data[0], 0, 8);
	}
}
int main(void)
{
	NVIC_InitTypeDef NVIC_InitStructure; // added by wly
	err_t err;  
	struct tcp_pcb *tcppcbnew;  	//定义一个TCP服务器控制块
	struct tcp_pcb *tcppcbconn;  	//定义一个TCP服务器控制块

//	struct udp_pcb *udppcb;  	//定义一个UDP服务器控制块
//	struct ip_addr rmtipaddr;  	//远端ip地址

	u8 res=0;		

	
	float pos[6] = {0, 0, 0, 0, 0, 0};
	float legs[6] = {0,0,0,0,0,0};
	u32 data[6] = {0,0,0,0,0,0};
	int index; 
	int i;
	float time = 0;
	int total_cnt = 0;
	u8 init_flag = 0;
	u8 this_loop_has_delayed = 0;
	u8 t=0;
	u8 rsp_time_cnt=0;
	u8 ori_pos_stable_cnt=0;
	//u8 key;
	
	rsp_data_send_flag = 1;
	
	
	delay_init(168);       	//延时初始化
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//设置系统中断优先级分组2
	uart_init(115200);   	//串口波特率设置
	usmart_dev.init(84); 	//初始化USMART
	LED_Init();  			//LED初始化
	KEY_Init();  			//按键初始化
	LCD_Init(); 			//LCD初始化
	FSMC_SRAM_Init();		//初始化外部SRAM  
	BEEP_Init();			//蜂鸣器初始化
	My_RTC_Init();  		//RTC初始化
	Adc_Init();  			//ADC初始化 
	Adc_Temperate_Init(); 	//内部温度传感器初始化
	TIM3_Int_Init(999,839); //100khz的频率,计数1000为10ms
	mymem_init(SRAMIN);		//初始化内部内存池
	mymem_init(SRAMEX);		//初始化外部内存池
	mymem_init(SRAMCCM);	//初始化CCM内存池
	POINT_COLOR = RED; 		//红色字体
	can_recv_buf=mymalloc(SRAMIN,10);	//申请内存
	if(can_recv_buf==NULL)return 0;
	tcp_rsp_buf=mymalloc(SRAMIN,128);	//申请内存
	ori_pos_buf=mymalloc(SRAMIN,128);	//申请内存
	if(tcp_rsp_buf==NULL)return 0;
	if(ori_pos_buf==NULL)return 0;
	pbuf_alloc(PBUF_TRANSPORT,128,PBUF_POOL);
	CAN1_Mode_Init(CAN_SJW_1tq,CAN_BS2_6tq,CAN_BS1_7tq,3,CAN_Mode_Normal);
	
 // added by wly
  NVIC_PriorityGroupConfig(NVIC_PriorityGroup_0);

  NVIC_InitStructure.NVIC_IRQChannel = CAN1_RX0_IRQn;
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0x00;
  NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0x01;
  NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  NVIC_Init(&NVIC_InitStructure);
	
	frame.cmd_type = 0;
	state = 0;
	init_stewart_params();
	//get_inv_solution(in, out);
	
	//先初始化lwIP(包括LAN8720初始化),此时必须插上网线,否则初始化会失败!! 
	printf("lwIP Initing...\r\n");
	while(lwip_comm_init()!=0)
	{
		printf("lwIP Init failed!\r\n");
		delay_ms(1000);
		printf("Retrying...\r\n");
	}
	printf("lwIP Init Successed\r\n");
	//等待DHCP获取 
 	printf("DHCP IP configing...\r\n");
	while((lwipdev.dhcpstatus!=2)&&(lwipdev.dhcpstatus!=0XFF))//等待DHCP获取成功/超时溢出
	{
		lwip_periodic_handle();
	}
	httpd_init();	//HTTP初始化(默认开启websever)
	
	printf("Server IP:%d.%d.%d.%d",lwipdev.ip[0],lwipdev.ip[1],lwipdev.ip[2],lwipdev.ip[3]);//服务器IP
	printf("Server Port:%d",TCP_SERVER_PORT);//服务器端口号
	tcppcbnew=tcp_new();	//创建一个新的pcb
	if(tcppcbnew)			//创建成功
	{ 
		err=tcp_bind(tcppcbnew,IP_ADDR_ANY,TCP_SERVER_PORT);	//将本地IP与指定的端口号绑定在一起,IP_ADDR_ANY为绑定本地所有的IP地址
		if(err==ERR_OK)	//绑定完成
		{
			tcppcbconn=tcp_listen(tcppcbnew); 			//设置tcppcb进入监听状态
			tcp_accept(tcppcbconn,tcp_server_accept); 	//初始化LWIP的tcp_accept的回调函数
		}else res=1;  
	}else res=1;
	POINT_COLOR=BLUE;//蓝色字体

//	// 创建udp
//	udppcb=udp_new();
//	if(udppcb)//创建成功
//	{ 
//		IP4_ADDR(&rmtipaddr,lwipdev.remoteip[0],lwipdev.remoteip[1],lwipdev.remoteip[2],lwipdev.remoteip[3]);
//		printf("Remote IP:%d.%d.%d.%d",lwipdev.remoteip[0],lwipdev.remoteip[1],lwipdev.remoteip[2],lwipdev.remoteip[3]);//服务器IP

//		err=udp_connect(udppcb,&rmtipaddr,UDP_DEMO_PORT);//UDP客户端连接到指定IP地址和端口号的服务器
//		if(err==ERR_OK)
//		{
//			err=udp_bind(udppcb,IP_ADDR_ANY,UDP_DEMO_PORT);//绑定本地IP地址与端口号
//			if(err==ERR_OK)	//绑定完成
//			{
//				printf("bind port succeed!\r\n");
//				udp_recv(udppcb,udp_demo_recv,NULL);//注册接收回调函数 
//			}else res=1;
//		}else res=1;		
//	}else res=1;
	
	
	
	while(res==0)
	{
//		// 发送udp报文
//		udp_demo_senddata(udppcb);
//		if(udp_demo_flag&1<<6)//是否收到数据?
//		{
//			udp_demo_flag&=~(1<<6);//标记数据已经被处理了.
//		} 
		if ( state == 0 ) {
			time = 0;
			total_cnt = 0;


			if( frame.cmd_type == 0x01 ){ // 单点发送
				for ( index = 0 ; index < 6; index ++) {
					TxMessage.StdId = 0x0601 + index;
					TxMessage.IDE=CAN_ID_STD;		  // 使用标准帧识符
					TxMessage.RTR=CAN_RTR_DATA;		  // 消息类型为数据帧，一帧8位	
					TxMessage.DLC = 8;
					TxMessage.Data[7] = frame.vel[1];
					TxMessage.Data[6] = frame.vel[0];
					TxMessage.Data[5] = frame.pos[index][3];
					TxMessage.Data[4] = frame.pos[index][2];
					TxMessage.Data[3] = frame.pos[index][1];
					TxMessage.Data[2] = frame.pos[index][0];
					TxMessage.Data[1] = 0x05;
					TxMessage.Data[0] = 0x01;
					/*
					for( j = 0; j <8 ; j ++) {
						printf("0x%x ", TxMessage.Data[j]);
					}*/
					CAN_Transmit(CAN1, &TxMessage);  
					
					delay_us(CAN_SEND_INT);
					refresh_pos_data_from_can_recv();
					this_loop_has_delayed = 1;
				}
				state = 0;
				frame.cmd_type = 0x00;
			} 
			if ( frame.cmd_type == 0x02 ) { // 连续发送
				state = 1;
				this_loop_has_delayed = 0;
			}
			if ( frame.cmd_type == 0x04 ) {
				state = 2;
				this_loop_has_delayed = 0;
			}
		}
		if ( state == 1 ) {// 连续发送
			for ( i = 0; i < 6; i ++) {
				if ( frame.params[i].enable ) {
					pos[i] = frame.params[i].ap * sin ( 2 * PI * frame.params[i].fr * time + frame.params[i].pha);
				} else {
					pos[i] = 0;
				}
			}
			pos[2] += frame.z0; // 加上中位高度
			get_inv_solution(pos, legs);
			for ( i = 0; i < 6; i ++) {
				if ( legs[i] < 0 )
					data[i] = 0;
				if ( legs[i] > 0 && legs[i] < 300/10*20000)
					data[i] = legs[i] / 10 * 20000;
				if ( legs[i] > 300/10*20000)
					data[i] = 300/10*20000;
				
				TxMessage.StdId = 0x0601 + i;
				TxMessage.IDE=CAN_ID_STD;		  // 使用标准帧识符
				TxMessage.RTR=CAN_RTR_DATA;		  // 消息类型为数据帧，一帧8位	
				TxMessage.DLC = 8;
				TxMessage.Data[7] = 0x11; 	//这里暂时使用最大速度
				TxMessage.Data[6] = 0x94;
				mymemcpy(&TxMessage.Data[2], &data[i], 4);
				TxMessage.Data[1] = 0x05;
				TxMessage.Data[0] = 0x01;
				
				CAN_Transmit(CAN1, &TxMessage);
				
				
				
				delay_us(CAN_SEND_INT);
				if (total_cnt%50 == 0){
					refresh_pos_data_from_can_recv();
				}
				this_loop_has_delayed = 1;
				// printf("leg[%d]:%f, data[%d]:%d\r\n", i, legs[i], i, data[i]);
			}
			// printf("%f ",time);
			time += (float)SEND_INTERVAL / 1000 ;
			if (total_cnt > frame.cnt/SEND_INTERVAL) {
				printf("total_cnt:%d, frame.cnt:%d, T:%d\r\n", total_cnt, \
								frame.cnt, frame.cnt/SEND_INTERVAL);
				time = 0;
				state = 0;
				frame.cmd_type = 0x00;
				total_cnt = 0;
			}
			total_cnt ++;
			lwip_periodic_handle();
			//delay_ms(SEND_INTERVAL);
		}
		if ( (state == 2 && frame.cmd_type == 0x04 ) || init_flag == 0) { // 平台复位 
			for ( index = 0 ; index < 6; index ++) {
				TxMessage.StdId = 0x0601 + index;
				TxMessage.IDE=CAN_ID_STD;		  // 使用标准帧识符
				TxMessage.RTR=CAN_RTR_DATA;		  // 消息类型为数据帧，一帧8位	
				TxMessage.DLC = 8;
				mymemset(&TxMessage.Data[0], 0, 8);
				TxMessage.Data[2] = 0x01;
				TxMessage.Data[1] = 0x03;
				TxMessage.Data[0] = 0x01;
				CAN_Transmit(CAN1, &TxMessage);  
				//CAN1_Send_Msg(TxMessage.Data,8);
				delay_us(CAN_SEND_INT);
				this_loop_has_delayed = 1;
			}
			delay_ms(5000);
			frame.cmd_type = 0x00;
			state = 0;
			if (!init_flag) {
				init_flag = 1;
			}
		}
		rsp_time_cnt++;
		if ( state == 0 && frame.cmd_type == 0x00 && rsp_time_cnt ==200) { //无指令下发时，自动轮询请求下位机参数
			rsp_time_cnt = 0;
			for ( index = 0 ; index < 6; index ++) {
				TxMessage.StdId = 0x0601 + index;
				TxMessage.IDE=CAN_ID_STD;		  // 使用标准帧识符
				TxMessage.RTR=CAN_RTR_DATA;		  // 消息类型为数据帧，一帧8位	
				TxMessage.DLC = 8;
				mymemset(&TxMessage.Data[0], 0, 8);
				TxMessage.Data[1] = 0x15; //查询位置信息
				TxMessage.Data[0] = 0x00;	// 0x00:读取数据
				mbox = CAN_Transmit(CAN1, &TxMessage);  
				delay_us(CAN_SEND_INT);
//					while((CAN_TransmitStatus(CAN1, mbox)==CAN_TxStatus_Failed)&&(i<0XFFF))i++;	//等待发送结束
//					if(i>=0XFFF){
//						printf("send data request timeout!\r\n");
//						i=0;
//						break;
//					}
				refresh_pos_data_from_can_recv();
			}
			if (init_flag == 1 ){
				ori_pos_stable_cnt++;
			}
			if (ori_pos_stable_cnt>10){
				//int j;
				init_flag = 2;
				ori_pos_stable_cnt = 0;
				mymemcpy(ori_pos_buf, tcp_rsp_buf, 128);
									
//					printf("ori leg data: \r\n");
//					for(j=0; j<24);j++){
//						printf("0x%x,",ori_pos_buf[j]);
//					}printf("\r\n");
			}
		}

		//printf("state:%d cmdtype:%d, rspcnt:%d\r\n",state,frame.cmd_type,rsp_time_cnt);
		lwip_periodic_handle();
		if (this_loop_has_delayed == 0 ) {
			delay_ms(SEND_INTERVAL);
		} 
		
		
		t++;
		if(t==200)
		{
			//int j;
			t=0;
			LED0=!LED0;
//			printf("cur leg data: \r\n");
//			for(j=0; j<24);j++){
//				printf("0x%x,",tcp_rsp_buf[j]);
//			}
//			printf("\r\n");
		}
		this_loop_has_delayed = 0;
  }
	tcp_server_connection_close(tcppcbnew,0);//关闭TCP Server连接
	tcp_server_connection_close(tcppcbconn,0);//关闭TCP Server连接 
	tcp_server_remove_timewait(); 
	// udp_demo_connection_close(udppcb); 
	mymemset(tcppcbnew,0,sizeof(struct tcp_pcb));
	mymemset(tcppcbconn,0,sizeof(struct tcp_pcb)); 
	myfree(SRAMIN,can_recv_buf); 
	myfree(SRAMIN,tcp_rsp_buf);
	myfree(SRAMIN,ori_pos_buf); 
} 
