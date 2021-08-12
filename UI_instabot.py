# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maintzTBRg.ui'
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
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(610, 450)
        MainWindow.setMinimumSize(QSize(610, 450))
        MainWindow.setMaximumSize(QSize(610, 450))
        icon = QIcon()
        icon.addFile(u"assets/insta_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(610, 450))
        self.centralwidget.setMaximumSize(QSize(610, 450))
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setGeometry(QRect(0, 0, 610, 450))
        self.drop_shadow_frame.setMinimumSize(QSize(610, 450))
        self.drop_shadow_frame.setMaximumSize(QSize(610, 450))
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 0.9), stop:0.555556 rgba(28, 29, 73, 0.9));\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout = QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
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

        self.drop_shadow_layout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setMinimumSize(QSize(610, 0))
        self.content_bar.setMaximumSize(QSize(610, 16777215))
        self.content_bar.setStyleSheet(u"background-color:none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pagina_Start = QWidget()
        self.pagina_Start.setObjectName(u"pagina_Start")
        self.verticalLayout_8 = QVBoxLayout(self.pagina_Start)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.pagina_Start)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_main)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.accoutsDropDown = QComboBox(self.frame_main)
        self.accoutsDropDown.setObjectName(u"accoutsDropDown")
        self.accoutsDropDown.setMinimumSize(QSize(0, 25))
        self.accoutsDropDown.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_9.addWidget(self.accoutsDropDown)

        self.frame_accountOverview = QFrame(self.frame_main)
        self.frame_accountOverview.setObjectName(u"frame_accountOverview")
        self.frame_accountOverview.setFrameShape(QFrame.NoFrame)
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
        self.label_accountPhoto.setStyleSheet(u"border-radius:25px;")
        self.label_accountPhoto.setPixmap(QPixmap(u"assets/insta_logo.png"))
        self.label_accountPhoto.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_accountPhoto)


        self.verticalLayout_19.addWidget(self.frame_accountPhoto)

        self.label_accountUsername = QLabel(self.frame_accountOverview)
        self.label_accountUsername.setObjectName(u"label_accountUsername")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.label_accountUsername.setFont(font1)
        self.label_accountUsername.setStyleSheet(u"color: #fff;\n"
"")
        self.label_accountUsername.setScaledContents(True)
        self.label_accountUsername.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_accountUsername)


        self.verticalLayout_9.addWidget(self.frame_accountOverview)

        self.frame_5 = QFrame(self.frame_main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.buton_adaugaContNou = QPushButton(self.frame_5)
        self.buton_adaugaContNou.setObjectName(u"buton_adaugaContNou")
        self.buton_adaugaContNou.setMinimumSize(QSize(120, 30))
        self.buton_adaugaContNou.setMaximumSize(QSize(200, 30))
        self.buton_adaugaContNou.setFont(font1)
        self.buton_adaugaContNou.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton_adaugaContNou.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.buton_adaugaContNou)

        self.buton_stergeCont = QPushButton(self.frame_5)
        self.buton_stergeCont.setObjectName(u"buton_stergeCont")
        self.buton_stergeCont.setMinimumSize(QSize(120, 30))
        self.buton_stergeCont.setMaximumSize(QSize(200, 30))
        self.buton_stergeCont.setFont(font1)
        self.buton_stergeCont.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton_stergeCont.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_4.addWidget(self.buton_stergeCont)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_main)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_4)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.radio_button_getFollowers = QRadioButton(self.frame_15)
        self.radio_button_getFollowers.setObjectName(u"radio_button_getFollowers")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(12)
        self.radio_button_getFollowers.setFont(font2)
        self.radio_button_getFollowers.setStyleSheet(u"color: #fff;\n"
"")

        self.verticalLayout_13.addWidget(self.radio_button_getFollowers)

        self.radio_button_unfollow = QRadioButton(self.frame_15)
        self.radio_button_unfollow.setObjectName(u"radio_button_unfollow")
        self.radio_button_unfollow.setFont(font2)
        self.radio_button_unfollow.setStyleSheet(u"color: #fff;\n"
"")

        self.verticalLayout_13.addWidget(self.radio_button_unfollow)

        self.radio_autoPost = QRadioButton(self.frame_15)
        self.radio_autoPost.setObjectName(u"radio_autoPost")
        self.radio_autoPost.setFont(font2)
        self.radio_autoPost.setStyleSheet(u"color: #fff;\n"
"")

        self.verticalLayout_13.addWidget(self.radio_autoPost)


        self.verticalLayout_14.addWidget(self.frame_15)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_16 = QFrame(self.frame_main)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.button_Next = QPushButton(self.frame_16)
        self.button_Next.setObjectName(u"button_Next")
        self.button_Next.setMinimumSize(QSize(80, 30))
        self.button_Next.setMaximumSize(QSize(80, 30))
        self.button_Next.setFont(font1)
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
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.username = QTextEdit(self.frame_3)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(300, 30))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.username.setFont(font3)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.username)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 120))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.password = QTextEdit(self.frame_9)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(300, 30))
        self.password.setFont(font3)
        self.password.setLayoutDirection(Qt.LeftToRight)
        self.password.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.password)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.button_backFromAddAccount = QPushButton(self.frame_4)
        self.button_backFromAddAccount.setObjectName(u"button_backFromAddAccount")
        self.button_backFromAddAccount.setMinimumSize(QSize(120, 30))
        self.button_backFromAddAccount.setMaximumSize(QSize(120, 30))
        self.button_backFromAddAccount.setFont(font1)
        self.button_backFromAddAccount.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_backFromAddAccount.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.button_backFromAddAccount)

        self.button_addAccount = QPushButton(self.frame_4)
        self.button_addAccount.setObjectName(u"button_addAccount")
        self.button_addAccount.setMinimumSize(QSize(120, 30))
        self.button_addAccount.setMaximumSize(QSize(120, 30))
        self.button_addAccount.setFont(font1)
        self.button_addAccount.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_addAccount.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.button_addAccount)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.pagina_AdaugareContNou)
        self.pagina_getFollowers = QWidget()
        self.pagina_getFollowers.setObjectName(u"pagina_getFollowers")
        self.verticalLayout_12 = QVBoxLayout(self.pagina_getFollowers)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.pagina_getFollowers)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 120))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountNameToGetFollowers = QTextEdit(self.frame_10)
        self.accountNameToGetFollowers.setObjectName(u"accountNameToGetFollowers")
        self.accountNameToGetFollowers.setMaximumSize(QSize(300, 30))
        self.accountNameToGetFollowers.setFont(font3)
        self.accountNameToGetFollowers.setLayoutDirection(Qt.LeftToRight)
        self.accountNameToGetFollowers.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.accountNameToGetFollowers)


        self.verticalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.pagina_getFollowers)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 160))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_6)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.numberOfFollowers = QTextEdit(self.frame_13)
        self.numberOfFollowers.setObjectName(u"numberOfFollowers")
        self.numberOfFollowers.setMaximumSize(QSize(300, 30))
        self.numberOfFollowers.setFont(font3)
        self.numberOfFollowers.setLayoutDirection(Qt.LeftToRight)
        self.numberOfFollowers.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.numberOfFollowers)


        self.verticalLayout_11.addWidget(self.frame_13)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.pagina_getFollowers)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_7)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_18)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(150, 0, 50, 0)
        self.radioButton_HeadlessYes = QRadioButton(self.frame_18)
        self.radioButton_HeadlessYes.setObjectName(u"radioButton_HeadlessYes")
        self.radioButton_HeadlessYes.setFont(font2)
        self.radioButton_HeadlessYes.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_HeadlessYes.setStyleSheet(u"color:#fff;")

        self.horizontalLayout.addWidget(self.radioButton_HeadlessYes)

        self.radioButton_HeadlessNo = QRadioButton(self.frame_18)
        self.radioButton_HeadlessNo.setObjectName(u"radioButton_HeadlessNo")
        self.radioButton_HeadlessNo.setFont(font2)
        self.radioButton_HeadlessNo.setStyleSheet(u"color:#fff;")

        self.horizontalLayout.addWidget(self.radioButton_HeadlessNo)


        self.verticalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_16.addWidget(self.frame_17)


        self.verticalLayout_12.addWidget(self.frame_14)

        self.frame_11 = QFrame(self.pagina_getFollowers)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_backFromGetFollowers = QPushButton(self.frame_11)
        self.button_backFromGetFollowers.setObjectName(u"button_backFromGetFollowers")
        self.button_backFromGetFollowers.setMinimumSize(QSize(120, 30))
        self.button_backFromGetFollowers.setMaximumSize(QSize(120, 30))
        self.button_backFromGetFollowers.setFont(font1)
        self.button_backFromGetFollowers.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_backFromGetFollowers.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_8.addWidget(self.button_backFromGetFollowers)

        self.button_startGetFollowers = QPushButton(self.frame_11)
        self.button_startGetFollowers.setObjectName(u"button_startGetFollowers")
        self.button_startGetFollowers.setMinimumSize(QSize(120, 30))
        self.button_startGetFollowers.setMaximumSize(QSize(120, 30))
        self.button_startGetFollowers.setFont(font1)
        self.button_startGetFollowers.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_startGetFollowers.setStyleSheet(u"background-color:rgba(60, 231, 195,0.8); color:#FFF;\n"
"border-radius:10px;")

        self.horizontalLayout_8.addWidget(self.button_startGetFollowers)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.pagina_getFollowers)
        self.pagina_startGettingFollowers = QWidget()
        self.pagina_startGettingFollowers.setObjectName(u"pagina_startGettingFollowers")
        self.frame_19 = QFrame(self.pagina_startGettingFollowers)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(170, 60, 200, 300))
        self.frame_19.setMinimumSize(QSize(200, 300))
        self.frame_19.setMaximumSize(QSize(200, 300))
        self.frame_19.setStyleSheet(u"background:transparent;\n"
"background-color:rgba(255,255,255,0.1)")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_19)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(200, 100))
        self.frame_20.setMaximumSize(QSize(200, 100))
        self.frame_20.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 0.9), stop:0.555556 rgba(28, 29, 73, 0.9));")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color:none;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.targetAccountName = QLabel(self.frame_21)
        self.targetAccountName.setObjectName(u"targetAccountName")
        self.targetAccountName.setFont(font1)
        self.targetAccountName.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"background-color:none;")
        self.targetAccountName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.targetAccountName)

        self.label_8 = QLabel(self.frame_21)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_9)


        self.verticalLayout_20.addWidget(self.frame_21)


        self.verticalLayout_18.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(200, 200))
        self.frame_22.setMaximumSize(QSize(200, 200))
        self.frame_22.setStyleSheet(u"border: 5px solid transparent;\n"
"border-radius:100px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #8e2de2, stop:0.555556 #4a00e0);\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_22)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(20, 15, 20, 35)
        self.targetAccountName_2 = QLabel(self.frame_22)
        self.targetAccountName_2.setObjectName(u"targetAccountName_2")
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(16)
        self.targetAccountName_2.setFont(font4)
        self.targetAccountName_2.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color:none;")
        self.targetAccountName_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.targetAccountName_2)

        self.targetAccountName_3 = QLabel(self.frame_22)
        self.targetAccountName_3.setObjectName(u"targetAccountName_3")
        font5 = QFont()
        font5.setFamily(u"Roboto")
        font5.setPointSize(28)
        self.targetAccountName_3.setFont(font5)
        self.targetAccountName_3.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color:none;")
        self.targetAccountName_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.targetAccountName_3)

        self.targetAccountName_4 = QLabel(self.frame_22)
        self.targetAccountName_4.setObjectName(u"targetAccountName_4")
        self.targetAccountName_4.setFont(font2)
        self.targetAccountName_4.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color:none;")
        self.targetAccountName_4.setAlignment(Qt.AlignCenter)
        self.targetAccountName_4.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.targetAccountName_4)


        self.verticalLayout_18.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.pagina_startGettingFollowers)

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
        font6 = QFont()
        font6.setFamily(u"Roboto Light")
        font6.setPointSize(8)
        self.label_credits.setFont(font6)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"InstaBot", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select the account to be used:", None))
        self.label_accountPhoto.setText("")
        self.label_accountUsername.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.buton_adaugaContNou.setText(QCoreApplication.translate("MainWindow", u"Add new account", None))
        self.buton_stergeCont.setText(QCoreApplication.translate("MainWindow", u"Remove account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Chose the action to perform:", None))
        self.radio_button_getFollowers.setText(QCoreApplication.translate("MainWindow", u"Get followers from another user", None))
        self.radio_button_unfollow.setText(QCoreApplication.translate("MainWindow", u"Unfollow users that are not following you ", None))
        self.radio_autoPost.setText(QCoreApplication.translate("MainWindow", u"Automatically posting", None))
        self.button_Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.button_backFromAddAccount.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_addAccount.setText(QCoreApplication.translate("MainWindow", u"Add account", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name of target account:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"How many followers to follow\n"
" (leave blank to follow all):", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Do you want to see what the bot is doing?", None))
        self.radioButton_HeadlessYes.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.radioButton_HeadlessNo.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.button_backFromGetFollowers.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_startGetFollowers.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.targetAccountName.setText(QCoreApplication.translate("MainWindow", u"asdsadsaddsad", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"2000 following", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2000 followers", None))
        self.targetAccountName_2.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.targetAccountName_3.setText(QCoreApplication.translate("MainWindow", u"1/5", None))
        self.targetAccountName_4.setText(QCoreApplication.translate("MainWindow", u"Scroll the followers list", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Crafted by: Cyber-Octopus", None))
    # retranslateUi

