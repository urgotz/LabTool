#include "tcp_server_demo.h" 
#include "delay.h"
#include "usart.h"
#include "led.h"
#include "key.h"
#include "lcd.h"
#include "malloc.h"
#include "stdio.h"
#include "string.h"
#include "can.h"


#include "common.h"
//////////////////////////////////////////////////////////////////////////////////	 
//本程序只供学习使用，未经作者许可，不得用于其它任何用途
//ALIENTEK STM32F407开发板
//TCP Server 测试代码	   
//正点原子@ALIENTEK
//技术论坛:www.openedv.com
//创建日期:2014/8/15
//版本：V1.0
//版权所有，盗版必究。
//Copyright(C) 广州市星翼电子科技有限公司 2009-2019
//All rights reserved									  
//*******************************************************************************
//修改信息
//无
////////////////////////////////////////////////////////////////////////////////// 	   
 
//TCP Server接收数据缓冲区
u8 tcp_server_recvbuf[TCP_SERVER_RX_BUFSIZE];	
//TCP服务器发送数据内容
const u8 *tcp_server_sendbuf="Explorer STM32F407 TCP Server send data\r\n";

//TCP Server 测试全局状态标记变量
//bit7:0,没有数据要发送;1,有数据要发送
//bit6:0,没有收到数据;1,收到数据了.
//bit5:0,没有客户端连接上;1,有客户端连接上了.
//bit4~0:保留
u8 tcp_server_flag;	 
u8 rsp_tcp_flag;

extern data_frame_t frame, rsp_frm;
extern u8 state;
extern u8 rsp_data_send_flag;

extern CanTxMsg TxMessage;
extern CanRxMsg RxMessage;
extern u8 mbox;
extern u8 *can_recv_buf;
extern u8 *tcp_rsp_buf;
extern u8 *ori_pos_buf;
/////////////
 
