"""
    Created By Hoss
    - Main

"""



import threading
from PyQt5.QtWidgets import QApplication
#from lib.Practice_client_server.Server import Server
from .commons.window.login_page import Login_window
#from lib.Chatroom import Chatroom
#from lib.Chatroom2 import Chatroom2

#start_server = Server()
#chatroom = Chatroom()
#chatroom2 = Chatroom2()


def start_app():
    """ Starting the GUI application """

    from sys import(
    argv as sys_argv, exit as sys_exit
    )
    q_application = QApplication(sys_argv)
    
    main_window = Login_window()
    main_window.show()

    sys_exit(q_application.exec_())

# Start the server
#def server_starting():
 #   start_server.start_server()

# Starting the app
def main():

#    t1 = threading.Thread(target=server_starting)
    t2 = threading.Thread(target=start_app)
#    t3 = threading.Thread(target=chatroom.receve_msg)
#    t4 = threading.Thread(target=chatroom2.receve_msg)


   # t1.start()
    t2.start()
#    t3.start()
#    t4.start()


if __name__ == "__main__":
    main()