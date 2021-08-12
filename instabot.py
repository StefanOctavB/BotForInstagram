from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys
from UI_instabot import Ui_MainWindow
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import socket
import sqlite3
import time
from random import randint
from PyQt5.QtCore import QObject,QThread,pyqtSignal
#############################################
#                                           #
#      IMPORTS FOR MACOS BIG SUR            #
#                                           #
#############################################
# import matplotlib
# import matplotlib.pyplot as plt
#
# matplotlib.use('TkAgg')
#############################################
#                                           #
#     END - IMPORTS FOR MACOS BIG SUR       #
#                                           #
#############################################


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #############################################
        #                                           #
        #      FUNCTIONS TO CALL BEFORE OPEN UI     #
        #                                           #
        #############################################
        checkInternet()
        self.populateUsersDropDown()
        self.arataPozaUser()
        #############################################
        #                                           #
        #          SHOW THE MAIN WINDOW             #
        #                                           #
        #############################################
        self.ui.stackedWidget.setCurrentIndex(0)
        self.show()
        #############################################
        #                                           #
        #          LINK ACTIONS TO BUTTONS          #
        #                                           #
        #############################################
        self.ui.buton_adaugaContNou.clicked.connect(self.addAccount)
        self.ui.buton_stergeCont.clicked.connect(self.removeAccountButton)
        self.ui.button_backFromAddAccount.clicked.connect(self.backToMainWindow)
        self.ui.button_backFromGetFollowers.clicked.connect(self.backToMainWindow)
        self.ui.button_addAccount.clicked.connect(self.addAccountButton)
        self.ui.accoutsDropDown.currentIndexChanged.connect(self.showSelectedUserUI)
        self.ui.button_Next.clicked.connect(self.clickNext)
        self.ui.button_startGetFollowers.clicked.connect(self.startFollowingTargetFollowers)
    #############################################
    #                                           #
    #    FUNCTIONS THAT ARE USING THE UI        #
    #                                           #
    #############################################
    def populateUsersDropDown(self):
        self.ui.accoutsDropDown.clear()
        users = getAllUsersFromDB()
        print(users, type(users))
        for user in users:
            self.ui.accoutsDropDown.addItem(user[0])
        if self.ui.accoutsDropDown.count() == 0:
            self.ui.frame_accountOverview.hide()
            self.ui.buton_stergeCont.hide()
        else:
            self.ui.frame_accountOverview.show()
            self.ui.buton_stergeCont.show()
    def arataPozaUser(self):
        numePoza = "pictures/" + self.ui.accoutsDropDown.currentText() + ".png"
        pixmap = QPixmap(numePoza)
        self.ui.label_accountPhoto.setPixmap(pixmap)
    def addAccount(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def backToMainWindow(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def addAccountButton(self):
        username = self.ui.username.toPlainText()
        password = self.ui.password.toPlainText()
        if not username:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "Username was not provided\nPlease insert both username and password")
            msgBox1.setWindowTitle("Credentials error")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
        elif not password:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "Password was not provided\nPlease insert both username and password")
            msgBox1.setWindowTitle("Credentials error")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
        else:
            newAccount = igAccount(username, password)
            newAccount.checkPassword(newAccount.username, newAccount.password)
            self.populateUsersDropDown()
            self.ui.stackedWidget.setCurrentIndex(0)
    def showSelectedUserUI(self):
        account = self.ui.accoutsDropDown.currentText()
        self.ui.label_accountUsername.setText("@" + account)
        self.arataPozaUser()
    def clickNext(self):
        if self.ui.radio_button_getFollowers.isChecked():
            self.ui.stackedWidget.setCurrentIndex(2)
        elif self.ui.radio_button_unfollow.isChecked():
            print("nimic inca")
        else:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "Plese select the action to perform")
            msgBox1.setWindowTitle("No action selected")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
    def checkSelectedAccount(self):
        try:
            selectedAccount = self.ui.accoutsDropDown.currentText()
            conn = sqlite3.connect("accounts.db")
            c = conn.cursor()
            c.execute("SELECT * FROM accounts WHERE accountName LIKE '%" + selectedAccount + "%'")
            account = c.fetchall()
            usedAccount = igAccount(account[0][1], account[0][2])
            return usedAccount
        except Exception as e:
            print(e)
    def checkInputForGetFollowers(self):
        targetAccount = self.ui.accountNameToGetFollowers.toPlainText()
        numerOfActions = self.ui.numberOfFollowers.toPlainText()
        if not targetAccount:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "Please insert the name of target account")
            msgBox1.setWindowTitle("No target account specified")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
            return False
        elif not numerOfActions:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "All the followers will be followed")
            msgBox1.setWindowTitle("All followers")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
            return True
        elif numerOfActions.isnumeric():
            followersNumber = self.ui.numberOfFollowers.toPlainText()
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "First " + followersNumber + " followers from the followers list will be followed")
            msgBox1.setWindowTitle(followersNumber + "followers")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
            return True

    def workerFinished(self):
        self.ui.targetAccountName_2.setText("FINISHED")
    def workerStarted(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def startFollowingTargetFollowers(self):
        try:
            self.ui.stackedWidget.setCurrentIndex(3)
            driver = webdriver.Chrome(executable_path="chromedriver.exe")
            account = self.checkSelectedAccount()
            if self.checkInputForGetFollowers():
                if self.ui.radioButton_HeadlessYes.isChecked():
                    driver = setupHeadlessDriver()
                elif self.ui.radioButton_HeadlessNo.isChecked():
                    driver = webdriver.Chrome(executable_path="chromedriver.exe")
                else:
                    msgBox1 = QMessageBox()
                    msgBox1.setIcon(QMessageBox.Information)
                    msgBox1.setText(
                            "Please select if you want to see what the bot is doing or not.")
                    msgBox1.setWindowTitle("Selection required")
                    msgBox1.setStandardButtons(QMessageBox.Ok)
                    msgBox1.exec()
                    return False
                self.ui.targetAccountName_4.setText("Try to log in the ", account[0], " account")
            self.obj1 = followFollowersObject(account)
            self.objThread1 = QThread()
            self.obj1.moveToThread(self.objThread1)
            self.obj1.finished.connect(self.objThread1.quit) #when we emit the finish signal from QObject, will trigger the Quit() method of Thread to kill it
            self.obj1.sendTextSignal.connect(self.ui.targetAccountName_2.setText)
            self.objThread1.started.connect(login(driver,account.username,account.password))
            self.objThread1.start()
        except Exception as e:
            print(e)
    def scrollFollowersList(self,driver):
        scroll_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]")))
        usersLoadedInList = scroll_box.find_elements_by_tag_name("li")
        numerOfActions = self.ui.numberOfFollowers.toPlainText()
        if not numerOfActions:
            # All the followers will be followed
            last_ht, ht = 0, 1
            # getFollowersUI.targetAccountName_4.setText("Start scrolling go get x followers ")
            while last_ht != ht:
                last_ht = ht
                timp = randint(1, 5)
                time.sleep(timp)
                ht = driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                   return arguments[0].scrollHeight;
                                   """, scroll_box)
                print("Scrolling...", ht)
        print("Finished scrolling ")
    def removeAccountButton(self):
        try:
            account = self.ui.accoutsDropDown.currentText()
            conn = sqlite3.connect("accounts.db")
            c = conn.cursor()
            c.execute("DELETE from accounts WHERE accountName LIKE '%" + account + "%'")
            conn.commit()
            c.close()
            conn.close()
        except Exception as e:
            print(e)
        self.populateUsersDropDown()

def startPushingFollowButton(driver):
    buttons = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
    numberToFollow = len(buttons)
    print("There are ", numberToFollow, " accounts to be followed")
    # getFollowersUI.targetAccountName_4.setText("Starting to follow " + numberToFollow + " accounts")
    time.sleep(2)
    for i in range(len(buttons)):
        if buttons[i].text == 'Follow':
            # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
            driver.execute_script("arguments[0].click();", buttons[i])
            print("Followed ", i+1 ,"/",numberToFollow)
            timp = randint(1, 4)
            # getFollowersUI.targetAccountName_4.setText("Following " + i + "/" + numberToFollow + " accounts")
            time.sleep(timp)
def goToTargetPage(driver,numeCont):
    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
    search.clear()
    search.send_keys(numeCont)
    timp = randint(5, 15)
    time.sleep(timp)
    search.send_keys(Keys.ENTER)
    timp = randint(2, 5)
    time.sleep(timp)
    search.send_keys(Keys.ENTER)
    timp = randint(2, 5)
    time.sleep(timp)
    print("I'm on ", numeCont ," profile")
def openFollowersList(driver):
    timp = randint(1, 4)
    time.sleep(timp)
    followers = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))).click()
    # sugestions = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//h4[contains(text(), Suggestions)]")))
    # driver.execute_script('arguments[0].scrollIntoView()', sugestions)
    timp = randint(5, 15)
    time.sleep(timp)
    print("Followers list opened")
def getAllUsersFromDB():
    conn = sqlite3.connect("accounts.db")
    c = conn.cursor()
    users=[]
    c.execute("SELECT * FROM accounts")
    rows = c.fetchall()
    for row in rows:
        users.append(row)
    c.close()
    conn.close()
    return users
def checkInternet():
    try:
        socket.create_connection(('google.com',80))
        print("DADADA")
        return True
    except OSError:
        msgBox1 = QMessageBox()
        msgBox1.setIcon(QMessageBox.Information)
        msgBox1.setText(
            "No internet connection\nPlease connect to internet and try again")
        msgBox1.setWindowTitle("No internet connection")
        msgBox1.setStandardButtons(QMessageBox.Ok)
        msgBox1.exec()
        return False
def setupHeadlessDriver():
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        return driver
def login(driver,username,password):
    driver.get('https://www.instagram.com/')
    time.sleep(1.2)
    print("I'm on instagram.com")
    acceptCookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))).click()
    print("Accepted cookies")
    time.sleep(0.6)
    usernameInput = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    passwordInput = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    usernameInput.clear()
    passwordInput.clear()
    usernameInput.send_keys(username)
    passwordInput.send_keys(password)
    print("Username and password inserted")
    currentUrl = driver.current_url
    time.sleep(1.2)
    log_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    return currentUrl
def saveImage(driver,imageName):
    # Save the profile picture in pictures directory
    try:
        image = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/div/div/div/button/img')
    except Exception as e:
        if isinstance(e, NoSuchElementException):
            image = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/div/div/span/img')
        else:
            print(e)
    with open(imageName, 'wb') as file:
        file.write(image.screenshot_as_png)
def convertPic(imageName):
    filename = imageName
    with open(filename, 'rb') as file:
        photo = file.read()
    return photo

class igAccount:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def checkPassword(self,username,password):
        driver = setupHeadlessDriver()
        currentUrl = login(driver,username,password)
        time.sleep(6)
        afterLoginUrl = driver.current_url
        if currentUrl == afterLoginUrl:
            msgBox1 = QMessageBox()
            msgBox1.setIcon(QMessageBox.Information)
            msgBox1.setText(
                "The password inserted is wrong\nPlease try again")
            msgBox1.setWindowTitle("Wrong password")
            msgBox1.setStandardButtons(QMessageBox.Ok)
            msgBox1.exec()
            return False
        else:
            try:
                # Click on Not Now pop-up window
                print("Logged in")
                notNow = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
                print("Not now pop-up clicked")
                time.sleep(2)
                # Click on Notification pop-up window ( NOT NEEDED WHEN RUNING HEADLESS)
                # notifications = WebDriverWait(driver, 10).until(
                #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
                # Click on profile image to get to account page
                image = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
                image.click()
                time.sleep(2.3)
                profile = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]')
                profile.click()
                time.sleep(1.8)
                # Get the account name
                accountName = driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text
                print("Name of the account is:" ,accountName)
                # Create account image name to be saved on pictures directory
                imageName = "pictures/%s.png" % (accountName)
                saveImage(driver,imageName)
                time.sleep(2)
                photo = convertPic(imageName)
                conn = sqlite3.connect("accounts.db")
                c = conn.cursor()
                c.execute("INSERT INTO accounts (accountName, username, password, picture) VALUES (?, ?, ?, ?) ",
                          (accountName, username, password, photo))
                conn.commit()
                c.close()
                conn.close()
                print(accountName, " added successfully")
                return True
            except Exception as e:
                print(e)
class followFollowersObject(QObject):
    finished = pyqtSignal()
    sendTextSignal = pyqtSignal(str)
    def __init__(self,account):
        super().__init__()
        self.account = account
    def startFollowing(self,account):
        print("Run method started")
        trebuie inserata functia login si sa vad cum adaug aici elemente din UI, de incercat cu semnale din ui trimise aici
        self.sendTextSignal.emit(account)
        QApplication.sendPostedEvents()
        print("Finished")
        self.finished.emit()

    # def run(self):
    #     print("Run method started")
    #     account = self.checkSelectedAccount()
    #     if self.checkInputForGetFollowers():
    #         if self.ui.radioButton_HeadlessYes.isChecked():
    #             driver = setupHeadlessDriver()
    #         elif self.ui.radioButton_HeadlessNo.isChecked():
    #             driver = webdriver.Chrome(executable_path="chromedriver.exe")
    #         else:
    #             msgBox1 = QMessageBox()
    #             msgBox1.setIcon(QMessageBox.Information)
    #             msgBox1.setText(
    #                 "Please select if you want to see what the bot is doing or not.")
    #             msgBox1.setWindowTitle("Selection required")
    #             msgBox1.setStandardButtons(QMessageBox.Ok)
    #             msgBox1.exec()
    #             return False
    #         self.ui.targetAccountName_4.setText("Try to log in the ", account[0], " account")
    #         login(driver, account.username, account.password)
    #         print("Logged in")
    #         self.ui.targetAccountName_4.setText("Loged into the ", account[0], " account")
    #         time.sleep(5)
    #         notNow = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    #         print("Not now pop-up clicked")
    #         if self.ui.radioButton_HeadlessNo.isChecked():
    #             notifications = WebDriverWait(driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
    #         numeCont = self.ui.accountNameToGetFollowers.toPlainText()
    #         self.ui.targetAccountName_3.setText("2/5")
    #         self.ui.targetAccountName_4.setText("Navigate to ", numeCont, " page")
    #         goToTargetPage(driver, numeCont)
    #         time.sleep(6)
    #         numberOfFollowers = self.ui.numberOfFollowers.toPlainText()
    #         self.ui.targetAccountName_3.setText("3/5")
    #         self.ui.targetAccountName_4.setText("Opening the followers list of ", numeCont)
    #         openFollowersList(driver)
    #         self.ui.targetAccountName_3.setText("4/5")
    #         self.ui.targetAccountName_4.setText("Scrolling the followers list of ", numeCont)
    #         self.scrollFollowersList(driver)
    #         self.ui.targetAccountName_3.setText("5/5")
    #         self.ui.targetAccountName_4.setText("Starting to follow the accounts from  ", numeCont)
    #         startPushingFollowButton(driver)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())