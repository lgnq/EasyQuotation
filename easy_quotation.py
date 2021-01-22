#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from forex_python.converter import CurrencyRates                    

import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from main_window import *

import re
import json
import urllib.request

import xlrd
import time 
from PyQt5.QtCore import QStringListModel

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        if os.path.exists("exchange_rate.txt"):
            self.load_exchange_rate()

        self.wb = xlrd.open_workbook("price_book.xls")
        self.sheet = self.wb.sheet_by_index(0)

        self.qList = []

        self.exchange_rate_setup()

    def exchange_rate_setup(self):
        self.graphicsView.setBackground('w')

        # self.graphicsView.plot(title="sin 函数", x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])  # 添加第一个绘图窗口
        self.graphicsView.setLabel('left', text='meg', color='#ffffff')  # y轴设置函数
        self.graphicsView.showGrid(x=True, y=True)  # 栅格设置函数
        self.graphicsView.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
        self.graphicsView.setLabel('bottom', text='time', units='s')  # x轴设置函数
        # p1.addLegend()  # 可选择是否添加legend

    def about(self):
        print("about")

    def order_number_text_edited(self):
        current_str = self.order_number.text()

        #实例化列表模型，添加数据
        slm = QStringListModel()
        self.qList = []

        if len(current_str) > 7:
            for i in range(0, self.sheet.nrows):
                if self.sheet.cell_value(i, 0).find(current_str) >= 0:
                    # print(self.sheet.cell_value(i, 0))
                    self.qList.append(self.sheet.cell_value(i, 0))

        #设置模型列表视图，加载数据列表
        slm.setStringList(self.qList)

        #设置列表视图的模型
        self.listView.setModel(slm)

        if len(self.qList) == 1:
            self.update_price_list(self.qList[0])

        if len(self.qList) == 0:
            self.price_50k.setText("EUR 0.000") 
            self.price_100k.setText("EUR 0.000") 
            self.price_250k.setText("EUR 0.000") 
            self.price_500k.setText("EUR 0.000") 
            self.price_1m.setText("EUR 0.000") 
            self.price_2_5m.setText("EUR 0.000") 
            self.price_5m.setText("EUR 0.000") 
            self.price_10m.setText("EUR 0.000")             

    def price_x_clicked(self):
        button = self.findChild(QPushButton, self.sender().objectName())
        data = button.text().split(' ')
        price = float(data[1])

        self.update_quotation(button, price)

    def update_price_list(self, order_number):
        self.price_50k.setEnabled(True)
        self.price_100k.setEnabled(True)
        self.price_250k.setEnabled(True)
        self.price_500k.setEnabled(True)
        self.price_1m.setEnabled(True)
        self.price_2_5m.setEnabled(True)
        self.price_5m.setEnabled(True)
        self.price_10m.setEnabled(True)

        for i in range(0, self.sheet.nrows):
            if self.sheet.cell_value(i, 0) == order_number:
                column = 11
                self.price_50k.setText("EUR {}".format(str(self.sheet.cell_value(i, column)))) 
                self.price_100k.setText("EUR {}".format(str(self.sheet.cell_value(i, column+1)))) 
                self.price_250k.setText("EUR {}".format(str(self.sheet.cell_value(i, column+2)))) 
                self.price_500k.setText("EUR {}".format(str(self.sheet.cell_value(i, column+3)))) 
                self.price_1m.setText("EUR {}".format(str(self.sheet.cell_value(i, column+4)))) 
                self.price_2_5m.setText("EUR {}".format(str(self.sheet.cell_value(i, column+5)))) 
                self.price_5m.setText("EUR {}".format(str(self.sheet.cell_value(i, column+6)))) 
                self.price_10m.setText("EUR {}".format(str(self.sheet.cell_value(i, column+7)))) 

    def list_view_clicked(self, qModelIndex):
        # print(self.qList[qModelIndex.row()])  
        clicked_order_number = self.qList[qModelIndex.row()]
        self.update_price_list(clicked_order_number)    
    
    def clear(self):
        self.dc_cny.setText("")
        self.dc_usd.setText("")
        self.dc_eur.setText("")

        self.rs_eur.setText("")
        self.rs_usd.setText("")
        self.rs_cny.setText("")
        self.rs_cny_vat.setText("")

        self.rs_eur_x.setText("")
        self.rs_usd_x.setText("")
        self.rs_cny_x.setText("")
        self.rs_cny_vat_x.setText("")

    def update_quotation(self, current_obj, dc_eur):
        vat = float(self.vat.text()) / 100
        vat_x  = float(self.vat_x.text()) / 100

        margin = float(self.margin.text()) / 100
        margin_x  = float(self.margin_x.text()) / 100

        dc_cny = dc_eur * self.eur_cny
        dc_usd = dc_eur * self.eur_usd

        if current_obj != self.dc_eur:
            self.dc_eur.setText(("{0:.4f}").format(dc_eur))
        if current_obj != self.dc_usd:
            self.dc_usd.setText(("{0:.4f}").format(dc_usd))
        if current_obj != self.dc_cny:
            self.dc_cny.setText(("{0:.4f}").format(dc_cny))

        if current_obj != self.rs_cny:
            self.rs_cny.setText(("{0:.4f}").format(dc_cny*(1+margin)))
        if current_obj != self.rs_cny_vat:
            self.rs_cny_vat.setText(("{0:.4f}").format(dc_cny*(1+margin)*(1+vat)))
        if current_obj != self.rs_usd:
            self.rs_usd.setText(("{0:.4f}").format(dc_usd*(1+margin)))
        if current_obj != self.rs_eur:        
            self.rs_eur.setText(("{0:.4f}").format(dc_eur*(1+margin)))

        if current_obj != self.rs_cny_x:        
            self.rs_cny_x.setText(("{0:.4f}").format(dc_cny/(1-margin_x)))
        if current_obj != self.rs_cny_vat_x:        
            self.rs_cny_vat_x.setText(("{0:.4f}").format((dc_cny/(1-margin_x))*(1+vat_x)))
        if current_obj != self.rs_usd_x:        
            self.rs_usd_x.setText(("{0:.4f}").format(dc_usd/(1-margin_x)))
        if current_obj != self.rs_eur_x:        
            self.rs_eur_x.setText(("{0:.4f}").format(dc_eur/(1-margin_x)))        

    def update_cny(self):
        if self.dc_cny.text() != '':
            dc_cny = float(self.dc_cny.text())
            dc_eur = dc_cny * self.cny_eur 
        else:
            dc_eur = 0

        self.update_quotation(self.dc_cny, dc_eur)

    def update_usd(self):
        if self.dc_usd.text() != '':
            dc_usd = float(self.dc_usd.text())
            dc_eur = dc_usd * self.usd_eur 
        else:
            dc_eur = 0
        
        self.update_quotation(self.dc_usd, dc_eur)

    def update_eur(self):
        if self.dc_eur.text() != '':
            dc_eur = float(self.dc_eur.text())
        else:
            dc_eur = 0

        self.update_quotation(self.dc_eur, dc_eur)

    def update_rs_cny(self):
        margin = float(self.margin.text()) / 100

        rs_cny = float(self.rs_cny.text())
        dc_eur = (rs_cny/(1+margin)) * self.cny_eur 
        
        self.update_quotation(self.rs_cny, dc_eur)

    def update_rs_cny_vat(self):
        margin = float(self.margin.text()) / 100
        vat = float(self.vat.text()) / 100

        rs_cny_vat = float(self.rs_cny_vat.text())
        dc_eur = ((rs_cny_vat/(1+vat))/(1+margin)) * self.cny_eur 

        self.update_quotation(self.rs_cny_vat, dc_eur)

    def update_rs_usd(self):
        margin = float(self.margin.text()) / 100

        rs_usd = float(self.rs_usd.text())
        dc_eur = (rs_usd/(1+margin)) * self.usd_eur 
        
        self.update_quotation(self.rs_usd, dc_eur)

    def update_rs_eur(self):
        margin = float(self.margin.text()) / 100

        rs_eur = float(self.rs_eur.text())
        dc_eur = rs_eur/(1+margin) 
        
        self.update_quotation(self.rs_eur, dc_eur)

    def update_rs_cny_x(self):
        rs_cny_x = float(self.rs_cny_x.text())
        margin_x = float(self.margin_x.text()) / 100
        
        dc_eur = (rs_cny_x*(1-margin_x)) * self.cny_eur 
        
        self.update_quotation(self.rs_cny_x, dc_eur)

    def update_rs_cny_vat_x(self):
        rs_cny_vat_x = float(self.rs_cny_vat_x.text())
        margin_x = float(self.margin_x.text()) / 100
        vat_x = float(self.vat_x.text()) / 100

        dc_eur = ((rs_cny_vat_x/(1+vat_x))*(1-margin_x)) * self.cny_eur 

        self.update_quotation(self.rs_cny_vat_x, dc_eur)

    def update_rs_usd_x(self):
        rs_usd_x = float(self.rs_usd_x.text())
        margin_x = float(self.margin_x.text()) / 100

        dc_eur = (rs_usd_x*(1-margin_x)) * self.usd_eur 
        
        self.update_quotation(self.rs_usd_x, dc_eur)

    def update_rs_eur_x(self):
        rs_eur_x = float(self.rs_eur_x.text())
        margin_x = float(self.margin_x.text()) / 100

        dc_eur = rs_eur_x*(1-margin_x) 
        
        self.update_quotation(self.rs_eur_x, dc_eur)   

    def update_margin(self):
        self.update_quotation(self.margin, float(self.dc_eur.text()))

    def update_vat(self):
        self.update_quotation(self.vat, float(self.dc_eur.text()))

    def update_margin_x(self):
        self.update_quotation(self.margin_x, float(self.dc_eur.text()))

    def update_vat_x(self):
        self.update_quotation(self.vat_x, float(self.dc_eur.text()))        

    def update_exchange_rate(self, time):
        #1 CNY
        self.one_cny_xusd.setText(("1 CNY = {0:.4f} USD").format(self.cny_usd))
        self.one_cny_xeur.setText(("1 CNY = {0:.4f} EUR").format(self.cny_eur))

        # #1 USD
        self.one_usd_xeur.setText(("1 USD = {0:.4f} EUR").format(self.usd_eur))
        self.one_usd_xcny.setText(("1 USD = {0:.4f} CNY").format(self.usd_cny))        

        # #1 EUR
        self.one_eur_xusd.setText(("1 EUR = {0:.4f} USD").format(self.eur_usd))
        self.one_eur_xcny.setText(("1 EUR = {0:.4f} CNY").format(self.eur_cny))   

        self.quotation_group.setEnabled(True)    

        self.dc_eur.setEnabled(True)           
        self.dc_usd.setEnabled(True)           
        self.dc_cny.setEnabled(True)    

        self.rs_cny.setEnabled(True)       
        self.rs_cny_x.setEnabled(True)

        self.rs_cny_vat.setEnabled(True)       
        self.rs_cny_vat_x.setEnabled(True)       

        self.rs_eur.setEnabled(True)       
        self.rs_eur_x.setEnabled(True)

        self.rs_usd.setEnabled(True)       
        self.rs_usd_x.setEnabled(True)                       

        self.button_save_exchange_rate.setEnabled(True)

        # self.statusbar.showMessage(time.asctime(time.localtime(time.time())))
        self.statusbar.showMessage("Exchange Rate on {}".format(time))

    def hexun_update(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

        url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXCNYUSD&column=Code,Price"
        req = urllib.request.Request(url, headers=headers)
        f = urllib.request.urlopen(req)
        html = f.read().decode("utf-8")

        s = re.findall("{.*}",str(html))[0]
        sjson = json.loads(s)

        self.cny_usd = sjson["Data"][0][0][1]/10000
        # print(self.cny_usd)

        # url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXCNYEUR&column=Code,Price"
        # req = urllib.request.Request(url, headers=headers)
        # f = urllib.request.urlopen(req)
        # html = f.read().decode("utf-8")
        # print(html)
        # s = re.findall("{.*}",str(html))[0]
        # sjson = json.loads(s)

        # self.cny_eur = sjson["Data"][0][0][1]/10000
        # print(self.cny_eur)

        url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Code,Price"
        req = urllib.request.Request(url, headers=headers)
        f = urllib.request.urlopen(req)
        html = f.read().decode("utf-8")

        s = re.findall("{.*}",str(html))[0]
        sjson = json.loads(s)

        self.usd_cny = sjson["Data"][0][0][1]/10000
        # print(self.usd_cny)

        # url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDEUR&column=Code,Price"
        # req = urllib.request.Request(url, headers=headers)
        # f = urllib.request.urlopen(req)
        # html = f.read().decode("utf-8")

        # s = re.findall("{.*}",str(html))[0]
        # sjson = json.loads(s)

        # self.usd_eur = sjson["Data"][0][0][1]/10000
        # print(self.usd_eur)

        url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXEURCNY&column=Code,Price"
        req = urllib.request.Request(url, headers=headers)
        f = urllib.request.urlopen(req)
        html = f.read().decode("utf-8")

        s = re.findall("{.*}",str(html))[0]
        sjson = json.loads(s)

        self.eur_cny = sjson["Data"][0][0][1]/10000
        # print(self.eur_cny)

        url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXEURUSD&column=Code,Price"
        req = urllib.request.Request(url, headers=headers)
        f = urllib.request.urlopen(req)
        html = f.read().decode("utf-8")

        s = re.findall("{.*}",str(html))[0]
        sjson = json.loads(s)

        self.eur_usd = sjson["Data"][0][0][1]/10000
        # print(self.eur_usd)

        self.usd_eur = 1/self.eur_usd
        self.cny_eur = 1/self.eur_cny

        self.update_exchange_rate(time.asctime(time.localtime(time.time())))

    def forex_update(self):
        self.c = CurrencyRates()                                                 
        self.usd_eur = self.c.get_rate('USD', 'EUR')                                     
        self.usd_cny = self.c.get_rate('USD', 'CNY')

        # print(self.usd_eur)    
        # print(self.usd_cny)    

        self.cny_eur = self.c.get_rate('CNY', 'EUR')                                     
        self.cny_usd = self.c.get_rate('CNY', 'USD')

        # print(self.cny_eur)    
        # print(self.cny_usd)    

        self.eur_cny = self.c.get_rate('EUR', 'CNY')                                     
        self.eur_usd = self.c.get_rate('EUR', 'USD')

        # print(self.eur_cny)    
        # print(self.eur_usd)            

        self.update_exchange_rate(time.asctime(time.localtime(time.time())))
   

    def print_quotation(self):
        margin = float(self.margin.text()) / 100
        margin_x = float(self.margin_x.text()) / 100

        localtime = time.asctime(time.localtime(time.time()))
        print(localtime)

        print("Disty Cost: {0:.4f}EUR = {1:.4f}USD = {2:.4f}CNY".format(float(self.dc_eur.text()), float(self.dc_usd.text()), float(self.dc_cny.text())))
        print("Resale[{3}%]: {0:.4f}EUR = {1:.4f}USD = {2:.4f}CNY".format(float(self.rs_eur.text()), float(self.rs_usd.text()), float(self.rs_cny.text()), margin*100))
        print("Resale[{3}%] standard: {0:.4f}EUR = {1:.4f}USD = {2:.4f}CNY".format(float(self.rs_eur_x.text()), float(self.rs_usd_x.text()), float(self.rs_cny_x.text()), margin_x*100))

    def save_exchange_rate(self):
        f = open("exchange_rate.txt", "w") 
        f.write(time.asctime(time.localtime(time.time())))
        f.write('\r')
        f.write("1 EUR = {0:.4f} USD\r".format(self.eur_usd))
        f.write("1 EUR = {0:.4f} CNY\r".format(self.eur_cny))
        f.write("1 USD = {0:.4f} EUR\r".format(self.usd_eur))
        f.write("1 USD = {0:.4f} CNY\r".format(self.usd_cny))
        f.write("1 CNY = {0:.4f} EUR\r".format(self.cny_eur))
        f.write("1 CNY = {0:.4f} USD\r".format(self.cny_usd))
        f.close()             

    def load_exchange_rate(self):
        f = open("exchange_rate.txt", "r") 
        lines = f.readlines()  
        f.close()             

        for line in lines:
            data = line.split(' ')
            print(data)

        self.eur_usd = float(lines[1].split(' ')[3])
        self.eur_cny = float(lines[2].split(' ')[3])
        self.usd_eur = float(lines[3].split(' ')[3])
        self.usd_cny = float(lines[4].split(' ')[3])
        self.cny_eur = float(lines[5].split(' ')[3])
        self.cny_usd = float(lines[6].split(' ')[3])

        self.update_exchange_rate(lines[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())