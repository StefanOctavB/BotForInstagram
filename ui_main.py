# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainBQFdob.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    # def openWindow
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 0))
        MainWindow.setMaximumSize(QSize(16777215, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 0))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setMinimumSize(QSize(500, 30))
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 0.9), stop:0.555556 rgba(28, 29, 73, 0.9));\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout = QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(1, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(500, 0))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.title_bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setLayoutDirection(Qt.RightToLeft)
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 10))
        font = QFont()
        font.setFamily(u"Roboto Medium")
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_title)


        self.verticalLayout.addWidget(self.frame_title)


        self.drop_shadow_layout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setMinimumSize(QSize(500, 0))
        self.content_bar.setStyleSheet(u"background-color:none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pagina_Start = QWidget()
        self.pagina_Start.setObjectName(u"pagina_Start")
        self.verticalLayout_8 = QVBoxLayout(self.pagina_Start)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_main = QFrame(self.pagina_Start)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_main)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.frame_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(18)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.accoutsDropDown = QComboBox(self.frame_main)
        self.accoutsDropDown.setObjectName(u"accoutsDropDown")

        self.verticalLayout_9.addWidget(self.accoutsDropDown)

        self.frame_accountOverview = QFrame(self.frame_main)
        self.frame_accountOverview.setObjectName(u"frame_accountOverview")
        self.frame_accountOverview.setFrameShape(QFrame.StyledPanel)
        self.frame_accountOverview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_accountOverview)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_accountPhoto = QFrame(self.frame_accountOverview)
        self.frame_accountPhoto.setObjectName(u"frame_accountPhoto")
        self.frame_accountPhoto.setLayoutDirection(Qt.LeftToRight)
        self.frame_accountPhoto.setFrameShape(QFrame.NoFrame)
        self.frame_accountPhoto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_accountPhoto)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_accountPhoto = QLabel(self.frame_accountPhoto)
        self.label_accountPhoto.setObjectName(u"label_accountPhoto")
        self.label_accountPhoto.setMaximumSize(QSize(50, 50))
        self.label_accountPhoto.setPixmap(QPixmap(u"assets/insta_logo.png"))
        self.label_accountPhoto.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_accountPhoto)


        self.verticalLayout_19.addWidget(self.frame_accountPhoto)

        self.label_accountUsername = QLabel(self.frame_accountOverview)
        self.label_accountUsername.setObjectName(u"label_accountUsername")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(14)
        self.label_accountUsername.setFont(font2)
        self.label_accountUsername.setStyleSheet(u"color: #fff;\n"
"")
        self.label_accountUsername.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_accountUsername)


        self.verticalLayout_9.addWidget(self.frame_accountOverview)

        self.frame_5 = QFrame(self.frame_main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buton_adaugaContNou = QPushButton(self.frame_5)
        self.buton_adaugaContNou.setObjectName(u"buton_adaugaContNou")
        self.buton_adaugaContNou.setMinimumSize(QSize(120, 30))
        self.buton_adaugaContNou.setMaximumSize(QSize(200, 30))
        self.buton_adaugaContNou.setFont(font2)
        self.buton_adaugaContNou.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton_adaugaContNou.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.buton_adaugaContNou)

        self.buton_adaugaContNou_3 = QPushButton(self.frame_5)
        self.buton_adaugaContNou_3.setObjectName(u"buton_adaugaContNou_3")
        self.buton_adaugaContNou_3.setMinimumSize(QSize(120, 30))
        self.buton_adaugaContNou_3.setMaximumSize(QSize(200, 30))
        self.buton_adaugaContNou_3.setFont(font2)
        self.buton_adaugaContNou_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton_adaugaContNou_3.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.buton_adaugaContNou_3)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_main)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.frame_15)
        self.radioButton.setObjectName(u"radioButton")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        self.radioButton.setFont(font3)
        self.radioButton.setStyleSheet(u"color: #fff;\n"
"")

        self.verticalLayout_13.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_15)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font3)
        self.radioButton_2.setStyleSheet(u"color: #fff;\n"
"")

        self.verticalLayout_13.addWidget(self.radioButton_2)


        self.verticalLayout_14.addWidget(self.frame_15)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_16 = QFrame(self.frame_main)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.button_Next = QPushButton(self.frame_16)
        self.button_Next.setObjectName(u"button_Next")
        self.button_Next.setMinimumSize(QSize(80, 30))
        self.button_Next.setMaximumSize(QSize(80, 30))
        self.button_Next.setFont(font2)
        self.button_Next.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_Next.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_12.addWidget(self.button_Next)


        self.verticalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_8.addWidget(self.frame_main)

        self.stackedWidget.addWidget(self.pagina_Start)
        self.pagina_AdaugareContNou = QWidget()
        self.pagina_AdaugareContNou.setObjectName(u"pagina_AdaugareContNou")
        self.verticalLayout_6 = QVBoxLayout(self.pagina_AdaugareContNou)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.pagina_AdaugareContNou)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username = QTextEdit(self.frame_3)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(300, 30))
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.username.setFont(font4)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.username)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 120))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.password = QTextEdit(self.frame_9)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(300, 30))
        self.password.setFont(font4)
        self.password.setLayoutDirection(Qt.LeftToRight)
        self.password.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.password)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_backFromAddAccount = QPushButton(self.frame_4)
        self.button_backFromAddAccount.setObjectName(u"button_backFromAddAccount")
        self.button_backFromAddAccount.setMinimumSize(QSize(120, 30))
        self.button_backFromAddAccount.setMaximumSize(QSize(120, 30))
        self.button_backFromAddAccount.setFont(font2)
        self.button_backFromAddAccount.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_backFromAddAccount.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.button_backFromAddAccount)

        self.button_addAccount = QPushButton(self.frame_4)
        self.button_addAccount.setObjectName(u"button_addAccount")
        self.button_addAccount.setMinimumSize(QSize(120, 30))
        self.button_addAccount.setMaximumSize(QSize(120, 30))
        self.button_addAccount.setFont(font2)
        self.button_addAccount.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_addAccount.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.button_addAccount)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.pagina_AdaugareContNou)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.drop_shadow_layout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(30, 0))
        self.credits_bar.setMaximumSize(QSize(16777212, 30))
        self.credits_bar.setStyleSheet(u"background-color:none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font5 = QFont()
        font5.setFamily(u"Roboto Light")
        font5.setPointSize(8)
        self.label_credits.setFont(font5)
        self.label_credits.setStyleSheet(u"color:rgb(128,102,168);")
        self.label_credits.setTextFormat(Qt.PlainText)

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_5.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding:5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_grip)


        self.drop_shadow_layout.addWidget(self.credits_bar)


        self.horizontalLayout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"INSTAGRAM BOOT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select the account to be used:", None))
        self.label_accountPhoto.setText("")
        self.label_accountUsername.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.buton_adaugaContNou.setText(QCoreApplication.translate("MainWindow", u"Add another account", None))
        self.buton_adaugaContNou_3.setText(QCoreApplication.translate("MainWindow", u"Remove account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Chose the action to perform:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Get followers from another user", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Unfollow users that are not following you ", None))
        self.button_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.button_backFromAddAccount.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_addAccount.setText(QCoreApplication.translate("MainWindow", u"Add account", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Crafted by: Cyber-Octopus", None))
    # retranslateUi

