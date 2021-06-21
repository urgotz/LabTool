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
//������ֻ��ѧϰʹ�ã�δ��������ɣ��������������κ���;
//ALIENTEK STM32F407������
//TCP Server ���Դ���	   
//����ԭ��@ALIENTEK
//������̳:www.openedv.com
//��������:2014/8/15
//�汾��V1.0
//��Ȩ���У�����ؾ���
//Copyright(C) ������������ӿƼ����޹�˾ 2009-2019
//All rights reserved									  
//*******************************************************************************
//�޸���Ϣ
//��
////////////////////////////////////////////////////////////////////////////////// 	   
 
//TCP Server�������ݻ�����
u8 tcp_server_recvbuf[TCP_SERVER_RX_BUFSIZE];	
//TCP������������������
const u8 *tcp_server_sendbuf="Explorer STM32F407 TCP Server send data\r\n";

//TCP Server ����ȫ��״̬��Ǳ���
//bit7:0,û������Ҫ����;1,������Ҫ����
//bit6:0,û���յ�����;1,�յ�������.
//bit5:0,û�пͻ���������;1,�пͻ�����������.
//bit4~0:����
u8 tcp_server_flag;	 


extern data_frame_t frame;
extern u8 state;

/////////////
 
//TCP Server ����
void tcp_server_test(void)
{
	err_t err;  
	struct tcp_pcb *tcppcbnew;  	//����һ��TCP���������ƿ�
	struct tcp_pcb *tcppcbconn;  	//����һ��TCP���������ƿ�
	
	u8 *tbuf;
 	u8 key;
	u8 res=0;		
	u8 t=0; 
	u8 connflag=0;		//���ӱ��
	
//	int i = 0; //added by wly
	
	LCD_Clear(WHITE);	//����
	POINT_COLOR=RED; 	//��ɫ����
	LCD_ShowString(30,30,200,16,16,"Explorer STM32F4");
	LCD_ShowString(30,50,200,16,16,"TCP Server Test");
	LCD_ShowString(30,70,200,16,16,"ATOM@ALIENTEK");  
	LCD_ShowString(30,90,200,16,16,"KEY0:Send data");  
	LCD_ShowString(30,110,200,16,16,"KEY_UP:Quit");  
	tbuf=mymalloc(SRAMIN,200);	//�����ڴ�
	if(tbuf==NULL)return ;		//�ڴ�����ʧ����,ֱ���˳�
	sprintf((char*)tbuf,"Server IP:%d.%d.%d.%d",lwipdev.ip[0],lwipdev.ip[1],lwipdev.ip[2],lwipdev.ip[3]);//������IP
	printf("%s\r\n", (char*)tbuf);
	LCD_ShowString(30,130,210,16,16,tbuf);  
	sprintf((char*)tbuf,"Server Port:%d",TCP_SERVER_PORT);//�������˿ں�
	LCD_ShowString(30,150,210,16,16,tbuf); 
	tcppcbnew=tcp_new();	//����һ���µ�pcb
	if(tcppcbnew)			//�����ɹ�
	{ 
		err=tcp_bind(tcppcbnew,IP_ADDR_ANY,TCP_SERVER_PORT);	//������IP��ָ���Ķ˿ںŰ���һ��,IP_ADDR_ANYΪ�󶨱������е�IP��ַ
		if(err==ERR_OK)	//�����
		{
			tcppcbconn=tcp_listen(tcppcbnew); 			//����tcppcb�������״̬
			tcp_accept(tcppcbconn,tcp_server_accept); 	//��ʼ��LWIP��tcp_accept�Ļص�����
		}else res=1;  
	}else res=1;
	POINT_COLOR=BLUE;//��ɫ����
	while(res==0)
	{
		key=KEY_Scan(0);
		if(key==WKUP_PRES)break;
		if(key==KEY0_PRES)//KEY0������,��������
		{
			tcp_server_flag|=1<<7;//���Ҫ��������
		}
		if(tcp_server_flag&1<<6)//�Ƿ��յ�����?
		{
			LCD_Fill(30,210,lcddev.width-1,lcddev.height-1,WHITE);//����һ������
			LCD_ShowString(30,210,lcddev.width-30,lcddev.height-210,16,tcp_server_recvbuf);//��ʾ���յ�������			
			//printf("recv data:%s\r\n", tcp_server_recvbuf);
			//printf("recv data:\r\n");
			//for(i = 0 ; i < TCP_SERVER_RX_BUFSIZE; i++){
			//	printf("0x%x ", tcp_server_recvbuf[i]);
			//}
			//printf("\r\n");
			
			tcp_server_flag&=~(1<<6);//��������Ѿ���������.
		}
		if(tcp_server_flag&1<<5)//�Ƿ�������?
		{
			if(connflag==0)
			{ 
				sprintf((char*)tbuf,"Client IP:%d.%d.%d.%d",lwipdev.remoteip[0],lwipdev.remoteip[1],lwipdev.remoteip[2],lwipdev.remoteip[3]);//�ͻ���IP
 				LCD_ShowString(30,170,230,16,16,tbuf);
				POINT_COLOR=RED;
				LCD_ShowString(30,190,lcddev.width-30,lcddev.height-190,16,"Receive Data:");//��ʾ��Ϣ		
				POINT_COLOR=BLUE;//��ɫ����
				connflag=1;//���������
			} 
		}else if(connflag)
		{
			LCD_Fill(30,170,lcddev.width-1,lcddev.height-1,WHITE);//����
			connflag=0;	//������ӶϿ���
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
	tcp_server_connection_close(tcppcbnew,0);//�ر�TCP Server����
	tcp_server_connection_close(tcppcbconn,0);//�ر�TCP Server���� 
	tcp_server_remove_timewait(); 
	memset(tcppcbnew,0,sizeof(struct tcp_pcb));
	memset(tcppcbconn,0,sizeof(struct tcp_pcb)); 
	myfree(SRAMIN,tbuf);
} 
//lwIP tcp_accept()�Ļص�����
err_t tcp_server_accept(void *arg,struct tcp_pcb *newpcb,err_t err)
{
	err_t ret_err;
	struct tcp_server_struct *es; 
 	LWIP_UNUSED_ARG(arg);
	LWIP_UNUSED_ARG(err);
	tcp_setprio(newpcb,TCP_PRIO_MIN);//�����´�����pcb���ȼ�
	es=(struct tcp_server_struct*)mem_malloc(sizeof(struct tcp_server_struct)); //�����ڴ�
 	if(es!=NULL) //�ڴ����ɹ�
	{
		es->state=ES_TCPSERVER_ACCEPTED;  	//��������
		es->pcb=newpcb;
		es->p=NULL;
		
		tcp_arg(newpcb,es);
		tcp_recv(newpcb,tcp_server_recv);	//��ʼ��tcp_recv()�Ļص�����
		tcp_err(newpcb,tcp_server_error); 	//��ʼ��tcp_err()�ص�����
		tcp_poll(newpcb,tcp_server_poll,1);	//��ʼ��tcp_poll�ص�����
		tcp_sent(newpcb,tcp_server_sent);  	//��ʼ�����ͻص�����
		  
		tcp_server_flag|=1<<5;				//����пͻ���������
		lwipdev.remoteip[0]=newpcb->remote_ip.addr&0xff; 		//IADDR4
		lwipdev.remoteip[1]=(newpcb->remote_ip.addr>>8)&0xff;  	//IADDR3
		lwipdev.remoteip[2]=(newpcb->remote_ip.addr>>16)&0xff; 	//IADDR2
		lwipdev.remoteip[3]=(newpcb->remote_ip.addr>>24)&0xff; 	//IADDR1 
		ret_err=ERR_OK;
	}else ret_err=ERR_MEM;
	return ret_err;
}
//lwIP tcp_recv()�����Ļص�����
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
	//struct tcp_server_struct *ret_es;
	LWIP_ASSERT("arg != NULL",arg != NULL);
	es=(struct tcp_server_struct *)arg;
	if(p==NULL) //�ӿͻ��˽��յ�������
	{
		es->state=ES_TCPSERVER_CLOSING;//��Ҫ�ر�TCP ������
		es->p=p; 
		ret_err=ERR_OK;
	}else if(err!=ERR_OK)	//�ӿͻ��˽��յ�һ���ǿ�����,��������ĳ��ԭ��err!=ERR_OK
	{
		if(p)pbuf_free(p);	//�ͷŽ���pbuf
		ret_err=err;
	}else if(es->state==ES_TCPSERVER_ACCEPTED) 	//��������״̬
	{
		if(p!=NULL)  //����������״̬���ҽ��յ������ݲ�Ϊ��ʱ�����ӡ����
		{
			memset(tcp_server_recvbuf,0,TCP_SERVER_RX_BUFSIZE);  //���ݽ��ջ���������
			for(q=p;q!=NULL;q=q->next)  //����������pbuf����
			{
				//�ж�Ҫ������TCP_SERVER_RX_BUFSIZE�е������Ƿ����TCP_SERVER_RX_BUFSIZE��ʣ��ռ䣬�������
				//�Ļ���ֻ����TCP_SERVER_RX_BUFSIZE��ʣ�೤�ȵ����ݣ�����Ļ��Ϳ������е�����
				if(q->len > (TCP_SERVER_RX_BUFSIZE-data_len)) memcpy(tcp_server_recvbuf+data_len,q->payload,(TCP_SERVER_RX_BUFSIZE-data_len));//��������
				else memcpy(tcp_server_recvbuf+data_len,q->payload,q->len);
				data_len += q->len;  	
				if(data_len > TCP_SERVER_RX_BUFSIZE) break; //����TCP�ͻ��˽�������,����	
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
			// ��ֹ����ִ�е�����
				state = 0;
				frame.cmd_type = 0x00;
			} else if ( state == 0 ) {
				// �������ݣ�ֻ�е�������״̬Ϊidleʱ���Ż�������ݣ�����������λ�����͵�����
				if ( cmd_type_tmp == 0x01 ) { //���㷢�ͣ�����λ������
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
				if ( cmd_type_tmp == 0x02 ) { // �������ͣ��������Ǻ�������
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
				if ( cmd_type_tmp == 0x04) { // ƽ̨��λ
					frame.cmd_type = cmd_type_tmp;
				}
			}
			
			//ret_es = (struct tcp_server_struct *) arg;
			//if(ret_es->p)tcp_server_senddata(tpcb,ret_es);//��������
			/*
			for ( index = 0 ; index < 6; index ++) {
				printf("fucking index:%d\r\n",index);
				
				TxMessage.StdId = 0x0601 + index;
				
				printf("fucking StdId:%d\r\n",TxMessage.StdId);
				//TxMessage.ExtId = 0x03;
				//TxMessage.IDE = CAN_ID_EXT;
				//TxMessage.RTR = CAN_RTR_DATA;
				
				TxMessage.ExtId=0x12;	 // ������չ��ʾ����29λ��
				TxMessage.IDE=0;		  // ʹ����չ��ʶ��
				TxMessage.RTR=0;		  // ��Ϣ����Ϊ����֡��һ֡8λ
				
				TxMessage.DLC = 8;
				TxMessage.Data[7] = 0x05;
				TxMessage.Data[6] = 0xdc;
				TxMessage.Data[5] = tcp_server_recvbuf[3 + index*4];
				TxMessage.Data[4] = tcp_server_recvbuf[2 + index*4];
				TxMessage.Data[3] = tcp_server_recvbuf[1 + index*4];
				TxMessage.Data[2] = tcp_server_recvbuf[0 + index*4];
				TxMessage.Data[1] = 0x05;
				TxMessage.Data[0] = 0x01;
				for( j = 0; j <8 ; j ++) {
					printf("0x%x ", TxMessage.Data[j]);
				}
				CAN_Transmit(CAN1, &TxMessage);  
				//CAN1_Send_Msg(TxMessage.Data,8);
			}
			*/
			tcp_server_flag|=1<<7;	//��ǽ��յ�������
			lwipdev.remoteip[0]=tpcb->remote_ip.addr&0xff; 		//IADDR4
			lwipdev.remoteip[1]=(tpcb->remote_ip.addr>>8)&0xff; //IADDR3
			lwipdev.remoteip[2]=(tpcb->remote_ip.addr>>16)&0xff;//IADDR2
			lwipdev.remoteip[3]=(tpcb->remote_ip.addr>>24)&0xff;//IADDR1 
 			tcp_recved(tpcb,p->tot_len);//���ڻ�ȡ��������,֪ͨLWIP���Ի�ȡ��������
			pbuf_free(p);  	//�ͷ��ڴ�
			ret_err=ERR_OK;
		}
	}else//�������ر���
	{
		tcp_recved(tpcb,p->tot_len);//���ڻ�ȡ��������,֪ͨLWIP���Ի�ȡ��������
		es->p=NULL;
		pbuf_free(p); //�ͷ��ڴ�
		ret_err=ERR_OK;
	}
	return ret_err;
}
//lwIP tcp_err�����Ļص�����
void tcp_server_error(void *arg,err_t err)
{  
	LWIP_UNUSED_ARG(err);  
	printf("tcp error:%x\r\n",(u32)arg);
	if(arg!=NULL)mem_free(arg);//�ͷ��ڴ�
} 
//lwIP tcp_poll�Ļص�����
err_t tcp_server_poll(void *arg, struct tcp_pcb *tpcb)
{
	err_t ret_err;
	struct tcp_server_struct *es; 
	es=(struct tcp_server_struct *)arg; 
	if(es!=NULL)
	{
		if(tcp_server_flag&(1<<7))	//�ж��Ƿ�������Ҫ����
		{
			es->p=pbuf_alloc(PBUF_TRANSPORT,strlen((char*)tcp_server_sendbuf),PBUF_POOL);//�����ڴ�
			pbuf_take(es->p,(char*)tcp_server_sendbuf,strlen((char*)tcp_server_sendbuf));
			tcp_server_senddata(tpcb,es); 		//��ѯ��ʱ����Ҫ���͵�����
			tcp_server_flag&=~(1<<7);  			//������ݷ��ͱ�־λ
			tcp_server_flag|=1<<6;
			if(es->p!=NULL)pbuf_free(es->p); 	//�ͷ��ڴ�	
		}else if(es->state==ES_TCPSERVER_CLOSING)//��Ҫ�ر�����?ִ�йرղ���
		{
			tcp_server_connection_close(tpcb,es);//�ر�����
		}
		ret_err=ERR_OK;
	}else
	{
		tcp_abort(tpcb);//��ֹ����,ɾ��pcb���ƿ�
		ret_err=ERR_ABRT; 
	}
	return ret_err;
} 
//lwIP tcp_sent�Ļص�����(����Զ���������յ�ACK�źź�������)
err_t tcp_server_sent(void *arg, struct tcp_pcb *tpcb, u16_t len)
{
	struct tcp_server_struct *es;
	LWIP_UNUSED_ARG(len); 
	es = (struct tcp_server_struct *) arg;
	if(es->p)tcp_server_senddata(tpcb,es);//��������
	return ERR_OK;
} 
//�˺���������������
void tcp_server_senddata(struct tcp_pcb *tpcb, struct tcp_server_struct *es)
{
	struct pbuf *ptr;
	u16 plen;
	err_t wr_err=ERR_OK;
	 while((wr_err==ERR_OK)&&es->p&&(es->p->len<=tcp_sndbuf(tpcb)))
	 {
		ptr=es->p;
		wr_err=tcp_write(tpcb,ptr->payload,ptr->len,1); //��Ҫ���͵����ݼ��뷢�ͻ��������
		if(wr_err==ERR_OK)
		{ 
			plen=ptr->len;
			es->p=ptr->next;			//ָ����һ��pbuf
			if(es->p)pbuf_ref(es->p);	//pbuf��ref��һ
			pbuf_free(ptr);
			tcp_recved(tpcb,plen); 		//����tcp���ڴ�С
		}else if(wr_err==ERR_MEM)es->p=ptr;
		tcp_output(tpcb);   //�����ͻ�������е����ݷ��ͳ�ȥ
	 }
} 
//�ر�tcp����
void tcp_server_connection_close(struct tcp_pcb *tpcb, struct tcp_server_struct *es)
{
	tcp_close(tpcb);
	tcp_arg(tpcb,NULL);
	tcp_sent(tpcb,NULL);
	tcp_recv(tpcb,NULL);
	tcp_err(tpcb,NULL);
	tcp_poll(tpcb,NULL,0);
	if(es)mem_free(es); 
	tcp_server_flag&=~(1<<5);//������ӶϿ���
}
extern void tcp_pcb_purge(struct tcp_pcb *pcb);	//�� tcp.c���� 
extern struct tcp_pcb *tcp_active_pcbs;			//�� tcp.c���� 
extern struct tcp_pcb *tcp_tw_pcbs;				//�� tcp.c����  
//ǿ��ɾ��TCP Server�����Ͽ�ʱ��time wait
void tcp_server_remove_timewait(void)
{
	struct tcp_pcb *pcb,*pcb2; 
	while(tcp_active_pcbs!=NULL)
	{
		lwip_periodic_handle();//������ѯ
		delay_ms(10);//�ȴ�tcp_active_pcbsΪ��  
	}
	pcb=tcp_tw_pcbs;
	while(pcb!=NULL)//����еȴ�״̬��pcbs
	{
		tcp_pcb_purge(pcb); 
		tcp_tw_pcbs=pcb->next;
		pcb2=pcb;
		pcb=pcb->next;
		memp_free(MEMP_TCP_PCB,pcb2);	
	}
}



































