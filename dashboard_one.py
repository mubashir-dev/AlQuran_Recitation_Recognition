# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1159, 671)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(180, 80, 961, 571))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("border:1px solid black;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 941, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:2px solid black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(500, 140, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(255, 157, 19);\n"
"padding:10px;")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(90, 140, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(255, 157, 19);\n"
"padding:10px;")
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(210, 230, 531, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(255, 157, 19);\n"
"padding:10px;")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 941, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:2px solid black;")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.page_3)
        self.frame.setGeometry(QtCore.QRect(10, 80, 941, 471))
        self.frame.setStyleSheet("border:2px solid;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 361, 471))
        self.frame_2.setStyleSheet("border:2px solid;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 341, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(0, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.surha_search_button = QtWidgets.QPushButton(self.frame_2)
        self.surha_search_button.setGeometry(QtCore.QRect(110, 70, 141, 121))
        self.surha_search_button.setStyleSheet("border:none;")
        self.surha_search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../icons/voice-recognition.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.surha_search_button.setIcon(icon)
        self.surha_search_button.setIconSize(QtCore.QSize(100, 100))
        self.surha_search_button.setObjectName("surha_search_button")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(10, 190, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("border:none;")
        self.label_24.setObjectName("label_24")
        self.surha_text = QtWidgets.QLabel(self.frame_2)
        self.surha_text.setGeometry(QtCore.QRect(10, 310, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.surha_text.setFont(font)
        self.surha_text.setStyleSheet("border:none;")
        self.surha_text.setObjectName("surha_text")
        self.surah_combobox = QtWidgets.QComboBox(self.frame_2)
        self.surah_combobox.setGeometry(QtCore.QRect(30, 250, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.surah_combobox.setFont(font)
        self.surah_combobox.setObjectName("surah_combobox")
        self.surah_combobox.addItem("")
        self.surah_combobox.addItem("")
        self.surah_combobox.addItem("")
        self.surah_combobox.addItem("")
        self.surha_what_you_said = QtWidgets.QLabel(self.frame_2)
        self.surha_what_you_said.setGeometry(QtCore.QRect(10, 360, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.surha_what_you_said.setFont(font)
        self.surha_what_you_said.setStyleSheet("border:none;\n"
"border-top:2px solid black;")
        self.surha_what_you_said.setObjectName("surha_what_you_said")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(370, 10, 561, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(0, 255, 0);")
        self.label_11.setObjectName("label_11")
        self.surah_matched_result = QtWidgets.QLabel(self.frame)
        self.surah_matched_result.setGeometry(QtCore.QRect(370, 80, 561, 371))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.surah_matched_result.setFont(font)
        self.surah_matched_result.setStyleSheet("border:none;\n"
"padding:5px;")
        self.surah_matched_result.setWordWrap(True)
        self.surah_matched_result.setObjectName("surah_matched_result")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_3 = QtWidgets.QLabel(self.page_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 941, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:2px solid black;")
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.page_4)
        self.frame_3.setGeometry(QtCore.QRect(10, 70, 941, 491))
        self.frame_3.setStyleSheet("border:2px solid;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 361, 491))
        self.frame_4.setStyleSheet("border:2px solid;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 331, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border:2px solid black;")
        self.label_14.setObjectName("label_14")
        self.ayah_speak = QtWidgets.QLabel(self.frame_4)
        self.ayah_speak.setGeometry(QtCore.QRect(10, 270, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ayah_speak.setFont(font)
        self.ayah_speak.setStyleSheet("border:none;")
        self.ayah_speak.setObjectName("ayah_speak")
        self.ayah_what_you_said = QtWidgets.QLabel(self.frame_4)
        self.ayah_what_you_said.setGeometry(QtCore.QRect(10, 350, 341, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ayah_what_you_said.setFont(font)
        self.ayah_what_you_said.setStyleSheet("border:none;\n"
"border-top:2px solid black;")
        self.ayah_what_you_said.setObjectName("ayah_what_you_said")
        self.combobox_ayah = QtWidgets.QComboBox(self.frame_4)
        self.combobox_ayah.setGeometry(QtCore.QRect(30, 210, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.combobox_ayah.setFont(font)
        self.combobox_ayah.setObjectName("combobox_ayah")
        self.combobox_ayah.addItem("")
        self.combobox_ayah.addItem("")
        self.combobox_ayah.addItem("")
        self.combobox_ayah.addItem("")
        self.ayah_search_button = QtWidgets.QPushButton(self.frame_4)
        self.ayah_search_button.setGeometry(QtCore.QRect(80, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ayah_search_button.setFont(font)
        self.ayah_search_button.setObjectName("ayah_search_button")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(370, 10, 561, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border:2px solid black;")
        self.label_16.setObjectName("label_16")
        self.ayah_matched_result = QtWidgets.QLabel(self.frame_3)
        self.ayah_matched_result.setGeometry(QtCore.QRect(370, 70, 561, 401))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ayah_matched_result.setFont(font)
        self.ayah_matched_result.setStyleSheet("border:none;\n"
"padding:5px;")
        self.ayah_matched_result.setWordWrap(True)
        self.ayah_matched_result.setObjectName("ayah_matched_result")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_2 = QtWidgets.QLabel(self.page_5)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 941, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:2px solid black;")
        self.label_2.setObjectName("label_2")
        self.frame_5 = QtWidgets.QFrame(self.page_5)
        self.frame_5.setGeometry(QtCore.QRect(10, 80, 941, 471))
        self.frame_5.setStyleSheet("border:2px solid;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 921, 451))
        self.label_17.setStyleSheet("padding:10px;\n"
"border:none;\n"
"")
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 941, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border:2px solid black;")
        self.label_9.setObjectName("label_9")
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 941, 491))
        self.label_18.setStyleSheet("padding:10px;\n"
"border:2px solid;")
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 440, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border:2px solid black;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:2px solid black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 260, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border:2px solid black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 130, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:2px solid black;\n"
"background-color: rgb(255, 157, 19);\n"
"")
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.Urdu, QtCore.QLocale.Pakistan))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 380, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border:2px solid black;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 961, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:2px solid black;\n"
"border-color:green;\n"
"background-color: rgb(0, 255, 0);")
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 10, 141, 111))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border:none;")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../icons/quran.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(100, 90))
        self.pushButton_6.setObjectName("pushButton_6")
        self.btn_topic_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_topic_search.setGeometry(QtCore.QRect(10, 320, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.btn_topic_search.setFont(font)
        self.btn_topic_search.setStyleSheet("border:2px solid black;")
        self.btn_topic_search.setObjectName("btn_topic_search")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Al-Quran Recitation Recognition System"))
        self.label_5.setText(_translate("MainWindow", "DASHBOARD"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NO OF AYAHS 140</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TOTAL NO OF SURAHS 12</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NO OF RUKHS     44</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "SURAH SEARCH"))
        self.label_10.setText(_translate("MainWindow", "GIVE INPUT "))
        self.label_24.setText(_translate("MainWindow", "PRESS THE BUTTON AND THEN SPEAK!"))
        self.surha_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PLEASE SPEAK NOW!</p></body></html>"))
        self.surah_combobox.setItemText(0, _translate("MainWindow", "SELECT  YOUR LANGAUGE"))
        self.surah_combobox.setItemText(1, _translate("MainWindow", "ARABIC"))
        self.surah_combobox.setItemText(2, _translate("MainWindow", "URDU"))
        self.surah_combobox.setItemText(3, _translate("MainWindow", "ENGLISH"))
        self.surha_what_you_said.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">WHAT YOU SAID!</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "POSSIBILE RESULT"))
        self.surah_matched_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اس پوست سے ہیروئن بنتی ہے اور یہ سب سے زیادہ لت لگانے والی منشیات میں سے ایک ہے۔</span></p><p align=\"justify\"><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اقوام متحدہ میں منشیات کی غیر قانونی سمگلنگ کی نشاندہی کرنے اور اس سے نمٹنے کے ادارے یو این آو ڈی سی کے مطابق افغانستان میں پیدا ہونے والی پوست کا 80 فیصد حصہ ہلمند سمیت ملک کے جنوب مغربی حصوں سے آتا ہے۔</span></p><p align=\"justify\"><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اس کا مطلب ہے کہ دنیا بھر کی سپلائی کا دو تہائی حصہ۔ یہ وہ جگہ نہیں جو ملک کی معیشت کو کاربن سے پاک کرنے کی کوششوں میں سر فہرست دکھائی دیتی ہوں۔</span></p><p align=\"justify\"><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">لیکن جونہی میں نے یہ سولر پینل دیکھا اس کے بعد مجھے اور بھی دکھائی دیے۔ بلکہ درحقیقت وہاں ہر کھیت کے پاس سولر پینل کی قطاریں تھیں اور یہ سنہ 2016 تھا۔</span><span style=\" font-family:\'Times New Roman\'; font-size:16px; color:#000000;\"><br/></span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "AYAH SEARCH"))
        self.label_14.setText(_translate("MainWindow", "GIVE INPUT "))
        self.ayah_speak.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PLEASE SPEAK NOW!</p></body></html>"))
        self.ayah_what_you_said.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">WHAT YOU SAID!</p></body></html>"))
        self.combobox_ayah.setItemText(0, _translate("MainWindow", "SELECT  YOUR LANGAUGE"))
        self.combobox_ayah.setItemText(1, _translate("MainWindow", "ARABIC"))
        self.combobox_ayah.setItemText(2, _translate("MainWindow", "URDU"))
        self.combobox_ayah.setItemText(3, _translate("MainWindow", "ENGLISH"))
        self.ayah_search_button.setText(_translate("MainWindow", "SPEAK UP"))
        self.label_16.setText(_translate("MainWindow", "BEST MATCHED RESULT"))
        self.ayah_matched_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Times New Roman\'; font-size:16px; color:#000000;\">DESIRED TEXT</span></p><p align=\"justify\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "SYSTEM WORKING"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اس پوست سے ہیروئن بنتی ہے اور یہ سب سے زیادہ لت لگانے والی منشیات میں سے ایک ہے۔</span></p><p><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اقوام متحدہ میں منشیات کی غیر قانونی سمگلنگ کی نشاندہی کرنے اور اس سے نمٹنے کے ادارے یو این آو ڈی سی کے مطابق افغانستان میں پیدا ہونے والی پوست کا 80 فیصد حصہ ہلمند سمیت ملک کے جنوب مغربی حصوں سے آتا ہے۔</span></p><p><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اس کا مطلب ہے کہ دنیا بھر کی سپلائی کا دو تہائی حصہ۔ یہ وہ جگہ نہیں جو ملک کی معیشت کو کاربن سے پاک کرنے کی کوششوں میں سر فہرست دکھائی دیتی ہوں۔</span></p><p><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">لیکن جونہی میں نے یہ سولر پینل دیکھا اس کے بعد مجھے اور بھی دکھائی دیے۔ بلکہ درحقیقت وہاں ہر کھیت کے پاس سولر پینل کی قطاریں تھیں اور یہ سنہ 2016 تھا۔</span></p><p><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">اور یہ دور حاضر میں ہیروئن کی پیداوار میں آنے والے انقلاب کا تعین کر رہا تھا اور جس کا میں غیر دانستہ طور پر شاہد بنا۔ صرف میں فرد واحد نہیں تھا جس نے یہ بات نوٹس کی کہ افغان کاشتکار کم سے کم کاربن والی ٹیکنالوجی میں دلچسپی لے رہے ہیں۔</span></p><h2 dir=\"rtl\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fdfdfd;\"><a name=\"-خلا-سے-ملنے-والے-شواہد-\"/><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:x-large; font-weight:696; color:#3f3f42;\">خ</span><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:x-large; font-weight:696; color:#3f3f42;\">لا سے ملنے والے شواہد</span></h2><p><span style=\" font-family:\'BBC Nassim Urdu\'; font-size:16px; color:#3f3f42;\">انگلینڈ کے جنوب میں گلڈ فورڈ کے علاقے میں رچرڈ بریٹن اپنے دفتر میں کمپیوٹر پر جھکے ہوئے ہیں۔</span></p><p><span style=\" font-family:\'Times New Roman\'; font-size:16px; color:#000000;\"><br/></span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "SEARCH BY TOPIC"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; vertical-align:super;\">Available in Second Iteration</span></p><p align=\"center\"><span style=\" font-size:36pt; vertical-align:super;\">Under Developmental Process</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_2.setText(_translate("MainWindow", "SURAH SEARCH"))
        self.pushButton_3.setText(_translate("MainWindow", "AYAH SEARCH"))
        self.pushButton.setText(_translate("MainWindow", "DASHBOARD"))
        self.pushButton_4.setText(_translate("MainWindow", "WORKING"))
        self.label.setText(_translate("MainWindow", "AL-QURAN RECITATION RECOGNITION SYSTEM "))
        self.btn_topic_search.setText(_translate("MainWindow", "TOPIC SEARCH"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())