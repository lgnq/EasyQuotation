#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from forex_python.converter import CurrencyRates                    

import sys
import os

import pandas as pd

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from main_window import *

from openpyxl import load_workbook

import time
import re
import urllib.request
import requests

from PyQt5.QtCore import QDate

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('M.png'))

        self.df_mps = pd.read_excel('Pricing of BU MS Products.xlsx', sheet_name=1, header=7)
        self.df_ls  = pd.read_excel('Pricing of BU MS Products.xlsx', sheet_name=2, header=3)
        
        if os.path.exists("exchange_rate.txt"):
            self.load_exchange_rate()

        # self.dateEdit.setDate('1/1/2020')
        self.dateEdit_2.setDate(QDate.currentDate())
        self.current_currency_code = "6B27" #EUR

        self.exchange_rate_setup()

    def exchange_rate_setup(self):
        self.graphicsView.setTitle("ERU against CNY daily chart 欧元兑人民币日线图", color='k')

        self.graphicsView.setBackground('w')

        self.graphicsView.setLabel('left', text='CNY', units='元')  # y轴设置函数
        # self.graphicsView.setLabel('right', text='%')  # y轴设置函数
        # self.graphicsView.setLabel('bottom', text='date', units='day')  # x轴设置函数
        self.graphicsView.showGrid(x=True, y=True)  # 栅格设置函数
        self.graphicsView.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
        self.graphicsView.addLegend()  # 可选择是否添加legend

        # pen = pg.mkPen(color=(255, 0, 0))
        self.ttbr_line = self.graphicsView.plot(name='Telegraphic Transfer Buying Rate', pen='b', symbol='+')
        # pen = pg.mkPen(color=(255, 255, 0))
        self.cbr_line = self.graphicsView.plot(name='Cash Buying Rate', pen='g', symbol='+')
        # pen = pg.mkPen(color=(255, 0, 255))
        self.ttsr_line = self.graphicsView.plot(name='Telegraphic Transfer Selling Rate[Cash Selling Rate]', pen=(255,0,0), symbolBrush=(255,0,0), symbolPen='w', symbol='star', symbolSize=14)  

    def refresh(self):
        if self.current_currency_code == '6B27':    #EUR
            self.graphicsView.setTitle("ERU against CNY daily chart 欧元兑人民币日线图", color='k')
        elif self.current_currency_code == '7F8E':    #USD
            self.graphicsView.setTitle("USD against CNY daily chart 美元兑人民币日线图", color='k')
        
        dat = self.dateEdit.text().split('/')
        start = "{}-{}-{}".format(dat[2], dat[0], dat[1])
        
        dat = self.dateEdit_2.text().split('/')
        end = "{}-{}-{}".format(dat[2], dat[0], dat[1])
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

        #USD - http://fx.cmbchina.com/hq/History.aspx?startdate=2020-12-02&enddate=2021-01-20&nbr=%u7F8E%u5143&type=days
        #EUR - http://fx.cmbchina.com/hq/History.aspx?startdate=2020-12-02&enddate=2021-01-20&nbr=%u6B27%u5143&type=days
        url     = "http://fx.cmbchina.com/hq/History.aspx?startdate="+start+"&enddate="+end+"&nbr=%u"+self.current_currency_code+"%u5143&type=days"
        req     = urllib.request.Request(url, headers = headers)

        f = urllib.request.urlopen(req)
        html = f.read().decode("utf-8")

        date = re.findall('<td align="center">(.*?)</td>', html)
        data = re.findall('<td class="numberright">(.*?)</td>', html)

        TTBR = []
        CBR  = []
        TTSR = []
        # CSR  = []
        
        for i in range(0, int(len(data)/4)):
            TTBR.append(float(data[i*4]))
            CBR.append(float(data[i*4+1]))
            TTSR.append(float(data[i*4+2]))
            # CSR.append(float(data[i*4+3]))

        xax = self.graphicsView.getAxis('bottom') # 坐标轴x
        ticks = [list(zip(range(len(date)), date[::-1]))]
        xax.setTicks(ticks)

        self.ttbr_line.setData(y=TTBR[::-1])
        self.cbr_line.setData(y=CBR[::-1])
        self.ttsr_line.setData(y=TTSR[::-1])

        self.statusbar.showMessage("Exchange Rate refresh on {}, source from {}".format(self.dateEdit_2.text(), "CMBChina"))


    def currency_code_changed(self):
        if self.currency_code.currentIndex() == 0:  #EUR
            self.current_currency_code = "6B27"
            # self.graphicsView.setTitle("欧元兑人民币日线图", color='k')
        elif self.currency_code.currentIndex() == 1:  #USD
            self.current_currency_code = "7F8E"
            # self.graphicsView.setTitle("美元兑人民币日线图", color='k')

    def about(self):
        print("about")

    def order_number_text_edited(self):
        current_str = self.order_number.text().upper()

        self.listWidget.clear()

        if len(current_str) > 4:
            self.df_result = self.df_mps[self.df_mps['Part Number'].str.contains(current_str, na=False)]
            if (self.df_result.empty):
                self.df_result = self.df_ls[self.df_ls['MLX Order Number'].str.contains(current_str, na=False)]
                if (self.df_result.empty == False):
                    for ind in self.df_result.index:
                        self.listWidget.addItem('{} {} {} {} {} {} {} {} {}'.format(self.df_result['MLX Order Number'][ind], self.df_result['50K'][ind], self.df_result['100K'][ind], self.df_result['250K'][ind], self.df_result['500K'][ind], self.df_result['1M'][ind], self.df_result['2.5M'][ind], self.df_result['5M'][ind], self.df_result['10M'][ind]))
            else:
                for ind in self.df_result.index:
                    self.listWidget.addItem('{}{}{} {} {} {} {} {} {} {} {}'.format(self.df_result['Part Number'][ind], self.df_result['Temp Code'][ind], self.df_result['Package'][ind], self.df_result['>50K'][ind], self.df_result['>100K'][ind], self.df_result['>250K'][ind], self.df_result['>500K'][ind], self.df_result['>1M'][ind], self.df_result['>2.5M'][ind], self.df_result['>5 M'][ind], self.df_result['>10M'][ind]))

        if self.listWidget.count() == 1:
            self.update_price_list(self.listWidget.item(0).text())
        else:
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

    def update_price_list(self, text):
        self.price_50k.setEnabled(True)
        self.price_100k.setEnabled(True)
        self.price_250k.setEnabled(True)
        self.price_500k.setEnabled(True)
        self.price_1m.setEnabled(True)
        self.price_2_5m.setEnabled(True)
        self.price_5m.setEnabled(True)
        self.price_10m.setEnabled(True)

        price = text.split(' ')

        self.price_50k.setText("EUR {0:.3f}".format(float(price[1])))
        self.price_100k.setText("EUR {0:.3f}".format(float(price[2])))
        self.price_250k.setText("EUR {0:.3f}".format(float(price[3])))
        self.price_500k.setText("EUR {0:.3f}".format(float(price[4])))
        self.price_1m.setText("EUR {0:.3f}".format(float(price[5])))
        self.price_2_5m.setText("EUR {0:.3f}".format(float(price[6])))
        self.price_5m.setText("EUR {0:.3f}".format(float(price[7])))
        self.price_10m.setText("EUR {0:.3f}".format(float(price[8])))

    def list_view_clicked(self, qModelIndex):
        clicked_row = self.listWidget.currentItem().text()  

        self.update_price_list(clicked_row)    
    
    def clear(self):
        self.order_number.clear()
        self.listWidget.clear()

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

        self.save_quotation.setEnabled(False)

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

    def set_margin(self):
        if self.sender() == self.p8:
            self.margin.setText("8");
            self.margin_x.setText("8");

        if self.sender() == self.p10:
            self.margin.setText("10");
            self.margin_x.setText("10");

        if self.sender() == self.p15:
            self.margin.setText("15");
            self.margin_x.setText("15");

        self.update_quotation(self.margin, float(self.dc_eur.text()))

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

        self.statusbar.showMessage("Exchange Rate on {}".format(time))

        # self.statusbar.showMessage(time.asctime(time.localtime(time.time())))
        # self.statusbar.showMessage("Exchange Rate on {} | Price Book version {}".format(time, self.sheet0_name))

    def hexun_update(self):        
        url  = "https://open.er-api.com/v6/latest/CNY"
        json_data = requests.get(url).json()

        self.cny_usd = json_data["rates"]['USD']
        self.cny_eur = json_data["rates"]['EUR']

        url  = "https://open.er-api.com/v6/latest/USD"
        json_data = requests.get(url).json()

        self.usd_cny = json_data['rates']['CNY']
        self.usd_eur = json_data['rates']['EUR']

        url  = "https://open.er-api.com/v6/latest/EUR"
        json_data = requests.get(url).json()
        print(json_data['time_eol_unix'])

        self.eur_cny = json_data['rates']['CNY']
        self.eur_usd = json_data['rates']['USD']

        self.update_exchange_rate(json_data['time_last_update_utc'])

    # def hexun_update(self):        
    #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    #     url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXCNYUSD&column=Code,Price"
    #     req = urllib.request.Request(url, headers=headers)
    #     f = urllib.request.urlopen(req)
    #     html = f.read().decode("utf-8")

    #     s = re.findall("{.*}",str(html))[0]
    #     sjson = json.loads(s)

    #     self.cny_usd = sjson["Data"][0][0][1]/10000
    #     # print(self.cny_usd)

    #     # url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXCNYEUR&column=Code,Price"
    #     # req = urllib.request.Request(url, headers=headers)
    #     # f = urllib.request.urlopen(req)
    #     # html = f.read().decode("utf-8")
    #     # print(html)
    #     # s = re.findall("{.*}",str(html))[0]
    #     # sjson = json.loads(s)

    #     # self.cny_eur = sjson["Data"][0][0][1]/10000
    #     # print(self.cny_eur)

    #     url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDCNY&column=Code,Price"
    #     req = urllib.request.Request(url, headers=headers)
    #     f = urllib.request.urlopen(req)
    #     html = f.read().decode("utf-8")

    #     s = re.findall("{.*}",str(html))[0]
    #     sjson = json.loads(s)

    #     self.usd_cny = sjson["Data"][0][0][1]/10000
    #     # print(self.usd_cny)

    #     # url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXUSDEUR&column=Code,Price"
    #     # req = urllib.request.Request(url, headers=headers)
    #     # f = urllib.request.urlopen(req)
    #     # html = f.read().decode("utf-8")

    #     # s = re.findall("{.*}",str(html))[0]
    #     # sjson = json.loads(s)

    #     # self.usd_eur = sjson["Data"][0][0][1]/10000
    #     # print(self.usd_eur)

    #     url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXEURCNY&column=Code,Price"
    #     req = urllib.request.Request(url, headers=headers)
    #     f = urllib.request.urlopen(req)
    #     html = f.read().decode("utf-8")

    #     s = re.findall("{.*}",str(html))[0]
    #     sjson = json.loads(s)

    #     self.eur_cny = sjson["Data"][0][0][1]/10000
    #     # print(self.eur_cny)

    #     url = "http://webforex.hermes.hexun.com/forex/quotelist?code=FOREXEURUSD&column=Code,Price"
    #     req = urllib.request.Request(url, headers=headers)
    #     f = urllib.request.urlopen(req)
    #     html = f.read().decode("utf-8")

    #     s = re.findall("{.*}",str(html))[0]
    #     sjson = json.loads(s)

    #     self.eur_usd = sjson["Data"][0][0][1]/10000
    #     # print(self.eur_usd)

    #     self.usd_eur = 1/self.eur_usd
    #     self.cny_eur = 1/self.eur_cny

    #     self.update_exchange_rate(time.asctime(time.localtime(time.time())))
    #     # self.update_exchange_rate(QDate.currentDate())

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
   

    def open_quotation_xlsx(self):
        self.quotation_file_name, _ = QFileDialog.getOpenFileName(self, 'Open Backlog File', r'.\\', "(*.xlsx)")
        self.quotation_df = pd.read_excel(self.quotation_file_name, sheet_name=0, skiprows=0)
        # print(self.quotation_df)

        self.disty = self.quotation_df.loc[0, 'Disty']
        self.part_number = self.quotation_df.loc[0, 'part#']
        self.target_rmb_rs = self.quotation_df.loc[0, 'target RSL in RMB (13% VAT)']
        self.target_eur_rs = self.quotation_df.loc[0, 'target RSL in €']
        self.target_eur_dc = self.quotation_df.loc[0, 'target DC €']
        self.approved_eur_dc = self.quotation_df.loc[0, 'approved DC €']
        self.approved_date = self.quotation_df.loc[0, 'Approved date']
        self.approved_disty_margin = self.quotation_df.loc[0, 'disty margin']

        self.clear()

        self.order_number.setText(self.part_number)
        self.order_number_text_edited()

        self.rs_cny_vat_x.setText("{0:.4f}".format(self.target_rmb_rs))
        self.update_rs_cny_vat_x()

        self.save_quotation.setEnabled(True)

    def save_quotation_xlsx(self):
        wb = load_workbook(self.quotation_file_name)
        sheet_ranges = wb['Sheet1']

        print(sheet_ranges['B1'].value)
        sheet_ranges['B1'].value = 'NBO Number'
        
        wb.save("{}_{}.xlsx".format(self.disty, self.part_number))

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
    
    app.exec_()