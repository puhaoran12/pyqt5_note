import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300,100)
        layout=QVBoxLayout

        self.label=QLabel('请选择编程语言')
        self.cb=QComboBox()
        self.cb.addItem('c++')
        self.cb.addItem('python')
        self.cb.addItems(['java','c#','ruby'])

        #self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self,i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        for count in range(self.cb.count()):
            print('item'+str(count)+'='+self.cb.itemText(count))
            print('current index',i,'selection changed',self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
