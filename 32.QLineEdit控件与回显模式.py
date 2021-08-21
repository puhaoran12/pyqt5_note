'''
QLineEdit控件与回显模式
基本功能：输入单行的文本
设置回显模式：四种回显模式
1.normal正常模式：输入一个字符，就会在文本框中显示出来
2.noecho不回显：输入内容（密码）屏幕上没有显现（将输入内容已经提交给计算机了）
3.password：输入字符，回显的不是输入内容，而是一个.或者*（防止别人看到）
4.PasswordEcho0nedit：刚输入内容是可见的（回显），过一会儿就变成。或*（password）


'''


from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout=QFormLayout()#创建布局类型

        normalLineEdit=QLineEdit()#创建文本输入框
        noEcholLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnLineEdit = QLineEdit()


        formLayout.addRow('Normal',normalLineEdit)#将文本框添加到布局中   （标签，控件）
        formLayout.addRow('NoEcho', noEcholLineEdit)
        formLayout.addRow('password', passwordLineEdit)
        formLayout.addRow('PasswoedEchoOnEdit', passwordEchoOnLineEdit)

        #placeholdertext:在文本输入框没有输入内容是显示事先编写好的内容，当文本框中输入内容时内容消失
        normalLineEdit.setPlaceholderText('Normal')
        noEcholLineEdit.setPlaceholderText('noEcho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnLineEdit.setPlaceholderText('PasswordEchoOnEdit')
        #设置模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEcholLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
