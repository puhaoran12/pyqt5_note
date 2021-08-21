'''
用掩码限制QLineEdit控件的输入
A  ASCII字母字符是必须输入的（a-z，A-Z）
a  ASCII字母字符是允许输入的，但不是必须的（a-z，A-Z）
N  ASCII字母字符必须输入的(a-z，A-Z，0-9)
n  ASCII字母字符是允许输入的，但不是必须的（a-z，A-Z）
X  任何字符都是必须输入的
x  任何字符都是允许输入的，但不是必须的
9  ASCII数字字符是必须输入的（0-9）
0  ASCII数字字符是允许输入的，但不是必须的（0-9）
D  ASCII数字字符是必须输入的（1-9）
d  ASCII数字字符是允许输入的，但不是必须的（1-9）
#  ASCII数字字符或加减符号是允许输入的，但不是必须的
H  十六进制格式字符是必须输入的（A-F，a-f，0-9）
h  十六进制格式字符是允许输入的，但不是必须的（A-F，a-f，0-9）
B  二进制格式字符是必须输入的（0，1）
b  二进制格式字符是允许输入的，但不是必须的（0，1）
>  所有的字母字符都大写
<  所有的字母字符都小写
！  关闭大小写转换
\  使用”\“转义上面列出的字符
'''
from PyQt5.QtWidgets import *
import sys
class QlineEditMask(QWidget):
    def __init__(self):
        super(QlineEditMask,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formLayout=QFormLayout()

        ipLineEdit=QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        #设置掩码
        #192.168.21.45
        ipLineEdit.setInputMask('000.000.000.00;_')#表示没有输入时0表示成下划线
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('mac掩码',macLineEdit)
        formLayout.addRow('日期掩码',dateLineEdit)
        formLayout.addRow('许可证掩码',licenseLineEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlineEditMask()
    main.show()
    sys.exit(app.exec_())





