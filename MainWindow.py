# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StewartCtrlPanelUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabWidget.setGeometry(QtCore.QRect(10, 10, 781, 271))
        self.MainTabWidget.setObjectName("MainTabWidget")
        self.TestPanel = QtWidgets.QWidget()
        self.TestPanel.setObjectName("TestPanel")
        self.groupBox = QtWidgets.QGroupBox(self.TestPanel)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 741, 231))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 701, 111))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.slider_roll = QtWidgets.QSlider(self.horizontalLayoutWidget_4)
        self.slider_roll.setOrientation(QtCore.Qt.Horizontal)
        self.slider_roll.setObjectName("slider_roll")
        self.horizontalLayout.addWidget(self.slider_roll)
        self.line_edit_roll = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.line_edit_roll.setMinimumSize(QtCore.QSize(137, 20))
        self.line_edit_roll.setText("")
        self.line_edit_roll.setObjectName("line_edit_roll")
        self.horizontalLayout.addWidget(self.line_edit_roll)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.slider_pitch = QtWidgets.QSlider(self.horizontalLayoutWidget_4)
        self.slider_pitch.setMaximumSize(QtCore.QSize(135, 16777215))
        self.slider_pitch.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pitch.setObjectName("slider_pitch")
        self.horizontalLayout_2.addWidget(self.slider_pitch)
        self.line_edit_pitch = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.line_edit_pitch.setObjectName("line_edit_pitch")
        self.horizontalLayout_2.addWidget(self.line_edit_pitch)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.slider_yaw = QtWidgets.QSlider(self.horizontalLayoutWidget_4)
        self.slider_yaw.setOrientation(QtCore.Qt.Horizontal)
        self.slider_yaw.setObjectName("slider_yaw")
        self.horizontalLayout_3.addWidget(self.slider_yaw)
        self.line_edit_yaw = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.line_edit_yaw.setObjectName("line_edit_yaw")
        self.horizontalLayout_3.addWidget(self.line_edit_yaw)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.slider_x = QtWidgets.QSlider(self.horizontalLayoutWidget_4)
        self.slider_x.setOrientation(QtCore.Qt.Horizontal)
        self.slider_x.setObjectName("slider_x")
        self.horizontalLayout_4.addWidget(self.slider_x)
        self.line_edit_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.line_edit_x.setObjectName("line_edit_x")
        self.horizontalLayout_4.addWidget(self.line_edit_x)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.slider_y = QtWidgets.QSlider(self.horizontalLayoutWidget_4)
        self.slider_y.setOrientation(QtCore.Qt.Horizontal)
        self.slider_y.setObjectName("slider_y")
        self.horizontalLayout_5.addWidget(self.slider_y)
        self.line_edit_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.line_edit_y.setObjectName("line_edit_y")
        self.horizontalLayout_5.addWidget(self.line_edit_y)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.slider_z = QtWidgets.QSlider(self.horizontalLayoutWidget_4)
        self.slider_z.setOrientation(QtCore.Qt.Horizontal)
        self.slider_z.setObjectName("slider_z")
        self.horizontalLayout_7.addWidget(self.slider_z)
        self.line_edit_z = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.line_edit_z.setObjectName("line_edit_z")
        self.horizontalLayout_7.addWidget(self.line_edit_z)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(470, 170, 239, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_9.addWidget(self.btn_clear)
        self.btn_send = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_9.addWidget(self.btn_send)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 189, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_32.addWidget(self.label_31)
        self.spinBox_leg_vel = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_leg_vel.setMinimum(100)
        self.spinBox_leg_vel.setMaximum(4500)
        self.spinBox_leg_vel.setSingleStep(100)
        self.spinBox_leg_vel.setProperty("value", 1000)
        self.spinBox_leg_vel.setDisplayIntegerBase(10)
        self.spinBox_leg_vel.setObjectName("spinBox_leg_vel")
        self.horizontalLayout_32.addWidget(self.spinBox_leg_vel)
        self.MainTabWidget.addTab(self.TestPanel, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 751, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(30, 40, 421, 166))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_roll_enable = QtWidgets.QCheckBox(self.horizontalLayoutWidget_9)
        self.checkBox_roll_enable.setChecked(True)
        self.checkBox_roll_enable.setObjectName("checkBox_roll_enable")
        self.verticalLayout.addWidget(self.checkBox_roll_enable)
        self.checkBox_pitch_enable = QtWidgets.QCheckBox(self.horizontalLayoutWidget_9)
        self.checkBox_pitch_enable.setChecked(True)
        self.checkBox_pitch_enable.setObjectName("checkBox_pitch_enable")
        self.verticalLayout.addWidget(self.checkBox_pitch_enable)
        self.checkBox_yaw_enable = QtWidgets.QCheckBox(self.horizontalLayoutWidget_9)
        self.checkBox_yaw_enable.setChecked(True)
        self.checkBox_yaw_enable.setObjectName("checkBox_yaw_enable")
        self.verticalLayout.addWidget(self.checkBox_yaw_enable)
        self.checkBox_x_enable = QtWidgets.QCheckBox(self.horizontalLayoutWidget_9)
        self.checkBox_x_enable.setChecked(True)
        self.checkBox_x_enable.setObjectName("checkBox_x_enable")
        self.verticalLayout.addWidget(self.checkBox_x_enable)
        self.checkBox_y_enable = QtWidgets.QCheckBox(self.horizontalLayoutWidget_9)
        self.checkBox_y_enable.setChecked(True)
        self.checkBox_y_enable.setObjectName("checkBox_y_enable")
        self.verticalLayout.addWidget(self.checkBox_y_enable)
        self.checkBox_z_enable = QtWidgets.QCheckBox(self.horizontalLayoutWidget_9)
        self.checkBox_z_enable.setChecked(True)
        self.checkBox_z_enable.setObjectName("checkBox_z_enable")
        self.verticalLayout.addWidget(self.checkBox_z_enable)
        self.horizontalLayout_22.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.doubleSpinBox_roll_fr = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_roll_fr.setEnabled(True)
        self.doubleSpinBox_roll_fr.setDecimals(1)
        self.doubleSpinBox_roll_fr.setSingleStep(0.1)
        self.doubleSpinBox_roll_fr.setProperty("value", 1.0)
        self.doubleSpinBox_roll_fr.setObjectName("doubleSpinBox_roll_fr")
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_roll_fr)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.doubleSpinBox_pitch_fr = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_pitch_fr.setEnabled(True)
        self.doubleSpinBox_pitch_fr.setDecimals(1)
        self.doubleSpinBox_pitch_fr.setSingleStep(0.1)
        self.doubleSpinBox_pitch_fr.setProperty("value", 1.0)
        self.doubleSpinBox_pitch_fr.setObjectName("doubleSpinBox_pitch_fr")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_pitch_fr)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.doubleSpinBox_yaw_fr = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_yaw_fr.setEnabled(True)
        self.doubleSpinBox_yaw_fr.setDecimals(1)
        self.doubleSpinBox_yaw_fr.setSingleStep(0.1)
        self.doubleSpinBox_yaw_fr.setProperty("value", 1.0)
        self.doubleSpinBox_yaw_fr.setObjectName("doubleSpinBox_yaw_fr")
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_yaw_fr)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.doubleSpinBox_x_fr = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_x_fr.setEnabled(True)
        self.doubleSpinBox_x_fr.setDecimals(1)
        self.doubleSpinBox_x_fr.setSingleStep(0.1)
        self.doubleSpinBox_x_fr.setProperty("value", 1.0)
        self.doubleSpinBox_x_fr.setObjectName("doubleSpinBox_x_fr")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_x_fr)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.doubleSpinBox_y_fr = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_y_fr.setEnabled(True)
        self.doubleSpinBox_y_fr.setDecimals(1)
        self.doubleSpinBox_y_fr.setSingleStep(0.1)
        self.doubleSpinBox_y_fr.setProperty("value", 1.0)
        self.doubleSpinBox_y_fr.setObjectName("doubleSpinBox_y_fr")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_y_fr)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.doubleSpinBox_z_fr = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_z_fr.setEnabled(True)
        self.doubleSpinBox_z_fr.setDecimals(1)
        self.doubleSpinBox_z_fr.setSingleStep(0.1)
        self.doubleSpinBox_z_fr.setProperty("value", 1.0)
        self.doubleSpinBox_z_fr.setObjectName("doubleSpinBox_z_fr")
        self.horizontalLayout_15.addWidget(self.doubleSpinBox_z_fr)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_22.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.doubleSpinBox_roll_ap = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_roll_ap.setEnabled(True)
        self.doubleSpinBox_roll_ap.setDecimals(0)
        self.doubleSpinBox_roll_ap.setSingleStep(1.0)
        self.doubleSpinBox_roll_ap.setProperty("value", 10.0)
        self.doubleSpinBox_roll_ap.setObjectName("doubleSpinBox_roll_ap")
        self.horizontalLayout_16.addWidget(self.doubleSpinBox_roll_ap)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.doubleSpinBox_pitch_ap = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_pitch_ap.setEnabled(True)
        self.doubleSpinBox_pitch_ap.setDecimals(0)
        self.doubleSpinBox_pitch_ap.setSingleStep(1.0)
        self.doubleSpinBox_pitch_ap.setProperty("value", 10.0)
        self.doubleSpinBox_pitch_ap.setObjectName("doubleSpinBox_pitch_ap")
        self.horizontalLayout_17.addWidget(self.doubleSpinBox_pitch_ap)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.doubleSpinBox_yaw_ap = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_yaw_ap.setEnabled(True)
        self.doubleSpinBox_yaw_ap.setDecimals(0)
        self.doubleSpinBox_yaw_ap.setSingleStep(1.0)
        self.doubleSpinBox_yaw_ap.setProperty("value", 10.0)
        self.doubleSpinBox_yaw_ap.setObjectName("doubleSpinBox_yaw_ap")
        self.horizontalLayout_18.addWidget(self.doubleSpinBox_yaw_ap)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_18.addWidget(self.label_16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.doubleSpinBox_x_ap = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_x_ap.setEnabled(True)
        self.doubleSpinBox_x_ap.setDecimals(0)
        self.doubleSpinBox_x_ap.setSingleStep(1.0)
        self.doubleSpinBox_x_ap.setProperty("value", 30.0)
        self.doubleSpinBox_x_ap.setObjectName("doubleSpinBox_x_ap")
        self.horizontalLayout_19.addWidget(self.doubleSpinBox_x_ap)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_19.addWidget(self.label_17)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.doubleSpinBox_y_ap = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_y_ap.setEnabled(True)
        self.doubleSpinBox_y_ap.setDecimals(0)
        self.doubleSpinBox_y_ap.setSingleStep(1.0)
        self.doubleSpinBox_y_ap.setProperty("value", 30.0)
        self.doubleSpinBox_y_ap.setObjectName("doubleSpinBox_y_ap")
        self.horizontalLayout_20.addWidget(self.doubleSpinBox_y_ap)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.doubleSpinBox_z_ap = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_z_ap.setEnabled(True)
        self.doubleSpinBox_z_ap.setDecimals(0)
        self.doubleSpinBox_z_ap.setSingleStep(1.0)
        self.doubleSpinBox_z_ap.setProperty("value", 30.0)
        self.doubleSpinBox_z_ap.setObjectName("doubleSpinBox_z_ap")
        self.horizontalLayout_21.addWidget(self.doubleSpinBox_z_ap)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_21.addWidget(self.label_19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.doubleSpinBox_roll_fai = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_roll_fai.setEnabled(True)
        self.doubleSpinBox_roll_fai.setDecimals(0)
        self.doubleSpinBox_roll_fai.setMinimum(-360.0)
        self.doubleSpinBox_roll_fai.setMaximum(360.0)
        self.doubleSpinBox_roll_fai.setSingleStep(1.0)
        self.doubleSpinBox_roll_fai.setProperty("value", 0.0)
        self.doubleSpinBox_roll_fai.setObjectName("doubleSpinBox_roll_fai")
        self.horizontalLayout_26.addWidget(self.doubleSpinBox_roll_fai)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_26.addWidget(self.label_24)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.doubleSpinBox_pitch_fai = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_pitch_fai.setEnabled(True)
        self.doubleSpinBox_pitch_fai.setDecimals(0)
        self.doubleSpinBox_pitch_fai.setMinimum(-360.0)
        self.doubleSpinBox_pitch_fai.setMaximum(360.0)
        self.doubleSpinBox_pitch_fai.setSingleStep(1.0)
        self.doubleSpinBox_pitch_fai.setProperty("value", 0.0)
        self.doubleSpinBox_pitch_fai.setObjectName("doubleSpinBox_pitch_fai")
        self.horizontalLayout_27.addWidget(self.doubleSpinBox_pitch_fai)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_27.addWidget(self.label_25)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.doubleSpinBox_yaw_fai = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_yaw_fai.setEnabled(True)
        self.doubleSpinBox_yaw_fai.setDecimals(0)
        self.doubleSpinBox_yaw_fai.setMinimum(-360.0)
        self.doubleSpinBox_yaw_fai.setMaximum(360.0)
        self.doubleSpinBox_yaw_fai.setSingleStep(1.0)
        self.doubleSpinBox_yaw_fai.setProperty("value", 0.0)
        self.doubleSpinBox_yaw_fai.setObjectName("doubleSpinBox_yaw_fai")
        self.horizontalLayout_28.addWidget(self.doubleSpinBox_yaw_fai)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_28.addWidget(self.label_26)
        self.verticalLayout_7.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.doubleSpinBox_x_fai = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_x_fai.setEnabled(True)
        self.doubleSpinBox_x_fai.setDecimals(0)
        self.doubleSpinBox_x_fai.setMinimum(-360.0)
        self.doubleSpinBox_x_fai.setMaximum(360.0)
        self.doubleSpinBox_x_fai.setSingleStep(1.0)
        self.doubleSpinBox_x_fai.setProperty("value", 0.0)
        self.doubleSpinBox_x_fai.setObjectName("doubleSpinBox_x_fai")
        self.horizontalLayout_29.addWidget(self.doubleSpinBox_x_fai)
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_29.addWidget(self.label_27)
        self.verticalLayout_7.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.doubleSpinBox_y_fai = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_y_fai.setEnabled(True)
        self.doubleSpinBox_y_fai.setDecimals(0)
        self.doubleSpinBox_y_fai.setMinimum(-360.0)
        self.doubleSpinBox_y_fai.setMaximum(360.0)
        self.doubleSpinBox_y_fai.setSingleStep(1.0)
        self.doubleSpinBox_y_fai.setProperty("value", 90.0)
        self.doubleSpinBox_y_fai.setObjectName("doubleSpinBox_y_fai")
        self.horizontalLayout_30.addWidget(self.doubleSpinBox_y_fai)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_30.addWidget(self.label_28)
        self.verticalLayout_7.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.doubleSpinBox_z_fai = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_9)
        self.doubleSpinBox_z_fai.setEnabled(True)
        self.doubleSpinBox_z_fai.setDecimals(0)
        self.doubleSpinBox_z_fai.setMinimum(-360.0)
        self.doubleSpinBox_z_fai.setMaximum(360.0)
        self.doubleSpinBox_z_fai.setSingleStep(1.0)
        self.doubleSpinBox_z_fai.setProperty("value", 0.0)
        self.doubleSpinBox_z_fai.setObjectName("doubleSpinBox_z_fai")
        self.horizontalLayout_31.addWidget(self.doubleSpinBox_z_fai)
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_31.addWidget(self.label_29)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_22.addLayout(self.verticalLayout_7)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 60, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_24.addWidget(self.label_21)
        self.spinBox_z0 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_z0.setEnabled(True)
        self.spinBox_z0.setMinimum(1)
        self.spinBox_z0.setMaximum(1000)
        self.spinBox_z0.setProperty("value", 150)
        self.spinBox_z0.setObjectName("spinBox_z0")
        self.horizontalLayout_24.addWidget(self.spinBox_z0)
        self.verticalLayout_6.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.spinBox_loop_cnt = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_loop_cnt.setMinimum(1)
        self.spinBox_loop_cnt.setMaximum(10000)
        self.spinBox_loop_cnt.setProperty("value", 10)
        self.spinBox_loop_cnt.setDisplayIntegerBase(10)
        self.spinBox_loop_cnt.setObjectName("spinBox_loop_cnt")
        self.horizontalLayout_10.addWidget(self.spinBox_loop_cnt)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 160, 239, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.pushButton_continuous_motion = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_continuous_motion.setObjectName("pushButton_continuous_motion")
        self.horizontalLayout_25.addWidget(self.pushButton_continuous_motion)
        self.pushButton_cont_motion_stop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cont_motion_stop.setObjectName("pushButton_cont_motion_stop")
        self.horizontalLayout_25.addWidget(self.pushButton_cont_motion_stop)
        self.pushButton_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout_25.addWidget(self.pushButton_reset)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(150, 20, 54, 12))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_23.setObjectName("label_23")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(360, 20, 54, 12))
        self.label_30.setObjectName("label_30")
        self.MainTabWidget.addTab(self.tab_4, "")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(520, 50, 131, 41))
        self.logo_label.setObjectName("logo_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 290, 771, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 1, 0, 1, 1)
        self.leglen_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leglen_1.setEnabled(False)
        self.leglen_1.setObjectName("leglen_1")
        self.gridLayout.addWidget(self.leglen_1, 1, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 0, 6, 1, 1)
        self.leglen_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leglen_6.setEnabled(False)
        self.leglen_6.setObjectName("leglen_6")
        self.gridLayout.addWidget(self.leglen_6, 1, 6, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 0, 5, 1, 1)
        self.leglen_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leglen_2.setEnabled(False)
        self.leglen_2.setObjectName("leglen_2")
        self.gridLayout.addWidget(self.leglen_2, 1, 2, 1, 1)
        self.leglen_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leglen_4.setEnabled(False)
        self.leglen_4.setObjectName("leglen_4")
        self.gridLayout.addWidget(self.leglen_4, 1, 4, 1, 1)
        self.leglen_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leglen_5.setEnabled(False)
        self.leglen_5.setObjectName("leglen_5")
        self.gridLayout.addWidget(self.leglen_5, 1, 5, 1, 1)
        self.leglen_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leglen_3.setEnabled(False)
        self.leglen_3.setObjectName("leglen_3")
        self.gridLayout.addWidget(self.leglen_3, 1, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 0, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 0, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 4, 1, 1)
        self.save_data = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.save_data.setObjectName("save_data")
        self.gridLayout.addWidget(self.save_data, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        self.checkBox_roll_enable.clicked['bool'].connect(self.doubleSpinBox_roll_fr.setEnabled)
        self.checkBox_roll_enable.clicked['bool'].connect(self.doubleSpinBox_roll_ap.setEnabled)
        self.checkBox_pitch_enable.clicked['bool'].connect(self.doubleSpinBox_pitch_fr.setEnabled)
        self.checkBox_pitch_enable.clicked['bool'].connect(self.doubleSpinBox_pitch_ap.setEnabled)
        self.checkBox_yaw_enable.clicked['bool'].connect(self.doubleSpinBox_yaw_fr.setEnabled)
        self.checkBox_yaw_enable.clicked['bool'].connect(self.doubleSpinBox_yaw_ap.setEnabled)
        self.checkBox_x_enable.clicked['bool'].connect(self.doubleSpinBox_x_fr.setEnabled)
        self.checkBox_x_enable.clicked['bool'].connect(self.doubleSpinBox_x_ap.setEnabled)
        self.checkBox_y_enable.clicked['bool'].connect(self.doubleSpinBox_y_fr.setEnabled)
        self.checkBox_y_enable.clicked['bool'].connect(self.doubleSpinBox_y_ap.setEnabled)
        self.checkBox_z_enable.clicked['bool'].connect(self.doubleSpinBox_z_fr.setEnabled)
        self.checkBox_z_enable.clicked['bool'].connect(self.doubleSpinBox_z_ap.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "平台姿态（单位：°,mm）"))
        self.label.setText(_translate("MainWindow", "横滚角 roll"))
        self.label_2.setText(_translate("MainWindow", "俯仰角 pitch"))
        self.label_3.setText(_translate("MainWindow", "偏航角 yaw"))
        self.label_4.setText(_translate("MainWindow", "X 位移"))
        self.label_5.setText(_translate("MainWindow", "Y 位移"))
        self.label_6.setText(_translate("MainWindow", "Z 位移"))
        self.btn_clear.setText(_translate("MainWindow", "清零"))
        self.btn_send.setText(_translate("MainWindow", "发送"))
        self.label_31.setText(_translate("MainWindow", "支腿速度 mm/s"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.TestPanel), _translate("MainWindow", "单点运动"))
        self.groupBox_2.setTitle(_translate("MainWindow", "函数输出"))
        self.checkBox_roll_enable.setText(_translate("MainWindow", "横滚角 Roll"))
        self.checkBox_pitch_enable.setText(_translate("MainWindow", "俯仰角 Pitch"))
        self.checkBox_yaw_enable.setText(_translate("MainWindow", "偏航角 Yaw"))
        self.checkBox_x_enable.setText(_translate("MainWindow", "左右 X"))
        self.checkBox_y_enable.setText(_translate("MainWindow", "前后 Y"))
        self.checkBox_z_enable.setText(_translate("MainWindow", "上下 Z"))
        self.label_10.setText(_translate("MainWindow", "Hz"))
        self.label_7.setText(_translate("MainWindow", "Hz"))
        self.label_11.setText(_translate("MainWindow", "Hz"))
        self.label_9.setText(_translate("MainWindow", "Hz"))
        self.label_12.setText(_translate("MainWindow", "Hz"))
        self.label_13.setText(_translate("MainWindow", "Hz"))
        self.label_14.setText(_translate("MainWindow", "°"))
        self.label_15.setText(_translate("MainWindow", "°"))
        self.label_16.setText(_translate("MainWindow", "°"))
        self.label_17.setText(_translate("MainWindow", "mm"))
        self.label_18.setText(_translate("MainWindow", "mm"))
        self.label_19.setText(_translate("MainWindow", "mm"))
        self.label_24.setText(_translate("MainWindow", "°"))
        self.label_25.setText(_translate("MainWindow", "°"))
        self.label_26.setText(_translate("MainWindow", "°"))
        self.label_27.setText(_translate("MainWindow", "°"))
        self.label_28.setText(_translate("MainWindow", "°"))
        self.label_29.setText(_translate("MainWindow", "°"))
        self.label_21.setText(_translate("MainWindow", "中位高度(mm)："))
        self.label_8.setText(_translate("MainWindow", "运动时长(s)："))
        self.pushButton_continuous_motion.setText(_translate("MainWindow", "开始"))
        self.pushButton_cont_motion_stop.setText(_translate("MainWindow", "停止"))
        self.pushButton_reset.setText(_translate("MainWindow", "复位"))
        self.label_22.setText(_translate("MainWindow", "频率"))
        self.label_23.setText(_translate("MainWindow", "幅值"))
        self.label_30.setText(_translate("MainWindow", "相位"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.tab_4), _translate("MainWindow", "连续运动"))
        self.logo_label.setText(_translate("MainWindow", "logo"))
        self.label_20.setText(_translate("MainWindow", "支腿 1"))
        self.label_37.setText(_translate("MainWindow", "位置 mm"))
        self.label_36.setText(_translate("MainWindow", "支腿 6"))
        self.label_35.setText(_translate("MainWindow", "支腿 5"))
        self.label_32.setText(_translate("MainWindow", "支腿 2"))
        self.label_33.setText(_translate("MainWindow", "支腿 3"))
        self.label_34.setText(_translate("MainWindow", "支腿 4"))
        self.save_data.setText(_translate("MainWindow", "实时存储"))
