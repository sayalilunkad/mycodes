import sys

from keystoneclient.v2_0 import client
from PyQt5 import QtWidgets
from PyQt5 import uic


form1, base1 = uic.loadUiType("login.ui")
form2, base2 = uic.loadUiType("overview.ui")


class OverviewTab(base2, form2):
    def __init__(self):
        super(base2, self).__init__()
        self.setupUi(self)


class LoginWindow(QtWidgets.QMainWindow, base1, form1):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.signin.clicked.connect(self.sign_in)

    def sign_in(self):
        global ui_2
        uname = "admin"
        passwd = "admin_pass"
        tenant = 'admin'
        url = 'http://192.168.100.51:5000/v2.0'
        keystone = client.Client(username=uname, password=passwd,
                                 tenant_name=tenant, auth_url=url)
        if keystone.authenticate() is True:
            ui_2 = OverviewTab()
            ui_2.show()
            self.close()
        else:
            self.show()

app = QtWidgets.QApplication(sys.argv)
global ui_1
ui_1 = LoginWindow(None)
ui_1.show()
app.exec_()
