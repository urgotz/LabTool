# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMessageBox, QMainWindow, QAction,\
                            QSlider, QStyleOptionSlider, QStyle, QFormLayout
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon


import sys
import MainWindow
import traceback
import socket
import numpy as np
import math
import time

from protocol_convert import *
import csv
import datetime
MIN_ANGLE = -30.0
MAX_ANGLE = 30.0
MIN_DISP = -100.0
MAX_DISP = 100.0




# global s
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# target_addr = ('127.0.0.1', 9800)
class DataPool():
    def __init__(self):
        self.send_data_roll = 0
        self.send_data_pitch = 0
        self.send_data_yaw = 0
        self.send_data_x = 0
        self.send_data_y = 0
        self.send_data_z = 0

    def refreshSendData(self, data):
        self.send_data_roll = data[0]
        self.send_data_pitch = data[1]
        self.send_data_yaw = data[2]
        self.send_data_x = data[3]
        self.send_data_y = data[4]
        self.send_data_z = data[5]

 
class MainProgram(QWidget):
    def __init__(self): 
        app = 0
        app = QtWidgets.QApplication(sys.argv)
        super().__init__()  

        MainProgram = QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(MainProgram)
        MainProgram.setWindowTitle("Stewart Upper Computer")
        MainProgram.setWindowIcon(QIcon('Icon.png'))
        self.ui.logo_label.setPixmap(QtGui.QPixmap('Logo.png').scaled(300, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))

        self.data = DataPool()

        self.initUI()
        
        self.send_cont_motion_thrd = None
        self.req_data_thrd = None
        self.path = 'test'
        self.pc = ProtoConvt()
        if self.pc.init_protocol() != 0:
            QMessageBox.critical(self, '错误', '网络连接失败！请检查硬件或IP配置')
            exit()

        self.menu = MainProgram.menuBar()   
        self.menu_config = self.menu.addMenu('&配置') 

        self.reset_platform = QAction('平台重置', self)
        self.menu_config.addAction(self.reset_platform)
        self.reset_platform.triggered.connect(self.reset_platform_func)

        self.reconnect = QAction('网络重连', self)
        self.menu_config.addAction(self.reconnect)
        self.reconnect.triggered.connect(self.socket_reconnect_func)
        self.start_req_data_thrd()
        MainProgram.show()
        sys.exit(app.exec_())


    def initSlider(self, slider, line_edit, init_value, min_value, max_value):
        len_of_slider = max_value - min_value
        line_edit.setValidator(QtGui.QDoubleValidator())
        slider.setMinimum(0)
        slider.setMaximum(65535)
        slider.setValue(int((init_value-min_value)/len_of_slider*65535))
        line_edit.setText(str(init_value))
        slider.valueChanged.connect(lambda v: line_edit.setText(str(round(v/65535*len_of_slider+min_value,2))))
        line_edit.editingFinished.connect(lambda : slider.setValue(int((float(line_edit.text())-min_value)/len_of_slider*65535)))

    def init_all_sliders(self):
        self.initSlider(self.ui.slider_roll, self.ui.line_edit_roll, 0, MIN_ANGLE, MAX_ANGLE)
        self.initSlider(self.ui.slider_pitch, self.ui.line_edit_pitch, 0, MIN_ANGLE, MAX_ANGLE)
        self.initSlider(self.ui.slider_yaw, self.ui.line_edit_yaw, 0, MIN_ANGLE, MAX_ANGLE)
        self.initSlider(self.ui.slider_x, self.ui.line_edit_x, 0, MIN_DISP, MAX_DISP)
        self.initSlider(self.ui.slider_y, self.ui.line_edit_y, 0, MIN_DISP, MAX_DISP)
        self.initSlider(self.ui.slider_z, self.ui.line_edit_z, self.ui.spinBox_z0.value(), self.ui.spinBox_z0.value()+MIN_DISP, self.ui.spinBox_z0.value()+MAX_DISP)

    def initUI(self):
        self.init_all_sliders()
        self.ui.btn_send.clicked.connect(self.btn_send_clicked)
        self.ui.btn_clear.clicked.connect(self.init_all_sliders)
        self.ui.pushButton_continuous_motion.clicked.connect(self.btn_continuous_motion_clicked)
        self.ui.pushButton_cont_motion_stop.clicked.connect(self.btn_cont_motion_stop_clicked)
        self.ui.pushButton_reset.clicked.connect(self.btn_reset_clicked)
        self.ui.save_data.clicked.connect(self.save_data_clicked)

    def save_data_clicked(self):
        if self.ui.save_data.isChecked():

            filename = str( datetime.datetime.now() )
            self.path = 'savedata' + ''.join(e for e in filename if e.isalnum()) +'.csv'
            with open(self.path,'w') as f:
                csv_write = csv.writer(f)
                csv_head = ["No.","leg1","leg2","leg3","leg4","leg5","leg6"]
                csv_write.writerow(csv_head)
            self.req_data_thrd.start_get_data()

        else:
            with open(self.path,'a+') as f:
                csv_write = csv.writer(f)
                i = 0
                for row in  self.req_data_thrd.get_data():
                    row.insert(0, i)
                    i += 1
                    csv_write.writerow(row)
                self.req_data_thrd.finish_get_data()

    def btn_reset_clicked(self):
        # move platform to middle position
        tmp = self.ui.spinBox_leg_vel.value()
        self.ui.spinBox_leg_vel.setValue(1000)
        self.init_all_sliders()
        self.btn_send_clicked()
        self.ui.spinBox_leg_vel.setValue(tmp)

    def reset_platform_func(self):
        # send reset comand
        self.pc.send_reset_cmd()
    def socket_reconnect_func(self):
        self.pc.init_protocol()
        self.start_req_data_thrd()

    def start_req_data_thrd(self):
        if self.req_data_thrd == None or self.req_data_thrd.is_finished_:
            self.req_data_thrd = ThreadRefreshData(self.pc, self.ui)
            self.req_data_thrd.start()

    def getAllSendData(self):
        data = list()
        data.append(float(self.ui.line_edit_roll.text()))
        data.append(float(self.ui.line_edit_pitch.text()))
        data.append(float(self.ui.line_edit_yaw.text()))
        data.append(float(self.ui.line_edit_x.text()))
        data.append(float(self.ui.line_edit_y.text()))
        data.append(float(self.ui.line_edit_z.text()))
        return data


    def btn_send_clicked(self):
        try:
            self.data.refreshSendData(self.getAllSendData())
            # send_str = "@A6:" + str(self.data.send_data_roll) + ',' + str(self.data.send_data_pitch) + ',' \
            #         + str(self.data.send_data_yaw) + ',' + str(self.data.send_data_x) + ',' \
            #         + str(self.data.send_data_y) + ',' + str(self.data.send_data_z) + ',F0#'
            # print(send_str)
            # buff = bytes(send_str, encoding = "utf8")
            # s.sendto(buff, target_addr)
            self.pc.send_location(self.data.send_data_x, self.data.send_data_y, self.data.send_data_z,\
                                  self.data.send_data_roll, self.data.send_data_pitch, self.data.send_data_yaw,
                                  self.ui.spinBox_leg_vel.value())

        except Exception as e:
            traceback.print_exc()

    def btn_continuous_motion_clicked(self):
        try:
            params = list()

            params.append( FuncParams(self.ui.checkBox_x_enable.isChecked(), \
                                      self.ui.doubleSpinBox_x_ap.value(), \
                                      self.ui.doubleSpinBox_x_fr.value(), \
                                      self.ui.doubleSpinBox_x_fai.value()/180*math.pi ) )
            params.append( FuncParams(self.ui.checkBox_y_enable.isChecked(), \
                                      self.ui.doubleSpinBox_y_ap.value(), \
                                      self.ui.doubleSpinBox_y_fr.value(), \
                                      self.ui.doubleSpinBox_y_fai.value()/180*math.pi ) )
            params.append( FuncParams(self.ui.checkBox_z_enable.isChecked(), \
                                      self.ui.doubleSpinBox_z_ap.value(), \
                                      self.ui.doubleSpinBox_z_fr.value(), \
                                      self.ui.doubleSpinBox_z_fai.value()/180*math.pi ) )
            params.append( FuncParams(self.ui.checkBox_roll_enable.isChecked(), \
                                      self.ui.doubleSpinBox_roll_ap.value()/180*math.pi , \
                                      self.ui.doubleSpinBox_roll_fr.value(), \
                                      self.ui.doubleSpinBox_roll_fai.value()/180*math.pi ) )
            params.append( FuncParams(self.ui.checkBox_pitch_enable.isChecked(), \
                                      self.ui.doubleSpinBox_pitch_ap.value()/180*math.pi , \
                                      self.ui.doubleSpinBox_pitch_fr.value(), \
                                      self.ui.doubleSpinBox_pitch_fai.value()/180*math.pi ) )
            params.append( FuncParams(self.ui.checkBox_yaw_enable.isChecked(), \
                                      self.ui.doubleSpinBox_yaw_ap.value()/180*math.pi , \
                                      self.ui.doubleSpinBox_yaw_fr.value(), \
                                      self.ui.doubleSpinBox_yaw_fai.value()/180*math.pi ) )
            self.pc.send_func_params(params, self.ui.spinBox_loop_cnt.value(), self.ui.spinBox_z0.value())


            ##### send dataset #####
            # dataset = [[] for x in range(6)]
            # dataset = self.get_continuous_motion_dataset(self.ui.spinBox_loop_cnt.value())
            # delay = self.ui.spinBox_delay.value()/1000 # from ms to s
            # check_box_flags = [self.ui.checkBox_roll_enable.isChecked(), \
            #                    self.ui.checkBox_yaw_enable.isChecked(), \
            #                    self.ui.checkBox_pitch_enable.isChecked(), \
            #                    self.ui.checkBox_x_enable.isChecked(), \
            #                    self.ui.checkBox_y_enable.isChecked(), \
            #                    self.ui.checkBox_z_enable.isChecked() ]
            # z0 = self.ui.spinBox_z0.value()
            # if self.send_cont_motion_thrd == None or self.send_cont_motion_thrd.is_finished_:
            #     self.send_cont_motion_thrd = ThreadSendContinuousMotion(dataset, delay, check_box_flags, z0, self.pc)
            #     self.send_cont_motion_thrd.signal.connect(self.show_message_handle)
            #     self.send_cont_motion_thrd.start()

        except Exception as e:
            traceback.print_exc()

    def btn_cont_motion_stop_clicked(self):
        try:
            self.pc.send_stop_cmd()
            
            return
            #### stop sending data thread ####  abandon
            self.send_cont_motion_thrd.stop()

        except Exception as e:
            traceback.print_exc()



    def get_continuous_motion_dataset(self, loop_cnt):
        dataset = [[] for x in range(6)]
        z0 = self.ui.spinBox_z0.value()
        cnt = 0
        t = 0.0
       
        delay = self.ui.spinBox_delay.value()/1000 # from ms to s
        while cnt < loop_cnt:
            dataset[0].append(self.ui.doubleSpinBox_roll_ap.value() * \
                                math.sin(2*math.pi*self.ui.doubleSpinBox_roll_fr.value()*t \
                                + self.ui.doubleSpinBox_roll_fai.value()/180*math.pi))        # roll
            dataset[1].append(self.ui.doubleSpinBox_yaw_ap.value() * \
                                math.sin(2*math.pi*self.ui.doubleSpinBox_yaw_fr.value()*t \
                                + self.ui.doubleSpinBox_pitch_fai.value()/180*math.pi))          # yaw
            dataset[2].append(self.ui.doubleSpinBox_pitch_ap.value() *\
                                math.sin(2*math.pi*self.ui.doubleSpinBox_pitch_fr.value()*t \
                                + self.ui.doubleSpinBox_yaw_fai.value()/180*math.pi))      # pitch
            dataset[3].append(self.ui.doubleSpinBox_x_ap.value()*\
                                math.sin(2*math.pi*self.ui.doubleSpinBox_x_fr.value()*t \
                                + self.ui.doubleSpinBox_x_fai.value()/180*math.pi))              # x
            dataset[4].append(self.ui.doubleSpinBox_y_ap.value()*\
                                math.sin(2*math.pi*self.ui.doubleSpinBox_y_fr.value()*t + \
                                self.ui.doubleSpinBox_y_fai.value()/180*math.pi))              # y
            dataset[5].append(self.ui.doubleSpinBox_z_ap.value()*\
                                math.sin(2*math.pi*self.ui.doubleSpinBox_z_fr.value()*t + \
                                self.ui.doubleSpinBox_z_fai.value()/180*math.pi) + z0 )        # z
            t += delay
            cnt += 1
        
        return dataset

    def show_message_handle(self, msg):
        QMessageBox.information(self, '提示', msg)


