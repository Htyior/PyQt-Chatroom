"""
    - Login page

"""


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import(
    QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QWidget, QHBoxLayout
)

from ...database_handler.Database_handler import DB_function
from ...message_handler.message_handler import Message_box
from ..main_window.main_window import Window



message = Message_box()
database = DB_function()

# Creating login page
class Login_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.main_layout = QVBoxLayout()

        self.__init_ui__()

    
    def __init_ui__(self):
        self.setWindowTitle("Login page")
        self.setAccessibleName("main_window")
        self.setStyleSheet("""
            [accessibleName="main_window"] {
                background-image: ("paper.gif");
                min-width: 700px;
                min-height: 500px;
            }
        """)

        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addStretch(0)
        self.setLayout(self.main_layout)

        self.__add_first_input__()
        self.__add_second_input__()
        self.main_button()

    # giving username from user
    def __add_first_input__(self):
        
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 150, 0)
        h_layout.addStretch(0)

        q_label = QLabel("Username:")
        q_label.setAccessibleName("lbl_name1")
        q_label.setContentsMargins(0 , 0, 50, 55)
        q_label.setStyleSheet("""
            [accessibleName="lbl_name1"] {
                color: Black;
                font-size: 17px;
                min-height: 50px;
            }
        """)

        self.q_line_edit1 = QLineEdit()
        self.q_line_edit1.setPlaceholderText("username")
        self.q_line_edit1.setContentsMargins(0, 0, 50, 50)
        self.q_line_edit1.setAccessibleName("user_name")
        self.q_line_edit1.setStyleSheet("""
            [accessibleName="user_name"] {
                color: black;
                min-width: 200px;
                min-height: 30px;
            }
        """)

        h_layout.addWidget(q_label)
        h_layout.addWidget(self.q_line_edit1)

        self.main_layout.addLayout(h_layout)

    # Giving password from user
    def __add_second_input__(self):
        
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 150, 0)
        h_layout.addStretch(0)

        q_label = QLabel("Password:")
        q_label.setAccessibleName("lbl_name2")
        q_label.setContentsMargins(0 , 0, 50, 155)
        q_label.setStyleSheet("""
            [accessibleName="lbl_name2"] {
                color: Black;
                font-size: 17px;
                min-height: 50px;
            }
        """)

        self.q_line_edit2 = QLineEdit()
        self.q_line_edit2.setPlaceholderText("password")
        self.q_line_edit2.setContentsMargins(0, 0, 50, 150)
        self.q_line_edit2.setAccessibleName("password")
        self.q_line_edit2.setStyleSheet("""
            [accessibleName="password"] {
                color: black;
                min-width: 200px;
                min-height: 30px;

            }
        """)

        # Dont show the password
        self.q_line_edit2.setEchoMode(QtWidgets.QLineEdit.Password)

        h_layout.addWidget(q_label)
        h_layout.addWidget(self.q_line_edit2)

        self.main_layout.addLayout(h_layout)

    # Creating the login button 
    def main_button(self):
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 200, 0)
        h_layout.addStretch(0)

        q_main_button = QPushButton()
        q_main_button.setText("Login")

        # Sending the username and paaword to the database and check if its right
        def login_action():
            username = str(self.q_line_edit1.text())
            password = str(self.q_line_edit2.text())
            con = database.db_create()

            # Sending username and password to database
            Condition = database.login_db(con, username, password)
            if Condition == True: # Go to users chatroom
                print(f"{username} loged in successfully")
                self.close()
                self.w = Window()
                self.w.show()
                self.close()
            else:
                # Show login error message
                print("login failed")
                
                message.show_login_error_messagebox()

        q_main_button.clicked.connect(login_action)

        q_main_button.setAccessibleName("button")
        q_main_button.setStyleSheet("""
            [accessibleName="button"] {
        background-color: #c2fbd7;
        border-radius: 100px;
        box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset,rgba(44, 187, 99, .15) 0 1px 2px,rgba(44, 187, 99, .15) 0 2px 4px,rgba(44, 187, 99, .15) 0 4px 8px,rgba(44, 187, 99, .15) 0 8px 16px,rgba(44, 187, 99, .15) 0 16px 32px;
        color: green;
        cursor: pointer;
        display: inline-block;
        font-family: CerebriSans-Regular,-apple-system,system-ui,Roboto,sans-serif;
        padding: 7px 20px;
        text-align: center;
        text-decoration: none;
        transition: all 250ms;
        border: 0;
        font-size: 16px;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
            }
        """)

        h_layout.addWidget(q_main_button)

        self.main_layout.addLayout(h_layout)

