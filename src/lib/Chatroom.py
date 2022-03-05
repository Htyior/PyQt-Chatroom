"""
    - Chatroom page client 1

"""

from PyQt5.QtWidgets import(
    QVBoxLayout, QLineEdit,
    QWidget, QHBoxLayout, 
    QPlainTextEdit
)

msg = ""

class Chatroom(QWidget):
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

        self.show_message()
        self.message_section()

    # show message section
    def show_message(self):
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 10, 10)
        h_layout.addStretch(0)



        self.editor = QPlainTextEdit()
        self.editor.setReadOnly(True)
        self.editor.setContentsMargins(0, 0, 0, 0)
        self.editor.setGeometry(0, 0, 0, 0)

        h_layout.addWidget(self.editor)
        self.main_layout.addLayout(h_layout)


    # Writing the message
    def message_section(self):
        
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 250, 0)
        h_layout.addStretch(0)

        self.q_line_edit1 = QLineEdit()
        self.q_line_edit1.setPlaceholderText("message")
        self.q_line_edit1.setContentsMargins(0, 0, 0, 0)
        self.q_line_edit1.setAccessibleName("user_name")
        self.q_line_edit1.setStyleSheet("""
            [accessibleName="user_name"] {
                color: black;
                min-width: 200px;
                min-height: 30px;
            }
        """)



        self.q_line_edit1.returnPressed.connect(lambda: show_msg())

        def show_msg():
            self.value = self.q_line_edit1.text()
            # make the input section clear after sending message
            self.q_line_edit1.setText("")

            # Check if the message box is empty do nothing
            if self.value == "":
            
                pass
            else:
            
                # send the message to show_message function and print it in output section
                self.editor.insertPlainText("You: " + self.value + "\n")
            
                # send message to client file for sending to other client

            

        h_layout.addWidget(self.q_line_edit1)
        self.main_layout.addLayout(h_layout)
