
#python3.8.0 64位（python 32位要用32位的DLL）
#
from ctypes import *
 
VCI_USBCAN2 = 4
STATUS_OK = 1

ubyte_array = c_ubyte*8
ubyte_3array = c_ubyte*3

class VCI_INIT_CONFIG(Structure):  
    _fields_ = [("AccCode", c_uint),
                ("AccMask", c_uint),
                ("Reserved", c_uint),
                ("Filter", c_ubyte),
                ("Timing0", c_ubyte),
                ("Timing1", c_ubyte),
                ("Mode", c_ubyte)
                ]  
class VCI_CAN_OBJ(Structure):  
    _fields_ = [("ID", c_uint),
                ("TimeStamp", c_uint),
                ("TimeFlag", c_ubyte),
                ("SendType", c_ubyte),
                ("RemoteFlag", c_ubyte),
                ("ExternFlag", c_ubyte),
                ("DataLen", c_ubyte),
                ("Data", c_ubyte*8),
                ("Reserved", c_ubyte*3)
                ] 
 
class CanDriver():
    def __init__(self, lib_dir="./lib/ControlCAN.dll"):
        print("can dll dir: " + lib_dir)
        self.canDLL_ = windll.LoadLibrary(lib_dir)
        #Linux系统下使用下面语句，编译命令：python3 python3.8.0.py
        #canDLL = cdll.LoadLibrary('./libcontrolcan.so')
        ret = self.canDLL_.VCI_OpenDevice(VCI_USBCAN2, 0, 0)
        if ret == STATUS_OK:
            print('调用 VCI_OpenDevice成功\r\n')
        if ret != STATUS_OK:
            print('调用 VCI_OpenDevice出错\r\n')
        #初始0通道
        # vci_initconfig = VCI_INIT_CONFIG(0x80000008, 0xFFFFFFFF, 0,
        #                                  0, 0x03, 0x1C, 0)#波特率125k，正常模式
        vci_initconfig = VCI_INIT_CONFIG(0x80000008, 0xFFFFFFFF, 0,
                                         0, 0x00, 0x14, 0)#波特率1000k，正常模式
        ret = self.canDLL_.VCI_InitCAN(VCI_USBCAN2, 0, 0, byref(vci_initconfig))
        if ret == STATUS_OK:
            print('调用 VCI_InitCAN1成功\r\n')
        if ret != STATUS_OK:
            print('调用 VCI_InitCAN1出错\r\n')
         
        ret = self.canDLL_.VCI_StartCAN(VCI_USBCAN2, 0, 0)
        if ret == STATUS_OK:
            print('调用 VCI_StartCAN1成功\r\n')
        if ret != STATUS_OK:
            print('调用 VCI_StartCAN1出错\r\n')

    def __del__(self):
        if self.canDLL_ != None:
            #关闭
            self.canDLL_.VCI_CloseDevice(VCI_USBCAN2, 0) 

    def send(self, node_id, data):
        if self.canDLL_ == None:
            print("can driver ptr is null!")
            return

        a = ubyte_array(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])

        vci_can_obj = VCI_CAN_OBJ(node_id, 0, 0, 1, 0, 0,  8, a, ubyte_3array(0, 0, 0)) #单次发送
     
        ret = self.canDLL_.VCI_Transmit(VCI_USBCAN2, 0, 0, byref(vci_can_obj), 1)
        # if ret == STATUS_OK:
        #     print('CAN1通道发送成功\r\n')
        # if ret != STATUS_OK:
        #     print('CAN1通道发送失败\r\n')
        if ret == STATUS_OK:
            return True
        else:
            return False

    def receive(self):
        if self.canDLL_ == None:
            print("can driver ptr is null!")
            return

        ret = self.canDLL_.VCI_Receive(VCI_USBCAN2, 0, 0, byref(vci_can_obj), 2500, 0)
        if ret > 0:#接收到一帧数据
            print('CAN1通道接收成功\r\n')
            print('ID：')
            print(vci_can_obj.ID)
            print('DataLen：')
            print(vci_can_obj.DataLen)
            print('Data：')
            print(list(vci_can_obj.Data))


if __name__ == "__main__":
    can_driver = CanDriver()
    # data = [0x01 ,0x05 ,0xB0 ,0x8F ,0x06 ,0x00 ,0xA0 ,0x00] # 运动到中位 430000pulse
    # data = [0x00 ,0x12 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00 ,0x00] # 查询回零状态
    data = [0x01 ,0x05 ,0x40 ,0x9C ,0x00 ,0x00 ,0xDC ,0x05] # 运动到零位 40000pulse
    node_id = 0x601 # axis1: 0x601; axis2: 0x602; ...
    can_driver.send(node_id, data)     