# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QApplication, QMessageBox
import tkinter as tk
from tkinter import filedialog as fd
import csv
import os
import pandas as pn
import numpy as np
import sys
import string
from pathlib import Path
# from extra import Ui_Form
import math
from scipy import stats
from sklearn import preprocessing





class Ui_MainWindow(object):
    def file_selection(self):
        path = fd.askopenfilename(filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        if len(path) == 0:
            return None
        """tr_dosya seçimi yapılıyor ---eng_file selection"""
        with open(path, 'r') as self.csvfile:
            self.csvreader = pn.read_csv(self.csvfile)
            self.csvfile.close()
            """tr_dosya okuma ve listeye aktarma ---eng_read file and transfer to list"""
        self.columns = self.csvreader.columns
        """tr_nitelik isimleri tespit edildi---eng_attribute names detected"""
        self.lencolumns = len(self.columns)
        """tr_sutun sayıları tespit edildi ---eng_row and column counts detected"""
        self.lenline = len(self.csvreader[self.columns[0]])
        self.dat = self.csvreader.dtypes
        self.intcolumns_name.clear()#liste sıfırlandı çünkü başka dosyalar seçilince comboboxda isimler kalmaya devam ediyordu
        for i in range(self.lencolumns):
            # ilk eleman nan ise onu float kabul ediyor bu yüzden ilk eleman nan kontrolü yapılıyor eğer nan ise sonraki eleman kontrol edliyor
            if self.dat[i] != object:
                self.intcolumns_name.append(self.columns[i])
                self.columsum.append(self.csvreader[self.columns[i]].sum())
                """integer değerlerin sütun isimleri bir listede tutldu"""
                """tr_niteliklerin veri tipleri integer olan değerler üzerinden işlemler yapacağımız için o sutunları seçiyoruz"""
                """eng_we choose those columns because we will be performing operations on values whose data types are integer"""
                self.intcolumns.append(self.csvreader[self.columns[i]])
        self.colcomboBox_3.clear()
        for a in range(self.lencolumns):
            self.allcolumns_name.append(self.columns[a])
            self.colcomboBox_3.addItem(self.columns[a])

        self.colcomboBox.clear()
        self.colcomboBox_2.clear()

        for i in self.intcolumns_name:
            self.colcomboBox.addItem(i)
            self.colcomboBox_2.addItem(i)

            """işlem yapılcak sütun seçilmesini sağlamak için comboboxlara int değere sahip niteliklerin isimleri eklendi"""
        self.sayi+=1
        self.missing_values_count = self.csvreader.isnull().sum()

    # -----------------------------------------------------------------------------------------------------------------------
    # eksik veri yoksa çalışmaması gereken fonksiyon kontrol noktası
    def mising_data_count(self):
        dizi = self.csvreader.isnull().sum()
        self.toplam = sum(dizi)
        # eksik veri sayısı hesaplandı
        if self.toplam == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No missing data")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return None
        else:
            return 1
    #------------------------------------------------------------------------------------------------------------------------
    #eksik veri varsa NaN sonuçlar almamak için yazıldı
    def mising_data_count_else(self):
        dizi = self.csvreader.isnull().sum()
        self.toplam = sum(dizi)
        # eksik veri sayısı hesaplandı
        if self.toplam != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You have missing data")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return None
        else:
            return 1

    # -----------------------------------------------------------------------------------------------------------------------
    # dosya seçilmesi kontrol noktası0
    def check_file(self):
        if len(self.csvreader) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select file")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return None
        else:
            return 1

    # -----------------------------------------------------------------------------------------------------------------------
    def missing_data_comp(self):
        """dosya seçilmemiş ise"""
        ad=self.check_file()
        if ad== None:
            return None

        """eksik veri yoksa :"""
        ad1=self.mising_data_count()
        if ad1 == None:
            return None

        # ortalamaya göre tamamlama
        if self.compcomboBox.currentText() == 'Mean':
            for i in self.intcolumns_name:
                self.csvreader[i].fillna(self.csvreader[i].mean(), inplace=True)
            self.csvreader.to_csv('car.csv', index=False)
        # Moda göre tamamlama
        if self.compcomboBox.currentText() == 'Mod':
            for i in self.intcolumns_name:
                self.csvreader[i].fillna(self.csvreader[i].mode(), inplace=True)
        # medyana göre tamamlama
        if self.compcomboBox.currentText() == 'Median':
            for i in self.intcolumns_name:
                self.csvreader[i].fillna(self.csvreader[i].median(), inplace=True)
        print(self.missing_values_count)
        self.textBrowser_5.setText(str(self.csvreader))
        print(self.csvreader)

    # -----------------------------------------------------------------------------------------------------------------------
    # eksik veri silinmesi
    def mising_data_delete(self):
        """dosya seçilmemiş ise"""
        ad = self.check_file()
        if ad == None:
            return None
        """eksik veri yoksa:"""
        asd = self.mising_data_count()
        if asd == None:
            return None
        # eksik veri sayısı 1/3den büyükse kısmı
        if self.toplam / self.lenline > 1 / 3:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Missing data count is bigger than (line count)/3")
            msg.setWindowTitle("Warning")
            msg.exec_()
            return  None

        self.csvreader = self.csvreader.dropna()
        print(self.csvreader)
        self.csvreader.to_csv('carssssssss.csv',mode='w',index=False,header=True)
        """veriyi kayıt etme"""
        """with open('carssssssss.csv','w') as f:
            writer = csv.writer(f)
            writer.writerows(self.csvreader)"""


    # -----------------------------------------------------------------------------------------------------------------------
    # nitelik üzerinde yapılmak istenen işlemi seçme fonk
    def select_fonction(self):
        asd = self.check_file()
        if asd == None:
            return None
        asd1=self.mising_data_count_else()
        if asd1== None:
            return None
        variable = self.colcomboBox.currentText()
        fonc = self.precesscomboBox_2.currentText()
        if fonc == 'Average':
            fin = self.csvreader[variable].mean()
            self.textBrowser_2.setText(str(fonc) + " of the " + str(variable) + " column =" + str(fin))
        if fonc == 'Median':
            fin = self.csvreader[variable].median()
            self.textBrowser_2.setText(str(fonc) + " of the " + str(variable) + " column =" + str(fin))
        if fonc == 'Mode':
            fin = self.csvreader[variable].mode()
            self.textBrowser_2.setText(str(fonc) + " of the " + str(variable) + " column =" + str(fin))
        if fonc == 'Frequency':
            fig, ax = plt.subplots()
            fin = self.csvreader[variable].value_counts().plot(ax=ax, kind='bar', xlabel=variable, ylabel=fonc)
            plt.show()
        if fonc == 'IQR':
            sort_array = sorted(self.csvreader[variable])
            self.Q1 = self.csvreader[variable].quantile(0.25)
            self.Q3 = self.csvreader[variable].quantile(0.75)
            self.iqr = self.Q3 - self.Q1
            self.textBrowser_2.setText(variable + " column IQR is " + str(self.iqr))

        if fonc == 'Outliers':
            """1. çeyreğin 1.5 katı az 3. çeyreğin 1.5 katı fazla olan değerler aykırı değerlerdir"""
            """kullanıcı ıqr değerini hesaplamadan buralara gelirse eğer hatalı çalışmaması için tekrar tanımlama yapıldı"""
            variable = self.colcomboBox.currentText()
            #sort_array = sorted(self.csvreader[variable])
            self.Q1 = self.csvreader[variable].quantile(0.25)
            self.Q3 = self.csvreader[variable].quantile(0.75)
            self.iqr = self.Q3 - self.Q1
            print(self.Q1, "-", self.Q3, "-", self.iqr)
            for i in range(self.lenline):
                if (self.csvreader[variable][i] < (self.Q1 - (self.iqr * 1.5))) or (
                        self.csvreader[variable][i] > (self.Q3 + (self.iqr * 1.5))):
                    self.textBrowser_2.append(str(self.csvreader[variable][i]))

        if fonc == 'Five Number Summary':
            self.textBrowser_2.setText("Minimum value in "+str(variable)+str(numpy.min(self.csvreader[variable])))
            self.textBrowser_2.append("Maximum value in "+str(variable)+str(numpy.max(self.csvreader[variable])))
            self.textBrowser_2.append("First quarter value in "+str(variable)+str(numpy.percentile(self.csvreader[variable],25)))
            self.textBrowser_2.append("Third  quarter in "+str(variable)+str(numpy.percentile(self.csvreader[variable],75)))
            self.textBrowser_2.append("Median value in "+str(variable)+str(numpy.median(self.csvreader[variable])))
        if fonc == 'Box Plot':
            plt.boxplot(self.csvreader[variable])
            plt.show()
        if fonc == 'Variance and Standard Deviation':
            self.textBrowser_2.setText("Standard deviation of "+str(variable)+" "+str(numpy.std(self.csvreader[variable])))
            self.textBrowser_2.append("Variance of "+str(variable)+" "+str(numpy.var(self.csvreader[variable])))
    # -------------------------------------------------------------------------------------------------------------------

    def outliner_norm(self):
        a=self.check_file()

        if a==None:
            return None
        b = self.mising_data_count_else()
        if b==None:
            return None
        variable = self.colcomboBox_2.currentText()
        fonc1 = self.zscore_raido_button.isChecked()
        fonc2 = self.minmax_radio_button.isChecked()
        if fonc1 == True:
            zscore = stats.zscore(self.csvreader[variable])
            self.textBrowser_3.setText(str(zscore))
            zscore.to_csv('carssssssss.csv',mode='w',index=False,header=True)
        if fonc2 == True:
            df_max_scaled = self.csvreader[variable]
            # apply normalization techniques
            for i in range(self.lenline):
                df_max_scaled[i] = df_max_scaled[i] / df_max_scaled.abs().max()
            self.textBrowser_3.setText(str(df_max_scaled))
            df_max_scaled.to_csv('carssssssss.csv',mode='w',index=False,header=True)
            """max_scaled=self.csvreader[variable].copy()
            max_sclaed=max_scaled / max_scaled.abs().max()
            self.textBrowser_3.setText(str(max_sclaed))
            max_scaled.to_csv('carssssssss.csv',mode='w',index=False,header=False)"""








    # ------------------------------------------------------------------------------------------------------------------
    def outliner_delet(self):
        a = self.check_file()

        if a == None:
            return None
        b = self.mising_data_count_else()
        if b == None:
            return None
        fonc1 = self.radioButton.isChecked()
        fonc2 = self.radioButton_2.isChecked()
        variable=variable = self.colcomboBox_2.currentText()
        if fonc1==True:
            self.Q1 = self.csvreader[variable].quantile(0.25)
            self.Q3 = self.csvreader[variable].quantile(0.75)
            self.iqr = self.Q3 - self.Q1
            print(self.Q1, "-", self.Q3, "-", self.iqr)
            data = self.csvreader
            for i in range(self.lenline):
                if (self.csvreader[variable][i] < (self.Q1 - (self.iqr * 1.5))) or (
                        self.csvreader[variable][i] > (self.Q3 + (self.iqr * 1.5))):
                    data = data.drop(data.index[1])

                    continue
                    # self.csvreader[variable][i]
            data.to_csv('carssssssss.csv', mode='w', index=False, header=True)
        if fonc2==True:
            self.Q1 = self.csvreader[variable].quantile(0.25)
            self.Q3 = self.csvreader[variable].quantile(0.75)
            self.iqr = self.Q3 - self.Q1
            print(self.Q1, "-", self.Q3, "-", self.iqr)
            data = self.csvreader
            for i in range(self.lenline):
                if (self.csvreader[variable][i] < (self.Q1 - (self.iqr * 1.5))) or (
                        self.csvreader[variable][i] > (self.Q3 + (self.iqr * 1.5))):
                    data = data.drop([variable],axis=1)
                    continue
                    # self.csvreader[variable][i]
            data.to_csv('carssssssss.csv', mode='w', index=False, header=True)






    def seacrh(self):
        pass
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 563)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 991, 521))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.fileselection = QtWidgets.QPushButton(self.tab_3)
        self.fileselection.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.fileselection.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.fileselection.setObjectName("fileselection")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 171, 81))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setToolTip("")
        self.textEdit.setToolTipDuration(0)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(280, 40, 101, 16))
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setObjectName("label")
        self.compcomboBox = QtWidgets.QComboBox(self.tab_3)
        self.compcomboBox.setGeometry(QtCore.QRect(280, 70, 91, 31))
        self.compcomboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.compcomboBox.setObjectName("compcomboBox")
        self.compcomboBox.addItem("")
        self.compcomboBox.addItem("")
        self.compcomboBox.addItem("")
        self.completebutton = QtWidgets.QPushButton(self.tab_3)
        self.completebutton.setGeometry(QtCore.QRect(280, 140, 93, 28))
        self.completebutton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.completebutton.setObjectName("completebutton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 190, 171, 81))
        self.textEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(620, 40, 111, 16))
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setObjectName("label_2")
        self.deletebutton = QtWidgets.QPushButton(self.tab_3)
        self.deletebutton.setGeometry(QtCore.QRect(620, 130, 93, 28))
        self.deletebutton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.deletebutton.setObjectName("deletebutton")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(620, 190, 331, 271))
        self.textBrowser_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(280, 190, 331, 271))
        self.textBrowser_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 371, 71))
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_5.setObjectName("label_5")
        self.colcomboBox = QtWidgets.QComboBox(self.tab_4)
        self.colcomboBox.setGeometry(QtCore.QRect(20, 140, 171, 21))
        self.colcomboBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.colcomboBox.setObjectName("colcomboBox")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 55, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.precesscomboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.precesscomboBox_2.setGeometry(QtCore.QRect(20, 290, 141, 31))
        self.precesscomboBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.precesscomboBox_2.setObjectName("precesscomboBox_2")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.precesscomboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 340, 121, 41))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(420, 20, 561, 461))
        self.textBrowser_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 190, 371, 81))
        self.textEdit_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_5.setObjectName("textEdit_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 10, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.textEdit_3.setPalette(palette)
        self.textEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 90, 221, 131))
        self.textEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_4.setObjectName("textEdit_4")
        self.colcomboBox_2 = QtWidgets.QComboBox(self.tab_5)
        self.colcomboBox_2.setGeometry(QtCore.QRect(20, 230, 141, 31))
        self.colcomboBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.colcomboBox_2.setObjectName("colcomboBox_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 10, 341, 411))
        self.textBrowser_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 280, 113, 22))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setObjectName("lineEdit")
        self.zscore_raido_button = QtWidgets.QRadioButton(self.tab_5)
        self.zscore_raido_button.setGeometry(QtCore.QRect(20, 320, 95, 20))
        self.zscore_raido_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.zscore_raido_button.setObjectName("zscore_raido_button")
        self.minmax_radio_button = QtWidgets.QRadioButton(self.tab_5)
        self.minmax_radio_button.setGeometry(QtCore.QRect(20, 360, 95, 20))
        self.minmax_radio_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.minmax_radio_button.setObjectName("minmax_radio_button")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 280, 113, 22))
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.norm_pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.norm_pushButton_2.setGeometry(QtCore.QRect(20, 420, 93, 28))
        self.norm_pushButton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.norm_pushButton_2.setObjectName("norm_pushButton_2")
        self.delete_pushButton_2 = QtWidgets.QPushButton(self.tab_5)
        self.delete_pushButton_2.setGeometry(QtCore.QRect(220, 420, 93, 28))
        self.delete_pushButton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.delete_pushButton_2.setObjectName("delete_pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_5)
        self.radioButton.setGeometry(QtCore.QRect(220, 320, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_5)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 360, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.colcomboBox_3 = QtWidgets.QComboBox(self.tab)
        self.colcomboBox_3.setGeometry(QtCore.QRect(410, 80, 141, 31))
        self.colcomboBox_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.colcomboBox_3.setObjectName("colcomboBox_3")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setGeometry(QtCore.QRect(380, 0, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.textEdit_6.setPalette(palette)
        self.textEdit_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_6.setGeometry(QtCore.QRect(180, 180, 601, 301))
        self.textBrowser_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 130, 141, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.fileselection.clicked.connect(self.file_selection)
        self.completebutton.clicked.connect(self.missing_data_comp)
        self.deletebutton.clicked.connect(self.mising_data_delete)
        self.pushButton.clicked.connect(self.select_fonction)
        self.norm_pushButton_2.clicked.connect(self.outliner_norm)
        self.delete_pushButton_2.clicked.connect(self.outliner_delet)
        self.toplam = 0
        """integer niteliklerin ortalamasını hesaplamak için toplama yaparken kullanılan değişken"""
        self.lencolumns = 0
        """başka fonk. da kullnılmak için tanımlanan sutun sayısını tutar"""
        self.lenline = 0
        """her sutunun satır sayısı aynı olacağı için herhangi bir satırdaki sutun sayısını hesaplar"""
        self.lenIntcolumns = 0
        """integer veri tipindeki sutun sayısını tutar"""
        self.columns = []
        """sutunların isimlerini tutar"""
        self.intcolumns = []
        """integer veri tipindeki sutunları tutan liste"""
        self.intcolumns_name = []
        """integer değere ahpi sütunlerın isimlerini tutuyoruz"""
        self.allcolumns_name=[]
        """bütün kolonların ismini tutar"""
        self.mean = 0.0
        """tr__niteliklerin hangi türde değişkenlere sahip olduğunu tutan liste 
           eng__list holding what type of variables the attributes have"""
        self.dat = []
        """integer değerlere sahip niteliklerin toplamlarını tutar"""
        self.columsum = []
        """dosya yolunu kayıt ediyoruz"""
        self.csvfile = ''
        """eksik veri sayısını tutan değişken"""
        self.missing_values_count = 0
        """csv dosyası"""
        self.csvreader = ""
        """IQR değerini farklı fonksiyonlarda kullanmak için"""
        self.iqr = 0
        """çeyreklerin tanımlaması"""
        self.Q1 = 0
        self.Q3 = 0
        self.sayi=0
        """dosya seçiminde kullanılan değişkendir """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.fileselection.setText(_translate("MainWindow", "Select file"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">For more accurate</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">results, complete or delete</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">missing data.</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Data Completion"))
        self.compcomboBox.setItemText(0, _translate("MainWindow", "Mod"))
        self.compcomboBox.setItemText(1, _translate("MainWindow", "Mean"))
        self.compcomboBox.setItemText(2, _translate("MainWindow", "Median"))
        self.completebutton.setText(_translate("MainWindow", "Complete"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa0000;\">Deletion of missing data </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa0000;\">delete on a row basis</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Data Deletion"))
        self.deletebutton.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Preprocess"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">Select the column you want to process.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#aa0000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#aa0000;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Columns:"))
        self.precesscomboBox_2.setItemText(0, _translate("MainWindow", "Average"))
        self.precesscomboBox_2.setItemText(1, _translate("MainWindow", "Median"))
        self.precesscomboBox_2.setItemText(2, _translate("MainWindow", "Mode"))
        self.precesscomboBox_2.setItemText(3, _translate("MainWindow", "Frequency"))
        self.precesscomboBox_2.setItemText(4, _translate("MainWindow", "IQR"))
        self.precesscomboBox_2.setItemText(5, _translate("MainWindow", "Outliers"))
        self.precesscomboBox_2.setItemText(6, _translate("MainWindow", "Five Number Summary"))
        self.precesscomboBox_2.setItemText(7, _translate("MainWindow", "Box Plot"))
        self.precesscomboBox_2.setItemText(8, _translate("MainWindow", "Variance and Standard Deviation"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">Select the action you want to do</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Functions"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa0000;\">Select the action to delete or edit outliers.</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#aa0000;\">Perform normalization to organize outlier data. Do according to z-score or min-max normalizations. Select attributes for transactions. Enter the new min and max values ​​for min max normalization.</span></p></body></html>"))

        self.lineEdit.setText(_translate("MainWindow", "Normalization"))
        self.zscore_raido_button.setText(_translate("MainWindow", "Z-Score"))
        self.minmax_radio_button.setText(_translate("MainWindow", "Min-Max"))
        self.lineEdit_2.setText(_translate("MainWindow", "Deletion "))
        self.norm_pushButton_2.setText(_translate("MainWindow", "Normalize"))
        self.delete_pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.radioButton.setText(_translate("MainWindow", "Line"))
        self.radioButton_2.setText(_translate("MainWindow", "Column"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Sprocessing "))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa0000;\">Please choose which attribute you want to search.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Search"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
