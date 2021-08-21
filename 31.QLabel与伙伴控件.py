from PyQt5.QtWidgets import *
import sys


class initUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')#设置窗口的标题

        nameLabel=QLabel('&Name',self)#设置标签name
        nameLineEdit=QLineEdit(self)#放置文本框
        #设置伙伴控件：setBuddy
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel=QLabel('&Password',self)#设置标签password
        passwordLineEidt=QLineEdit(self)#放置文本框
        #设置伙伴控件
        passwordLabel.setBuddy(passwordLineEidt)

        #添加按钮
        btnOK=QPushButton('OK')
        btnCancel=QPushButton('&Cancel')

        #设置标签，文本框，按钮位置坐标，占用位置大小
        mainlayout=QGridLayout(self)#布局类型GridLayout
        mainlayout.addWidget(nameLabel,0,0)#将标签添加到QGridLayout中（用addWidget）
        mainlayout.addWidget(nameLineEdit,0,1,1,2)#将为文本框添加到QGridLayout中

        mainlayout.addWidget(passwordLabel,1,0)
        mainlayout.addWidget(passwordLineEidt,1,1,1,2)

        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = initUI()
    main.show()
    sys.exit(app.exec_())