class ThreadRefreshData(QThread):
    def __init__(self, pc, ui):
        super().__init__()
        self.delay_ = 0.1
        self.trigger_stop_ = False
        self.is_finished_ = True
        self.pc_ = pc
        self.ui_ = ui
        self.legs_data = list()
        self.is_getting_data = False

    def run(self):
        self.is_finished_ = False
        time.sleep(3)
        while self.is_finished_ != True:
            leglens = self.pc_.send_data_request()
            if self.is_getting_data == True:
                self.legs_data.append(leglens)
            print(leglens)
            self.ui_.leglen_1.setText(str(round(leglens[0])))
            self.ui_.leglen_2.setText(str(round(leglens[1])))
            self.ui_.leglen_3.setText(str(round(leglens[2])))
            self.ui_.leglen_4.setText(str(round(leglens[3])))
            self.ui_.leglen_5.setText(str(round(leglens[4])))
            self.ui_.leglen_6.setText(str(round(leglens[5])))
            time.sleep(self.delay_)
        self.is_finished_ = True

    def stop(self):
        self.is_finished_ = True

    def get_data(self):
        return self.legs_data

    def start_get_data(self):
        self.is_getting_data = True

    def finish_get_data(self):
        self.legs_data = list()
        self.is_getting_data = False

class ThreadSendContinuousMotion(QThread):
    signal = pyqtSignal(str)

    def __init__(self, dataset, delay, check_box_flags, z0, pc):
        super().__init__()
        self.dataset_ = dataset
        self.delay_ = delay
        self.check_box_flags_ = check_box_flags
        self.z0_ = z0
        self.trigger_stop_ = False
        self.is_finished_ = True
        self.pc = pc

    def run(self):
        self.is_finished_ = False
        for i in range(len(self.dataset_[0])):
            # send_str = ('@A6:%s,%s,%s,%s,%s,%s,F0#') \
            #             % (str(round(self.dataset_[0][i],2)) if self.check_box_flags_[0] else "0" , \
            #              str(round(self.dataset_[1][i],2)) if self.check_box_flags_[1] else "0" , \
            #              str(round(self.dataset_[2][i],2)) if self.check_box_flags_[2] else "0" , \
            #              str(round(self.dataset_[3][i],2)) if self.check_box_flags_[3] else "0" , \
            #              str(round(self.dataset_[4][i],2)) if self.check_box_flags_[4] else "0" , \
            #              str(round(self.dataset_[5][i],2)) if self.check_box_flags_[5] else str(self.z0_) \
            #             )
            # print(i,send_str)
            # buff = bytes(send_str, encoding = "utf8")
            # s.sendto(buff, target_addr)
            roll = round(self.dataset_[0][i],2) if self.check_box_flags_[0] else 0
            yaw  = round(self.dataset_[1][i],2) if self.check_box_flags_[1] else 0
            pitch= round(self.dataset_[2][i],2) if self.check_box_flags_[2] else 0
            x    = round(self.dataset_[3][i],2) if self.check_box_flags_[3] else 0
            y    = round(self.dataset_[4][i],2) if self.check_box_flags_[4] else 0
            z    = round(self.dataset_[5][i],2) if self.check_box_flags_[5] else self.z0_
            
            self.pc.send_location(x,y,z,roll,pitch, yaw)
            if self.trigger_stop_:
                break;
            time.sleep(self.delay_)
        self.is_finished_ = True
        self.signal.emit('done')

    def stop(self):
        self.trigger_stop_ = True

class FuncParams():
    def __init__(self, enable, ap, fr, pha):
        self.enable = enable
        self.ap = ap
        self.fr = fr
        self.pha = pha



if __name__ == "__main__":
    MainProgram()
