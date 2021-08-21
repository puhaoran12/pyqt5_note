from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
class QLineEditdemo(QWidget):
    def __init__(self):
        super(QLineEditdemo,self).__init__()
        self.initUI()

    def initUI(self):
        edit1=QLineEdit()
        #使用int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)#不超过9999（四位数字）
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))

        edit2=QLineEdit()
        #使用double校验器
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))

        #掩码
        edit3=QLineEdit()
        edit3.setInputMask('99_9999_999999;_')

        edit4=QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5=QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6=QLineEdit('hello PyQt5')
        edit6.setReadOnly(True)

        formLayout=QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验',edit2)
        formLayout.addRow('Input mask',edit3)
        formLayout.addRow('文本变化',edit4)
        formLayout.addRow('密码',edit5)
        formLayout.addRow('只读',edit6)
        self.setWindowTitle('综合案例')

        self.setLayout(formLayout)

    def textChanged(self,text):
        print('输入内容：'+text)
    def enterPress(self):
        print('已输入值')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditdemo()
    main.show()
    sys.exit(app.exec_())