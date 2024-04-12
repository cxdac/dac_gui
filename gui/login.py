import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

# 登录窗口
class LoginWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('登录界面')
        self.setGeometry(100, 100, 280, 150)

        # 创建布局
        layout = QVBoxLayout()

        # 创建用户名和密码的标签和输入框
        self.username_label = QLabel('用户名:')
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('密码:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # 创建登录按钮，并连接到登录槽函数
        login_button = QPushButton('登录')
        login_button.clicked.connect(self.check_login)

        # 添加小部件到布局
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        # 设置中心小部件及其布局
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def check_login(self):
        # 这里应该有更复杂的登录验证逻辑
        username = self.username_input.text()
        password = self.password_input.text()
        if username == 'admin' and password == 'password':
            self.main_window.show()
            self.hide()
        else:
            # 登录失败的处理
            print("登录失败")

# 主窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('主界面')
        self.setGeometry(100, 100, 400, 400)

        # 主界面的内容可以根据需要添加

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建主窗口和登录窗口
    main_window = MainWindow()
    login_window = LoginWindow(main_window)

    # 显示登录窗口
    login_window.show()

    sys.exit(app.exec_())
