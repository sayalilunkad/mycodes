import sys
# from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import uic
from keystoneclient.v2_0 import client


form_class = uic.loadUiType("login.ui")[0]


class Mainwindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.signin.clicked.connect(self.sign_in)

    def sign_in(self):
        uname = self.username.value()
        passwd = self.password.value()
        url = ''
        client.Client(username=uname, password=passwd, auth_url=url)


app = QtWidgets.QApplication(sys.argv)
mywindow = Mainwindow(None)
mywindow.show()
app.exec_()
