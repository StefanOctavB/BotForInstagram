from PyQt5.QtCore import QThread
import time

class newThread(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __del__(self):
        self.wait()
    def run(self):
        print("RUN")
        time.sleep(10)
        print("DONE")
        # getFollowersUI = uic.loadUi("getFollowers.ui")
        # getFollowersUI.show()