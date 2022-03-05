"""
    - Main window 
    - giving the user you want to chat with

"""

from PyQt5.QtWidgets import(
    QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QWidget, QHBoxLayout
)

from ...database_handler.Database_handler import DB_function
from ...message_handler.message_handler import Message_box
from ..chatroom.Chatroom import Chatroom
from ..chatroom.Chatroom2 import Chatroom2

database = DB_function()
message = Message_box()

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.main_layout = QVBoxLayout()

        self.__init_ui__()

    
    def __init_ui__(self):
        self.setWindowTitle("Login page")
        self.setAccessibleName("main_window")
        self.setStyleSheet("""
            [accessibleName="main_window"] {
                background-color: None;
                min-width: 700px;
                min-height: 500px;
            }
        """)


        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addStretch(0)
        self.setLayout(self.main_layout)

        self.__first_input__()
        self.Button()

    # username you want to chat with
    def __first_input__(self):

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 150, 0)
        h_layout.addStretch(0)

        q_label = QLabel("Username:")
        q_label.setAccessibleName("lbl_username")
        q_label.setContentsMargins(0, 0, 20, 0)
        q_label.setStyleSheet("""
            [accessibleName="lbl_username"] {
                color: Black;
                font-size: 17px;
                min-height: 50px;
            }
        """)

        self.q_line_edit3 = QLineEdit()
        self.q_line_edit3.setPlaceholderText("username")
        self.q_line_edit3.setContentsMargins(0, 0, 0, 0)
        self.q_line_edit3.setAccessibleName("user_name")
        self.q_line_edit3.setStyleSheet("""
            [accessibleName="user_name"] {
                color: Black;
                min-width: 200px;
                min-height: 30px;
            }
        """)

        h_layout.addWidget(q_label)
        h_layout.addWidget(self.q_line_edit3)

        self.main_layout.addLayout(h_layout)

    def Button(self):
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 10, 250, 200)
        h_layout.addStretch(0)

        q_main_button = QPushButton()
        q_main_button.setText("Start chat")

        def action():
            username = str(self.q_line_edit3.text())
            con = database.db_create()

            Condition = database.db_search(con, username)
            if Condition == True:
                self.close()
                self.win2 = Chatroom2()
                self.win = Chatroom()

                self.win2.show()
                self.win.show()

                self.close()
            if Condition == False:
                message.show_username_not_exist()
        
        q_main_button.clicked.connect(action)

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