# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(704, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_6.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_6.addWidget(self.lineEdit_5, 2, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_6.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_6.addWidget(self.lineEdit_6, 2, 5, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_6.addWidget(self.lineEdit_7, 2, 6, 1, 1)
        self.price_10m = QtWidgets.QPushButton(self.groupBox_6)
        self.price_10m.setEnabled(False)
        self.price_10m.setObjectName("price_10m")
        self.gridLayout_6.addWidget(self.price_10m, 3, 8, 1, 1)
        self.price_5m = QtWidgets.QPushButton(self.groupBox_6)
        self.price_5m.setEnabled(False)
        self.price_5m.setObjectName("price_5m")
        self.gridLayout_6.addWidget(self.price_5m, 3, 7, 1, 1)
        self.price_2_5m = QtWidgets.QPushButton(self.groupBox_6)
        self.price_2_5m.setEnabled(False)
        self.price_2_5m.setObjectName("price_2_5m")
        self.gridLayout_6.addWidget(self.price_2_5m, 3, 6, 1, 1)
        self.price_1m = QtWidgets.QPushButton(self.groupBox_6)
        self.price_1m.setEnabled(False)
        self.price_1m.setObjectName("price_1m")
        self.gridLayout_6.addWidget(self.price_1m, 3, 5, 1, 1)
        self.price_250k = QtWidgets.QPushButton(self.groupBox_6)
        self.price_250k.setEnabled(False)
        self.price_250k.setObjectName("price_250k")
        self.gridLayout_6.addWidget(self.price_250k, 3, 3, 1, 1)
        self.price_500k = QtWidgets.QPushButton(self.groupBox_6)
        self.price_500k.setEnabled(False)
        self.price_500k.setObjectName("price_500k")
        self.gridLayout_6.addWidget(self.price_500k, 3, 4, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_6.addWidget(self.lineEdit_9, 2, 8, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_6.addWidget(self.lineEdit_8, 2, 7, 1, 1)
        self.listView = QtWidgets.QListView(self.groupBox_6)
        self.listView.setObjectName("listView")
        self.gridLayout_6.addWidget(self.listView, 1, 3, 1, 6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_6.addWidget(self.lineEdit_4, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 1, 1, 2)
        self.price_100k = QtWidgets.QPushButton(self.groupBox_6)
        self.price_100k.setEnabled(False)
        self.price_100k.setObjectName("price_100k")
        self.gridLayout_6.addWidget(self.price_100k, 3, 2, 1, 1)
        self.price_50k = QtWidgets.QPushButton(self.groupBox_6)
        self.price_50k.setEnabled(False)
        self.price_50k.setObjectName("price_50k")
        self.gridLayout_6.addWidget(self.price_50k, 3, 1, 1, 1)
        self.order_number = QtWidgets.QLineEdit(self.groupBox_6)
        self.order_number.setObjectName("order_number")
        self.gridLayout_6.addWidget(self.order_number, 0, 3, 1, 6)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.one_cny_xusd = QtWidgets.QLineEdit(self.groupBox)
        self.one_cny_xusd.setEnabled(False)
        self.one_cny_xusd.setObjectName("one_cny_xusd")
        self.gridLayout_5.addWidget(self.one_cny_xusd, 0, 2, 1, 1)
        self.one_eur_xusd = QtWidgets.QLineEdit(self.groupBox)
        self.one_eur_xusd.setEnabled(False)
        self.one_eur_xusd.setObjectName("one_eur_xusd")
        self.gridLayout_5.addWidget(self.one_eur_xusd, 0, 0, 1, 1)
        self.one_cny_xeur = QtWidgets.QLineEdit(self.groupBox)
        self.one_cny_xeur.setEnabled(False)
        self.one_cny_xeur.setObjectName("one_cny_xeur")
        self.gridLayout_5.addWidget(self.one_cny_xeur, 1, 2, 1, 1)
        self.one_usd_xeur = QtWidgets.QLineEdit(self.groupBox)
        self.one_usd_xeur.setEnabled(False)
        self.one_usd_xeur.setObjectName("one_usd_xeur")
        self.gridLayout_5.addWidget(self.one_usd_xeur, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 0, 3, 1, 1)
        self.one_eur_xcny = QtWidgets.QLineEdit(self.groupBox)
        self.one_eur_xcny.setEnabled(False)
        self.one_eur_xcny.setObjectName("one_eur_xcny")
        self.gridLayout_5.addWidget(self.one_eur_xcny, 1, 0, 1, 1)
        self.button_save_exchange_rate = QtWidgets.QPushButton(self.groupBox)
        self.button_save_exchange_rate.setEnabled(False)
        self.button_save_exchange_rate.setObjectName("button_save_exchange_rate")
        self.gridLayout_5.addWidget(self.button_save_exchange_rate, 0, 4, 1, 1)
        self.button_load_exchange_rate = QtWidgets.QPushButton(self.groupBox)
        self.button_load_exchange_rate.setObjectName("button_load_exchange_rate")
        self.gridLayout_5.addWidget(self.button_load_exchange_rate, 1, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.one_usd_xcny = QtWidgets.QLineEdit(self.groupBox)
        self.one_usd_xcny.setEnabled(False)
        self.one_usd_xcny.setObjectName("one_usd_xcny")
        self.gridLayout_5.addWidget(self.one_usd_xcny, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.quotation_group = QtWidgets.QGroupBox(self.tab)
        self.quotation_group.setEnabled(False)
        self.quotation_group.setObjectName("quotation_group")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.quotation_group)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.quotation_group)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.dc_usd = QtWidgets.QLineEdit(self.groupBox_2)
        self.dc_usd.setEnabled(False)
        self.dc_usd.setObjectName("dc_usd")
        self.gridLayout.addWidget(self.dc_usd, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.dc_cny = QtWidgets.QLineEdit(self.groupBox_2)
        self.dc_cny.setEnabled(False)
        self.dc_cny.setObjectName("dc_cny")
        self.gridLayout.addWidget(self.dc_cny, 2, 1, 1, 1)
        self.dc_eur = QtWidgets.QLineEdit(self.groupBox_2)
        self.dc_eur.setEnabled(False)
        self.dc_eur.setObjectName("dc_eur")
        self.gridLayout.addWidget(self.dc_eur, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.quotation_group)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 9, 0, 1, 1)
        self.rs_eur = QtWidgets.QLineEdit(self.groupBox_3)
        self.rs_eur.setEnabled(False)
        self.rs_eur.setObjectName("rs_eur")
        self.gridLayout_2.addWidget(self.rs_eur, 9, 1, 1, 1)
        self.rs_cny_vat = QtWidgets.QLineEdit(self.groupBox_3)
        self.rs_cny_vat.setEnabled(False)
        self.rs_cny_vat.setObjectName("rs_cny_vat")
        self.gridLayout_2.addWidget(self.rs_cny_vat, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.rs_usd = QtWidgets.QLineEdit(self.groupBox_3)
        self.rs_usd.setEnabled(False)
        self.rs_usd.setObjectName("rs_usd")
        self.gridLayout_2.addWidget(self.rs_usd, 8, 1, 1, 1)
        self.rs_cny = QtWidgets.QLineEdit(self.groupBox_3)
        self.rs_cny.setEnabled(False)
        self.rs_cny.setObjectName("rs_cny")
        self.gridLayout_2.addWidget(self.rs_cny, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)
        self.vat = QtWidgets.QLineEdit(self.groupBox_3)
        self.vat.setObjectName("vat")
        self.gridLayout_2.addWidget(self.vat, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.margin = QtWidgets.QLineEdit(self.groupBox_3)
        self.margin.setObjectName("margin")
        self.gridLayout_2.addWidget(self.margin, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.quotation_group)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rs_eur_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.rs_eur_x.setEnabled(False)
        self.rs_eur_x.setObjectName("rs_eur_x")
        self.gridLayout_4.addWidget(self.rs_eur_x, 7, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 7, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.margin_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.margin_x.setObjectName("margin_x")
        self.gridLayout_4.addWidget(self.margin_x, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)
        self.rs_cny_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.rs_cny_x.setEnabled(False)
        self.rs_cny_x.setObjectName("rs_cny_x")
        self.gridLayout_4.addWidget(self.rs_cny_x, 4, 1, 1, 1)
        self.rs_usd_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.rs_usd_x.setEnabled(False)
        self.rs_usd_x.setObjectName("rs_usd_x")
        self.gridLayout_4.addWidget(self.rs_usd_x, 6, 1, 1, 1)
        self.rs_cny_vat_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.rs_cny_vat_x.setEnabled(False)
        self.rs_cny_vat_x.setObjectName("rs_cny_vat_x")
        self.gridLayout_4.addWidget(self.rs_cny_vat_x, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.vat_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.vat_x.setObjectName("vat_x")
        self.gridLayout_4.addWidget(self.vat_x, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.quotation_group)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.quotation_group)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.button_clear = QtWidgets.QPushButton(self.quotation_group)
        self.button_clear.setObjectName("button_clear")
        self.verticalLayout.addWidget(self.button_clear)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.quotation_group)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout.addWidget(self.lineEdit_10)
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.graphicsView = PlotWidget(self.tab_2)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.button_clear.clicked.connect(MainWindow.clear)
        self.dc_cny.textEdited['QString'].connect(MainWindow.update_cny)
        self.dc_usd.textEdited['QString'].connect(MainWindow.update_usd)
        self.dc_eur.textEdited['QString'].connect(MainWindow.update_eur)
        self.rs_cny.textEdited['QString'].connect(MainWindow.update_rs_cny)
        self.rs_usd.textEdited['QString'].connect(MainWindow.update_rs_usd)
        self.rs_eur.textEdited['QString'].connect(MainWindow.update_rs_eur)
        self.pushButton.clicked.connect(MainWindow.hexun_update)
        self.pushButton_2.clicked.connect(MainWindow.forex_update)
        self.rs_cny_vat.textEdited['QString'].connect(MainWindow.update_rs_cny_vat)
        self.rs_usd_x.textEdited['QString'].connect(MainWindow.update_rs_usd_x)
        self.rs_cny_x.textEdited['QString'].connect(MainWindow.update_rs_cny_x)
        self.rs_cny_vat_x.textEdited['QString'].connect(MainWindow.update_rs_cny_vat_x)
        self.rs_eur_x.textEdited['QString'].connect(MainWindow.update_rs_eur_x)
        self.margin_x.textEdited['QString'].connect(MainWindow.update_margin_x)
        self.pushButton_3.clicked.connect(MainWindow.print_quotation)
        self.button_save_exchange_rate.clicked.connect(MainWindow.save_exchange_rate)
        self.button_load_exchange_rate.clicked.connect(MainWindow.load_exchange_rate)
        self.actionAbout.triggered.connect(MainWindow.about)
        self.actionClear.triggered.connect(MainWindow.clear)
        self.order_number.textEdited['QString'].connect(MainWindow.order_number_text_edited)
        self.listView.clicked['QModelIndex'].connect(MainWindow.list_view_clicked)
        self.vat_x.textEdited['QString'].connect(MainWindow.update_vat_x)
        self.price_50k.clicked.connect(MainWindow.price_x_clicked)
        self.price_100k.clicked.connect(MainWindow.price_x_clicked)
        self.price_250k.clicked.connect(MainWindow.price_x_clicked)
        self.price_500k.clicked.connect(MainWindow.price_x_clicked)
        self.price_1m.clicked.connect(MainWindow.price_x_clicked)
        self.price_2_5m.clicked.connect(MainWindow.price_x_clicked)
        self.price_5m.clicked.connect(MainWindow.price_x_clicked)
        self.price_10m.clicked.connect(MainWindow.price_x_clicked)
        self.margin.textEdited['QString'].connect(MainWindow.update_margin)
        self.vat.textEdited['QString'].connect(MainWindow.update_vat)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Quotation"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Price List"))
        self.lineEdit_2.setText(_translate("MainWindow", "50K"))
        self.lineEdit_5.setText(_translate("MainWindow", "500K"))
        self.lineEdit_3.setText(_translate("MainWindow", "100K"))
        self.lineEdit_6.setText(_translate("MainWindow", "1M"))
        self.lineEdit_7.setText(_translate("MainWindow", "2.5M"))
        self.price_10m.setText(_translate("MainWindow", "EUR 0.000"))
        self.price_5m.setText(_translate("MainWindow", "EUR 0.000"))
        self.price_2_5m.setText(_translate("MainWindow", "EUR 0.000"))
        self.price_1m.setText(_translate("MainWindow", "EUR 0.000"))
        self.price_250k.setText(_translate("MainWindow", "EUR 0.000"))
        self.price_500k.setText(_translate("MainWindow", "EUR 0.000"))
        self.lineEdit_9.setText(_translate("MainWindow", "10M"))
        self.lineEdit_8.setText(_translate("MainWindow", "5M"))
        self.lineEdit_4.setText(_translate("MainWindow", "250K"))
        self.label_4.setText(_translate("MainWindow", "Melexis Order Number"))
        self.price_100k.setText(_translate("MainWindow", "EUR 0.000"))
        self.price_50k.setText(_translate("MainWindow", "EUR 0.000"))
        self.groupBox.setTitle(_translate("MainWindow", "Exchange Rate"))
        self.one_cny_xusd.setText(_translate("MainWindow", "1 CNY = ? USD"))
        self.one_eur_xusd.setText(_translate("MainWindow", "1 EUR = ? USD"))
        self.one_cny_xeur.setText(_translate("MainWindow", "1 CNY = ? EUR"))
        self.one_usd_xeur.setText(_translate("MainWindow", "1 USD = ? EUR"))
        self.pushButton.setText(_translate("MainWindow", "Hexun"))
        self.one_eur_xcny.setText(_translate("MainWindow", "1 EUR = ? CNY"))
        self.button_save_exchange_rate.setText(_translate("MainWindow", "Save"))
        self.button_load_exchange_rate.setText(_translate("MainWindow", "Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Forex"))
        self.one_usd_xcny.setText(_translate("MainWindow", "1 USD = ? CNY"))
        self.quotation_group.setTitle(_translate("MainWindow", "Quotation Result"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Disty Cost"))
        self.label_2.setText(_translate("MainWindow", "USD:"))
        self.label.setText(_translate("MainWindow", "CNY:"))
        self.label_3.setText(_translate("MainWindow", "EUR:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Resale Price"))
        self.label_8.setText(_translate("MainWindow", "EUR:"))
        self.label_16.setText(_translate("MainWindow", "CNY(VAT):"))
        self.label_9.setText(_translate("MainWindow", "CNY:"))
        self.label_7.setText(_translate("MainWindow", "USD:"))
        self.vat.setText(_translate("MainWindow", "13"))
        self.label_10.setText(_translate("MainWindow", "VAT %:"))
        self.label_6.setText(_translate("MainWindow", "Margin %:"))
        self.margin.setText(_translate("MainWindow", "15"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Resale Price(standard) "))
        self.label_15.setText(_translate("MainWindow", "EUR:"))
        self.label_13.setText(_translate("MainWindow", "CNY:"))
        self.label_5.setText(_translate("MainWindow", "Margin %:"))
        self.margin_x.setText(_translate("MainWindow", "15"))
        self.label_18.setText(_translate("MainWindow", "CNY(VAT):"))
        self.label_14.setText(_translate("MainWindow", "USD:"))
        self.label_11.setText(_translate("MainWindow", "VAT %:"))
        self.vat_x.setText(_translate("MainWindow", "13"))
        self.pushButton_3.setText(_translate("MainWindow", "Print"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic"))
        self.label_12.setText(_translate("MainWindow", "Start"))
        self.label_17.setText(_translate("MainWindow", "End"))
        self.label_19.setText(_translate("MainWindow", "Money"))
        self.pushButton_4.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Exchange Rate"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
from pyqtgraph import PlotWidget
