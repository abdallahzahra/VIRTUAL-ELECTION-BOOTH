
# import lib is used to design gui and requests to get data from  server
from PyQt5 import QtWidgets, QtGui

import requests
from views import view

"""
this class is used to call fun of gui 
"""

class vote (QtWidgets.QMainWindow,view.Ui_MainWindow):
    def __init__(self):
        super(vote,self).__init__()
        self.setupUi(self)
        # that for button sign in  we call fun soon login_fun
        self.sign_ptn.clicked.connect(self.login_fun)
        # that for button send vote we call fun soon sender_voter
        self.send_vote_2.clicked.connect(self.sender_voter)
        # this to select vote used in fun sender_voter
        self.select_vote=""
        self.show()


    def login_fun(self):
        """
        in this function used to insert user and pass to get VID from cla and send ctf
        """
        # when to user insert user name
        user_name = self.line_mail_2.text()
        # when to user insert user password
        user_pass = self.line_pass_2.text()
        # that variable global to use in onther fun (token = vlaidation ID)
        global token
        # that Related requests
        data = {'user_name': user_name, "user_password": user_pass}
        response = requests.post("http://127.0.0.1:8000/get_token/", data=data)
        token = response.text  # this contain the token you ganna use it during the vote

        # that to know is user in database or not to vote
        if token != "user not existed":
            self.stackedWidget.setCurrentWidget(self.page_2)
            return token
        else:
            # if user not in data base we show this massage (Please cheack from username or password .and try again)
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle(" Warnning ")
            msg.setText("Please cheack from username or password .and try again")
            msg.exec_()




    def sender_voter(self):
        """
        this fun used to send VID to ctf
        """
        if self.person_1.isChecked() :
            self.select_vote = "person1"

        elif self.person_2.isChecked() :
            self.select_vote = "person2"

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle(" Warnning ")
            msg.setText(" Please choise option ")
            msg.exec_()

        data = {'token': token, "vote_name": self.select_vote}
        response = requests.post("http://127.0.0.1:7000/vote_for/", data=data)

        application.exit()

application = QtWidgets.QApplication([])
vote_app = vote()
application.exec_()





# pyuic5 forms/form.ui -o views/view.py
