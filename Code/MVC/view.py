from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog

import sys


class Ui_MainWindow(QMainWindow):

    def __init__(self, controller):
        super(Ui_MainWindow, self).__init__()

        self.controller = controller
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.setFixedSize(929, 766)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 571, 291))

        self.tabWidget.setObjectName("tabWidget")

        self.behavior_tab = QtWidgets.QWidget()

        self.behavior_tab.setObjectName("behavior_tab")

        self.frame_parameters = QtWidgets.QFrame(self.behavior_tab)

        self.frame_parameters.setGeometry(QtCore.QRect(10, 10, 221, 261))

        self.frame_parameters.setStyleSheet("")

        self.frame_parameters.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_parameters.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_parameters.setObjectName("frame_parameters")

        self.parameters = QtWidgets.QLabel(self.frame_parameters)

        self.parameters.setGeometry(QtCore.QRect(70, 0, 55, 16))

        self.parameters.setObjectName("parameters")

        self.size_of_env = QtWidgets.QLabel(self.frame_parameters)

        self.size_of_env.setGeometry(QtCore.QRect(11, 41, 116, 16))

        self.size_of_env.setObjectName("size_of_env")

        self.sampling_frequency = QtWidgets.QLabel(self.frame_parameters)

        self.sampling_frequency.setGeometry(QtCore.QRect(11, 71, 144, 16))

        self.sampling_frequency.setObjectName("sampling_frequency")

        self.binwidth = QtWidgets.QLabel(self.frame_parameters)

        self.binwidth.setGeometry(QtCore.QRect(11, 100, 44, 16))

        self.binwidth.setObjectName("binwidth")

        self.smooth_factor = QtWidgets.QLabel(self.frame_parameters)

        self.smooth_factor.setGeometry(QtCore.QRect(11, 129, 69, 16))

        self.smooth_factor.setObjectName("smooth_factor")

        self.binsizedir = QtWidgets.QLabel(self.frame_parameters)

        self.binsizedir.setGeometry(QtCore.QRect(10, 160, 48, 16))

        self.binsizedir.setObjectName("binsizedir")

        self.input_size_of_env = QtWidgets.QLineEdit(self.frame_parameters)

        self.input_size_of_env.setGeometry(QtCore.QRect(160, 40, 46, 19))

        self.input_size_of_env.setObjectName("input_size_of_env")

        self.input_sampling_freq = QtWidgets.QLineEdit(self.frame_parameters)

        self.input_sampling_freq.setGeometry(QtCore.QRect(160, 70, 46, 19))

        self.input_sampling_freq.setObjectName("input_sampling_freq")

        self.input_binwidth = QtWidgets.QLineEdit(self.frame_parameters)

        self.input_binwidth.setGeometry(QtCore.QRect(160, 100, 46, 19))

        self.input_binwidth.setObjectName("input_binwidth")

        self.input_smooth_factor = QtWidgets.QLineEdit(self.frame_parameters)

        self.input_smooth_factor.setGeometry(QtCore.QRect(160, 130, 46, 19))

        self.input_smooth_factor.setObjectName("input_smooth_factor")

        self.input_binsizedir = QtWidgets.QLineEdit(self.frame_parameters)

        self.input_binsizedir.setGeometry(QtCore.QRect(160, 160, 46, 19))

        self.input_binsizedir.setObjectName("input_binsizedir")

        self.frame_figure = QtWidgets.QFrame(self.behavior_tab)

        self.frame_figure.setGeometry(QtCore.QRect(240, 10, 151, 261))

        self.frame_figure.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_figure.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_figure.setObjectName("frame_figure")

        self.figure_selection = QtWidgets.QLabel(self.frame_figure)

        self.figure_selection.setGeometry(QtCore.QRect(20, 0, 86, 14))

        self.figure_selection.setObjectName("figure_selection")

        self.layoutWidget = QtWidgets.QWidget(self.frame_figure)

        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 133, 68))

        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.setObjectName("verticalLayout")

        self.path = QtWidgets.QCheckBox(self.layoutWidget)

        self.path.setObjectName("path")

        self.verticalLayout.addWidget(self.path)

        self.time_map = QtWidgets.QCheckBox(self.layoutWidget)

        self.time_map.setObjectName("time_map")

        self.verticalLayout.addWidget(self.time_map)

        self.directional_occupancy = QtWidgets.QCheckBox(self.layoutWidget)

        self.directional_occupancy.setObjectName("directional_occupancy")

        self.verticalLayout.addWidget(self.directional_occupancy)

        self.analysis_path = QtWidgets.QPushButton(self.frame_figure)

        self.analysis_path.setGeometry(QtCore.QRect(0, 190, 71, 23))

        self.analysis_path.setObjectName("analysis_path")

        self.figure_path = QtWidgets.QPushButton(self.frame_figure)

        self.figure_path.setGeometry(QtCore.QRect(80, 190, 71, 23))

        self.figure_path.setObjectName("figure_path")

        self.frame_3 = QtWidgets.QFrame(self.behavior_tab)

        self.frame_3.setGeometry(QtCore.QRect(400, 30, 143, 141))

        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_3.setObjectName("frame_3")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.verticalLayout_analysis = QtWidgets.QVBoxLayout()

        self.verticalLayout_analysis.setObjectName("verticalLayout_analysis")

        self.max_timemap_value = QtWidgets.QCheckBox(self.frame_3)

        self.max_timemap_value.setObjectName("max_timemap_value")

        self.verticalLayout_analysis.addWidget(self.max_timemap_value)

        self.mean_instantaneous = QtWidgets.QCheckBox(self.frame_3)

        self.mean_instantaneous.setObjectName("mean_instantaneous")

        self.verticalLayout_analysis.addWidget(self.mean_instantaneous)

        self.mean_speed = QtWidgets.QCheckBox(self.frame_3)

        self.mean_speed.setObjectName("mean_speed")

        self.verticalLayout_analysis.addWidget(self.mean_speed)

        self.total_distance = QtWidgets.QCheckBox(self.frame_3)

        self.total_distance.setObjectName("total_distance")

        self.verticalLayout_analysis.addWidget(self.total_distance)

        self.total_time = QtWidgets.QCheckBox(self.frame_3)

        self.total_time.setObjectName("total_time")

        self.verticalLayout_analysis.addWidget(self.total_time)

        self.verticalLayout_5.addLayout(self.verticalLayout_analysis)

        self.Analysis = QtWidgets.QLabel(self.behavior_tab)

        self.Analysis.setGeometry(QtCore.QRect(420, 10, 123, 14))

        self.Analysis.setObjectName("Analysis")

        self.run_analysis = QtWidgets.QPushButton(self.behavior_tab)

        self.run_analysis.setGeometry(QtCore.QRect(410, 200, 123, 23))

        self.run_analysis.setObjectName("run_analysis")

        self.tabWidget.addTab(self.behavior_tab, "")

        self.spike_tab = QtWidgets.QWidget()

        self.spike_tab.setObjectName("spike_tab")

        self.tabWidget.addTab(self.spike_tab, "")

        self.browse_file = QtWidgets.QToolButton(self.centralwidget)

        self.browse_file.setGeometry(QtCore.QRect(10, 10, 69, 20))

        self.browse_file.setObjectName("browse_file")

        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)

        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))

        self.layoutWidget1.setObjectName("layoutWidget1")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)

        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)

        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 2, 2))

        self.layoutWidget2.setObjectName("layoutWidget2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)

        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)

        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 2, 2))

        self.layoutWidget3.setObjectName("layoutWidget3")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)

        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.setObjectName("horizontalLayout")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)

        self.statusBar.setObjectName("statusBar")

        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "SPACE"))

        self.parameters.setText(_translate("MainWindow", "Parameters"))

        self.size_of_env.setText(_translate("MainWindow", "Size of the environment"))

        self.sampling_frequency.setText(_translate("MainWindow", "Sampling frequency (camera)"))

        self.binwidth.setText(_translate("MainWindow", "BinWidth"))

        self.smooth_factor.setText(_translate("MainWindow", "Smooth factor"))

        self.binsizedir.setText(_translate("MainWindow", "BinsizeDir"))

        self.figure_selection.setText(_translate("MainWindow", "Figure Selection"))

        self.path.setText(_translate("MainWindow", "Path"))

        self.time_map.setText(_translate("MainWindow", "Time Map"))

        self.directional_occupancy.setText(_translate("MainWindow", "Directional Occupancy"))

        self.analysis_path.setText(_translate("MainWindow", "Analysis path"))

        self.figure_path.setText(_translate("MainWindow", "Figure path"))

        self.max_timemap_value.setText(_translate("MainWindow", "Max Timemap value"))

        self.mean_instantaneous.setText(_translate("MainWindow", "Mean instantaneous"))

        self.mean_speed.setText(_translate("MainWindow", "Mean speed"))

        self.total_distance.setText(_translate("MainWindow", "Total distance"))

        self.total_time.setText(_translate("MainWindow", "Total time"))

        self.Analysis.setText(_translate("MainWindow", "Analysis Selection"))

        self.run_analysis.setText(_translate("MainWindow", "Run analysis"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.behavior_tab), _translate("MainWindow", "Behavior"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spike_tab), _translate("MainWindow", "Spike"))

        self.browse_file.setText(_translate("MainWindow", "Browse File"))
        self.browse_file.clicked.connect(self.open_file_dialog)


    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            self.controller.read_file(filename)


if __name__ == "__main__":
    app = QApplication([])

    window = Ui_MainWindow(None)

    window.show()

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())