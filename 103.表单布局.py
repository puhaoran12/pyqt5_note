'''
表单布局：QFormLayout
'''
import sys,math
from PyQt5.QtWidgets import *
class FormForm(QWidget):
    def __init__(self):
        super(FormForm,self).__init__()
        self.setWindowTitle('表单布局')
        self.resize(350,300)

        layout=QFormLayout()

        label1=QLabel('标题:')
        label2=QLabel('作者:')
        label3=QLabel('内容:')

        edit1=QLineEdit()
        edit2=QLineEdit()
        edit3=QTextEdit()

        layout.addRow(label1,edit1)
        layout.addRow(label2,edit2)
        layout.addRow(label3, edit3)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormForm()
    main.show()
    sys.exit(app.exec_())