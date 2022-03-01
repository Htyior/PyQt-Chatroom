import threading
from PyQt5.QtWidgets import QApplication
from lib.Practice_client_server.Server import Server
from lib.Login import Login_window

start_server = Server()

def server_starting():
    start_server.start_server()

def start_app():
    from sys import(
    argv as sys_argv, exit as sys_exit
    )
    q_application = QApplication(sys_argv)
    
    main_window = Login_window()
    main_window.show()

    sys_exit(q_application.exec_())



def main():

    t1 = threading.Thread(target=server_starting)
    t2 = threading.Thread(target=start_app)

    
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()