//TCP Server 测试
void tcp_server_test(void)
{
	err_t err;  
	struct tcp_pcb *tcppcbnew;  	//定义一个TCP服务器控制块
	struct tcp_pcb *tcppcbconn;  	//定义一个TCP服务器控制块
	
	u8 *tbuf;
 	u8 key;
	u8 res=0;		
	u8 t=0; 
	u8 connflag=0;		//连接标记
	
//	int i = 0; //added by wly
	
	LCD_Clear(WHITE);	//清屏
	POINT_COLOR=RED; 	//红色字体
	LCD_ShowString(30,30,200,16,16,"Explorer STM32F4");
	LCD_ShowString(30,50,200,16,16,"TCP Server Test");
	LCD_ShowString(30,70,200,16,16,"ATOM@ALIENTEK");  
	LCD_ShowString(30,90,200,16,16,"KEY0:Send data");  
	LCD_ShowString(30,110,200,16,16,"KEY_UP:Quit");  
	tbuf=mymalloc(SRAMIN,200);	//申请内存
	if(tbuf==NULL)return ;		//内存申请失败了,直接退出
	sprintf((char*)tbuf,"Server IP:%d.%d.%d.%d",lwipdev.ip[0],lwipdev.ip[1],lwipdev.ip[2],lwipdev.ip[3]);//服务器IP
	printf("%s\r\n", (char*)tbuf);
	LCD_ShowString(30,130,210,16,16,tbuf);  
	sprintf((char*)tbuf,"Server Port:%d",TCP_SERVER_PORT);//服务器端口号
	LCD_ShowString(30,150,210,16,16,tbuf); 
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
	while(res==0)
	{
		key=KEY_Scan(0);
		if(key==WKUP_PRES)break;
		if(key==KEY0_PRES)//KEY0按下了,发送数据
		{
			tcp_server_flag|=1<<7;//标记要发送数据
		}
		if(tcp_server_flag&1<<6)//是否收到数据?
		{
			LCD_Fill(30,210,lcddev.width-1,lcddev.height-1,WHITE);//清上一次数据
			LCD_ShowString(30,210,lcddev.width-30,lcddev.height-210,16,tcp_server_recvbuf);//显示接收到的数据			
			//printf("recv data:%s\r\n", tcp_server_recvbuf);
			//printf("recv data:\r\n");
			//for(i = 0 ; i < TCP_SERVER_RX_BUFSIZE; i++){
			//	printf("0x%x ", tcp_server_recvbuf[i]);
			//}
			//printf("\r\n");
			
			tcp_server_flag&=~(1<<6);//标记数据已经被处理了.
		}
		if(tcp_server_flag&1<<5)//是否连接上?
		{
			if(connflag==0)
			{ 
				sprintf((char*)tbuf,"Client IP:%d.%d.%d.%d",lwipdev.remoteip[0],lwipdev.remoteip[1],lwipdev.remoteip[2],lwipdev.remoteip[3]);//客户端IP
 				LCD_ShowString(30,170,230,16,16,tbuf);
				POINT_COLOR=RED;
				LCD_ShowString(30,190,lcddev.width-30,lcddev.height-190,16,"Receive Data:");//提示消息		
				POINT_COLOR=BLUE;//蓝色字体
				connflag=1;//标记连接了
			} 
		}else if(connflag)
		{
			LCD_Fill(30,170,lcddev.width-1,lcddev.height-1,WHITE);//清屏
			connflag=0;	//标记连接断开了
		}
		lwip_periodic_handle();
		delay_ms(2);
		t++;
		if(t==200)
		{
			t=0;
			LED0=!LED0;
		} 
	}   
	tcp_server_connection_close(tcppcbnew,0);//关闭TCP Server连接
	tcp_server_connection_close(tcppcbconn,0);//关闭TCP Server连接 
	tcp_server_remove_timewait(); 
	memset(tcppcbnew,0,sizeof(struct tcp_pcb));
	memset(tcppcbconn,0,sizeof(struct tcp_pcb)); 
	myfree(SRAMIN,tbuf);
} 
//lwIP tcp_accept()的回调函数
err_t tcp_server_accept(void *arg,struct tcp_pcb *newpcb,err_t err)
{
	err_t ret_err;
	struct tcp_server_struct *es; 
 	LWIP_UNUSED_ARG(arg);
	LWIP_UNUSED_ARG(err);
	tcp_setprio(newpcb,TCP_PRIO_MIN);//设置新创建的pcb优先级
	es=(struct tcp_server_struct*)mem_malloc(sizeof(struct tcp_server_struct)); //分配内存
 	if(es!=NULL) //内存分配成功
	{
		es->state=ES_TCPSERVER_ACCEPTED;  	//接收连接
		es->pcb=newpcb;
		es->p=NULL;
		
		tcp_arg(newpcb,es);
		tcp_recv(newpcb,tcp_server_recv);	//初始化tcp_recv()的回调函数
		tcp_err(newpcb,tcp_server_error); 	//初始化tcp_err()回调函数
		tcp_poll(newpcb,tcp_server_poll,1);	//初始化tcp_poll回调函数
		tcp_sent(newpcb,tcp_server_sent);  	//初始化发送回调函数
		  
		tcp_server_flag|=1<<5;				//标记有客户端连上了
		lwipdev.remoteip[0]=newpcb->remote_ip.addr&0xff; 		//IADDR4
		lwipdev.remoteip[1]=(newpcb->remote_ip.addr>>8)&0xff;  	//IADDR3
		lwipdev.remoteip[2]=(newpcb->remote_ip.addr>>16)&0xff; 	//IADDR2
		lwipdev.remoteip[3]=(newpcb->remote_ip.addr>>24)&0xff; 	//IADDR1 
		ret_err=ERR_OK;
	}else ret_err=ERR_MEM;
	return ret_err;
}
//lwIP tcp_recv()函数的回调函数
err_t tcp_server_recv(void *arg, struct tcp_pcb *tpcb, struct pbuf *p, err_t err)
{
	err_t ret_err;
	u32 data_len = 0;
	int cmd_type_tmp = 0x00;
	int i = 0;
	
	// int index = 0;//added by wly
	// int j = 0;//added by wly
	struct pbuf *q;
	struct tcp_server_struct *es;
//	struct tcp_server_struct *ret_es;
	LWIP_ASSERT("arg != NULL",arg != NULL);
	es=(struct tcp_server_struct *)arg;
	if(p==NULL) //从客户端接收到空数据
	{
		es->state=ES_TCPSERVER_CLOSING;//需要关闭TCP 连接了
		es->p=p; 
		ret_err=ERR_OK;
	}else if(err!=ERR_OK)	//从客户端接收到一个非空数据,但是由于某种原因err!=ERR_OK
	{
		if(p)pbuf_free(p);	//释放接收pbuf
		ret_err=err;
	}else if(es->state==ES_TCPSERVER_ACCEPTED) 	//处于连接状态
	{
		if(p!=NULL)  //当处于连接状态并且接收到的数据不为空时将其打印出来
		{
			memset(tcp_server_recvbuf,0,TCP_SERVER_RX_BUFSIZE);  //数据接收缓冲区清零
			for(q=p;q!=NULL;q=q->next)  //遍历完整个pbuf链表
			{
				//判断要拷贝到TCP_SERVER_RX_BUFSIZE中的数据是否大于TCP_SERVER_RX_BUFSIZE的剩余空间，如果大于
				//的话就只拷贝TCP_SERVER_RX_BUFSIZE中剩余长度的数据，否则的话就拷贝所有的数据
				if(q->len > (TCP_SERVER_RX_BUFSIZE-data_len)) memcpy(tcp_server_recvbuf+data_len,q->payload,(TCP_SERVER_RX_BUFSIZE-data_len));//拷贝数据
				else memcpy(tcp_server_recvbuf+data_len,q->payload,q->len);
				data_len += q->len;  	
				if(data_len > TCP_SERVER_RX_BUFSIZE) break; //超出TCP客户端接收数组,跳出	
			}
			///// print buf 
			printf("state=%d\r\n", state);
		  printf("recv buf %d:\r\n", data_len);
			for (i=0;i<data_len;i++) {
				printf("0x%x ", tcp_server_recvbuf[i]);
			}
			printf("\r\n");
			//////end print
			
			cmd_type_tmp = tcp_server_recvbuf[0];
			if (cmd_type_tmp == 0x03 ) {
			// 终止正在执行的任务
				state = 0;
				frame.cmd_type = 0x00;
			} else if ( state == 0 ) {
				// 解析数据，只有当主任务状态为idle时，才会解析数据，否则无视上位机发送的数据
				if ( cmd_type_tmp == 0x01 ) { //单点发送，解析位置数据
					frame.cmd_type = cmd_type_tmp;
					for ( i = 0 ; i < 6; i ++) {
						frame.pos[i][0] = tcp_server_recvbuf[1 + i*4];
						frame.pos[i][1] = tcp_server_recvbuf[2 + i*4];						
						frame.pos[i][2] = tcp_server_recvbuf[3 + i*4];
						frame.pos[i][3] = tcp_server_recvbuf[4 + i*4];
					}
					frame.vel[0] = tcp_server_recvbuf[25];
					frame.vel[1] = tcp_server_recvbuf[26];
				}
				if ( cmd_type_tmp == 0x02 ) { // 连续发送，解析三角函数参数
					frame.cmd_type = cmd_type_tmp;
					for ( i = 0 ; i < 6 ; i ++ ) {
						memcpy(&frame.params[i].enable, tcp_server_recvbuf + 1  + i * 13, 1);
						memcpy(&frame.params[i].ap    , tcp_server_recvbuf + 2  + i * 13, 4);
						memcpy(&frame.params[i].fr    , tcp_server_recvbuf + 6  + i * 13, 4);
						memcpy(&frame.params[i].pha   , tcp_server_recvbuf + 10 + i * 13, 4);
					}
					memcpy(&frame.cnt, tcp_server_recvbuf + 79, 4);
					memcpy(&frame.z0 , tcp_server_recvbuf + 83, 4);
					//frame.time /= 1000.0;
					// printf frame data
					
					printf("frame data:\r\n");
					for ( i = 0 ; i < 6; i ++ ) {
						printf("(%d): ", i );
						printf("ap: %f\t", frame.params[i].ap);
						printf("fr: %f\t", frame.params[i].fr);
						printf("pha: %f\r\n", frame.params[i].pha);
						
					}
					printf("loop cnt: %d\r\n", frame.cnt);
				}
				if ( cmd_type_tmp == 0x04) { // 平台复位
					frame.cmd_type = cmd_type_tmp;
				}
			}
				if ( cmd_type_tmp == 0x05) { // 请求下位机数据
					//frame.cmd_type = cmd_type_tmp;
					es->p=pbuf_alloc(PBUF_TRANSPORT,24,PBUF_POOL);//申请内存
//					printf("send data: \r\n");
//					for(j=0; j<strlen((char*)tcp_rsp_buf);j++){
//						printf("0x%x,",tcp_rsp_buf[j]);
//					}printf("\r\n");
//					printf("[tcp]send data response: %s size:%d.\r\n", tcp_rsp_buf, 24);
					//pbuf_take(es->p,(char*)tcp_server_sendbuf,strlen((char*)tcp_server_sendbuf));
					pbuf_take(es->p,(char*)tcp_rsp_buf,24);
					
					tcp_server_senddata(tpcb,es); 		//轮询的时候发送要发送的数据
					//tcp_server_flag&=~(1<<7);  			//清除数据发送标志位
					//tcp_server_flag|=1<<6;
					if(es->p!=NULL)pbuf_free(es->p); 	//释放内存	
				}
				if ( cmd_type_tmp == 0x06) { // 请求下位机数据
					//frame.cmd_type = cmd_type_tmp;
					int j;
					es->p=pbuf_alloc(PBUF_TRANSPORT,24,PBUF_POOL);//申请内存
					printf("ori leg data: \r\n");
					for(j=0; j<24;j++){
						printf("0x%x,",ori_pos_buf[j]);
					}printf("\r\n");
					//printf("send data response: %s size:%d.\r\n", tcp_rsp_buf, strlen((char*)tcp_rsp_buf));
					//pbuf_take(es->p,(char*)tcp_server_sendbuf,strlen((char*)tcp_server_sendbuf));
					pbuf_take(es->p,(char*)ori_pos_buf,24);

					tcp_server_senddata(tpcb,es); 		//轮询的时候发送要发送的数据
					//tcp_server_flag&=~(1<<7);  			//清除数据发送标志位
					//tcp_server_flag|=1<<6;
					if(es->p!=NULL)pbuf_free(es->p); 	//释放内存	
				}
			
			
			tcp_server_flag|=1<<7;	//标记接收到数据了
			lwipdev.remoteip[0]=tpcb->remote_ip.addr&0xff; 		//IADDR4
			lwipdev.remoteip[1]=(tpcb->remote_ip.addr>>8)&0xff; //IADDR3
			lwipdev.remoteip[2]=(tpcb->remote_ip.addr>>16)&0xff;//IADDR2
			lwipdev.remoteip[3]=(tpcb->remote_ip.addr>>24)&0xff;//IADDR1 
 			tcp_recved(tpcb,p->tot_len);//用于获取接收数据,通知LWIP可以获取更多数据
			pbuf_free(p);  	//释放内存
			ret_err=ERR_OK;
		}
	}else//服务器关闭了
	{
		tcp_recved(tpcb,p->tot_len);//用于获取接收数据,通知LWIP可以获取更多数据
		es->p=NULL;
		pbuf_free(p); //释放内存
		ret_err=ERR_OK;
	}
	return ret_err;
}
//lwIP tcp_err函数的回调函数
void tcp_server_error(void *arg,err_t err)
{  
	LWIP_UNUSED_ARG(err);  
	printf("tcp error:%x\r\n",(u32)arg);
	if(arg!=NULL)mem_free(arg);//释放内存
} 
//lwIP tcp_poll的回调函数
err_t tcp_server_poll(void *arg, struct tcp_pcb *tpcb)
{
//	int index; 				
//	CanRxMsg RxMessage;
//	int i=0, j=0, cnt=0;
	int j = 0;
	err_t ret_err;
	struct tcp_server_struct *es; 
	es=(struct tcp_server_struct *)arg; 

	if(es!=NULL)
	{
		//if(tcp_server_flag&(1<<7))	//判断是否有数据要发送
		if ( rsp_tcp_flag == 1)//判断是否有数据要发送
		{
			
		}else if(es->state==ES_TCPSERVER_CLOSING)//需要关闭连接?执行关闭操作
		{
			tcp_server_connection_close(tpcb,es);//关闭连接
		}
		ret_err=ERR_OK;
	}else
	{
		tcp_abort(tpcb);//终止连接,删除pcb控制块
		ret_err=ERR_ABRT; 
	}
	return ret_err;
} 
//lwIP tcp_sent的回调函数(当从远端主机接收到ACK信号后发送数据)
err_t tcp_server_sent(void *arg, struct tcp_pcb *tpcb, u16_t len)
{
	struct tcp_server_struct *es;
	LWIP_UNUSED_ARG(len); 
	es = (struct tcp_server_struct *) arg;
	if(es->p)tcp_server_senddata(tpcb,es);//发送数据
	return ERR_OK;
} 
//此函数用来发送数据
void tcp_server_senddata(struct tcp_pcb *tpcb, struct tcp_server_struct *es)
{
	struct pbuf *ptr;
	u16 plen;
	err_t wr_err=ERR_OK;
	 while((wr_err==ERR_OK)&&es->p&&(es->p->len<=tcp_sndbuf(tpcb)))
	 {
		ptr=es->p;
		wr_err=tcp_write(tpcb,ptr->payload,ptr->len,1); //将要发送的数据加入发送缓冲队列中
		if(wr_err==ERR_OK)
		{ 
			plen=ptr->len;
			es->p=ptr->next;			//指向下一个pbuf
			if(es->p)pbuf_ref(es->p);	//pbuf的ref加一
			pbuf_free(ptr);
			tcp_recved(tpcb,plen); 		//更新tcp窗口大小
		}else if(wr_err==ERR_MEM)es->p=ptr;
		tcp_output(tpcb);   //将发送缓冲队列中的数据发送出去
	 }
} 
//关闭tcp连接
void tcp_server_connection_close(struct tcp_pcb *tpcb, struct tcp_server_struct *es)
{
	tcp_close(tpcb);
	tcp_arg(tpcb,NULL);
	tcp_sent(tpcb,NULL);
	tcp_recv(tpcb,NULL);
	tcp_err(tpcb,NULL);
	tcp_poll(tpcb,NULL,0);
	if(es)mem_free(es); 
	tcp_server_flag&=~(1<<5);//标记连接断开了
}
extern void tcp_pcb_purge(struct tcp_pcb *pcb);	//在 tcp.c里面 
extern struct tcp_pcb *tcp_active_pcbs;			//在 tcp.c里面 
extern struct tcp_pcb *tcp_tw_pcbs;				//在 tcp.c里面  
//强制删除TCP Server主动断开时的time wait
void tcp_server_remove_timewait(void)
{
	struct tcp_pcb *pcb,*pcb2; 
	while(tcp_active_pcbs!=NULL)
	{
		lwip_periodic_handle();//继续轮询
		delay_ms(10);//等待tcp_active_pcbs为空  
	}
	pcb=tcp_tw_pcbs;
	while(pcb!=NULL)//如果有等待状态的pcbs
	{
		tcp_pcb_purge(pcb); 
		tcp_tw_pcbs=pcb->next;
		pcb2=pcb;
		pcb=pcb->next;
		memp_free(MEMP_TCP_PCB,pcb2);	
	}
}



































