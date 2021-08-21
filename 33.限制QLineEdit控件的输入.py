'''
限制QLineEdit控件的输入（校验器）
如限制只能输入整数，浮点数或满足一定条件的字符串

'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('限制QLineEdit控件的输入')
        #创建表单布局
        formLayout=QFormLayout()
        #创建文本输入框
        intLineEdit=QLineEdit()
        doubleLineEdit=QLineEdit()
        validatorLineEdit=QLineEdit()

        #将文本框加入布局中
        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点类型',doubleLineEdit)
        formLayout.addRow('数字和字母',validatorLineEdit)

        intLineEdit.setPlaceholderText('整数类型')
        doubleLineEdit.setPlaceholderText('浮点类型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        #校验器：Validator
        #整数校验器[1,99]
        intValidator=QIntValidator(self)
        intValidator.setRange(1,99)
        #浮点校验器[-360,360],精度：小数点后两位
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度，小数点两位
        doubleValidator.setDecimals(2)
        #字符和数字
        reg=QRegExp('[a-zA-Z0-9]+$')
        validator=QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器：将三个校验器与三个文本框绑定
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)


        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
