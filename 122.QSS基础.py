'''
QSS基础
QSS(Qt Style Sheets)
QT样式表
用于设置控件样式
'''
from PyQt5.QtWidgets import *
import sys
class BasicQSS(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSS样式')
        btn1=QPushButton(self)
        btn1.setText("按钮1")
        btn2=QPushButton(self)
        btn2.setText('按钮2')

        layout=QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.setLayout(layout)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = BasicQSS()
        #选择器
        qssStyle='''
            QPushButton{
            background-color:green
            }
        '''
        main.setStyleSheet(qssStyle)#当前窗口全局有效
        main.show()
        sys.exit(app.exec_())