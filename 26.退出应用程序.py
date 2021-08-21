import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(1000, 1000)
        self.setWindowTitle('退出应用程序')

        # 添加button
        self.button1 = QPushButton('退出应用程序')

        #信号绑定到槽:发送（单击）信号就会执行所对应槽的方法
        self.button1.clicked.connect(lambda: self.onClick_Button())

        # 创建水平布局对象
        layout = QHBoxLayout()
        # 将组件添加到水平布局上
        layout.addWidget(self.button1)

        # 将所有部件都放在mainFrame上
        mainFrame = QWidget()
        # 将layout的内容放在mainFrame上
        mainFrame.setLayout(layout)

        # 将mainFrame放在主窗口上
        self.setCentralWidget(mainFrame)

    # 按钮单击事件(自定义的槽)
    def onClick_Button(self):
        # 通过sender（发件人）方法来获取哪一个组件是发送者
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')

        # 得到一个实例
        app = QApplication.instance()
        # 退出应用程序
        app.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())












































