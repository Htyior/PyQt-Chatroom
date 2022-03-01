import sys
from PyQt5.QtWidgets import QMessageBox, QWidget


"""
Type of messages:

- QMessageBox.Ok
- QMessageBox.Open
- QMessageBox.Save
- QMessageBox.Cancel
- QMessageBox.Close
- QMessageBox.Yes
- QMessageBox.No
- QMessageBox.Abort
- QMessageBox.Retry
- QMessageBox.Ignore

"""





class Message_box(QWidget):
    def __init__(self):
        pass

    def show_login_error_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
    
        # Setting message for message box
        msg.setText("Username or password in not valid")
    
        # setting window title
        msg.setWindowTitle("Login")
    
        # declaring buttons on window Box
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()


    def show_login_input_is_empty(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        # Setting message for message box
        msg.setText("Please fill username and password")

        # setting window title
        msg.setWindowTitle("Warning")

        # declaring buttons on window Box
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()
    
    def show_username_not_exist(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Username in not exist")

        msg.setWindowTitle("Warning")

        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()