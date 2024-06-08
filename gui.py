# Copyright TU Wien (2022) - EVC: Task5
# Institute of Computer Graphics and Algorithms.

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 664)
        sizePolicy = QtWidgets.QSizePolicy()#QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\cg_icon.ico"))#, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_image = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy()#QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_image.sizePolicy().hasHeightForWidth())
        self.frame_image.setSizePolicy(sizePolicy)
        self.frame_image.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_image.setAutoFillBackground(False)
        self.frame_image.setStyleSheet("background-color:rgb(225, 225, 225)")
        # self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_image.setLineWidth(0)
        self.frame_image.setObjectName("frame_image")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_image)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_image = QtWidgets.QLabel(self.frame_image)
        sizePolicy = QtWidgets.QSizePolicy()#QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0,0,0);")
        self.label_image.setScaledContents(True)
        self.label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.verticalLayout_2.addWidget(self.label_image)
        self.horizontalLayout.addWidget(self.frame_image)
        self.frame_controls = QtWidgets.QFrame(self.centralwidget)
        self.frame_controls.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy()#QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy)
        # self.frame_controls.setCursor(QtCore.Qt.ArrowType.UpArrow)
        # self.frame_controls.setFrameShape(QtWidgets.QFrame.Panel)
        # self.frame_controls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_controls.setLineWidth(1)
        self.frame_controls.setObjectName("frame_controls")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_controls)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_info = QtWidgets.QGroupBox(self.frame_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox_info.sizePolicy().hasHeightForWidth())
        self.groupBox_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_info.setFont(font)
        self.groupBox_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_info.setFlat(False)
        self.groupBox_info.setObjectName("groupBox_info")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_info)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        # self.gridLayout.setSizeConstraint(QtWidgets.QLayout.Layout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 0, -1, -1)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_info_model = QtWidgets.QLabel(self.groupBox_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info_model.sizePolicy().hasHeightForWidth())
        self.label_info_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_info_model.setFont(font)
        self.label_info_model.setObjectName("label_info_model")
        self.gridLayout.addWidget(self.label_info_model, 0, 1, 1, 1)
        self.label_info_faces = QtWidgets.QLabel(self.groupBox_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info_faces.sizePolicy().hasHeightForWidth())
        self.label_info_faces.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_info_faces.setFont(font)
        self.label_info_faces.setObjectName("label_info_faces")
        self.gridLayout.addWidget(self.label_info_faces, 2, 1, 1, 1)
        self.label_info_vertices = QtWidgets.QLabel(self.groupBox_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info_vertices.sizePolicy().hasHeightForWidth())
        self.label_info_vertices.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_info_vertices.setFont(font)
        self.label_info_vertices.setObjectName("label_info_vertices")
        self.gridLayout.addWidget(self.label_info_vertices, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_info)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox_rasterization_mode = QtWidgets.QGroupBox(self.frame_controls)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_rasterization_mode.setFont(font)
        self.groupBox_rasterization_mode.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_rasterization_mode.setFlat(False)
        self.groupBox_rasterization_mode.setCheckable(False)
        self.groupBox_rasterization_mode.setObjectName("groupBox_rasterization_mode")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_rasterization_mode)
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_line = QtWidgets.QRadioButton(self.groupBox_rasterization_mode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_line.sizePolicy().hasHeightForWidth())
        self.radioButton_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_line.setFont(font)
        self.radioButton_line.setIconSize(QtCore.QSize(12, 12))
        self.radioButton_line.setChecked(True)
        self.radioButton_line.setObjectName("radioButton_line")
        self.horizontalLayout_2.addWidget(self.radioButton_line, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioButton_fill = QtWidgets.QRadioButton(self.groupBox_rasterization_mode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_fill.sizePolicy().hasHeightForWidth())
        self.radioButton_fill.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_fill.setFont(font)
        self.radioButton_fill.setObjectName("radioButton_fill")
        self.horizontalLayout_2.addWidget(self.radioButton_fill, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.groupBox_rasterization_mode)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.button_load_model = QtWidgets.QPushButton(self.frame_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_load_model.sizePolicy().hasHeightForWidth())
        self.button_load_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_load_model.setFont(font)
        self.button_load_model.setObjectName("button_load_model")
        self.verticalLayout.addWidget(self.button_load_model)
        self.button_rasterize = QtWidgets.QPushButton(self.frame_controls)
        self.button_rasterize.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_rasterize.sizePolicy().hasHeightForWidth())
        self.button_rasterize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_rasterize.setFont(font)
        self.button_rasterize.setObjectName("button_rasterize")
        self.verticalLayout.addWidget(self.button_rasterize)
        self.button_save_as = QtWidgets.QPushButton(self.frame_controls)
        self.button_save_as.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_save_as.sizePolicy().hasHeightForWidth())
        self.button_save_as.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_save_as.setFont(font)
        self.button_save_as.setObjectName("button_save_as")
        self.verticalLayout.addWidget(self.button_save_as)
        self.button_close = QtWidgets.QPushButton(self.frame_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_close.setFont(font)
        self.button_close.setObjectName("button_close")
        self.verticalLayout.addWidget(self.button_close)
        self.horizontalLayout.addWidget(self.frame_controls)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CG - Task 5"))
        self.label_image.setText(_translate("MainWindow", "Please load a model"))
        self.groupBox_info.setToolTip(_translate("MainWindow", "Information about the given model"))
        self.groupBox_info.setTitle(_translate("MainWindow", "Info"))
        self.label_2.setText(_translate("MainWindow", "Model:"))
        self.label_6.setText(_translate("MainWindow", "Vertices:"))
        self.label_info_model.setText(_translate("MainWindow", "-"))
        self.label_info_faces.setText(_translate("MainWindow", "-"))
        self.label_info_vertices.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "Faces:"))
        self.groupBox_rasterization_mode.setToolTip(_translate("MainWindow", "Select rasterization mode"))
        self.groupBox_rasterization_mode.setTitle(_translate("MainWindow", "Rasterization mode"))
        self.radioButton_line.setText(_translate("MainWindow", "line"))
        self.radioButton_fill.setText(_translate("MainWindow", "fill"))
        self.button_load_model.setText(_translate("MainWindow", "Load Model..."))
        self.button_rasterize.setText(_translate("MainWindow", "Rasterize"))
        self.button_save_as.setText(_translate("MainWindow", "Save as..."))
        self.button_close.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
