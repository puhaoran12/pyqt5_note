from PyQt5.QtWidgets import *
import sys
class QSSSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSS样式')
        btn1=QPushButton(self)
        btn1.setText("按钮1")
        btn2=QPushButton(self)
        btn2.setProperty('name','btn2')#给按钮2添加一个属性；name为key，btn2为value
        btn2.setText('按钮2')

        layout=QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.setLayout(layout)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        main = QSSSelector()
        #选择器
        qssStyle='''
            QPushButton[name=btn2]{
            background-color:green;
            color:red;
            height:60;
            font-sise:100px;
            }
        '''
        main.setStyleSheet(qssStyle)#当前窗口全局有效
        main.show()
        sys.exit(app.exec_())