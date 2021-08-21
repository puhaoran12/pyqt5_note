import sys,math
from PyQt5.QtWidgets import *
class GridForm(QWidget):
    def __init__(self):
        super(GridForm,self).__init__()
        self.setWindowTitle('栅格布局:表单设计')

        label1=QLabel('标题:')
        label2=QLabel('作者:')
        label3=QLabel('内容:')

        edit1=QLineEdit()
        edit2=QLineEdit()
        edit3=QTextEdit()

        layout=QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(label1,0,0)
        layout.addWidget(label2,1,0)
        layout.addWidget(label3,2,0)
        layout.addWidget(edit1,0,1)
        layout.addWidget(edit2,1,1)
        layout.addWidget(edit3,2,1,5,1)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GridForm()
    main.show()
    sys.exit(app.exec_())