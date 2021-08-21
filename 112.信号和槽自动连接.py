'''
信号和槽自动连接
槽名必须是：on__objectname__signalname(如on_okButton_clicked)

self.okButton.setObjectName('objectname')
def on__objectname__signalname():
其中objectname必须相同（即19行和31行，21行和 35行）

如self.okButton.setObjectName('okButton')
def on_okButton_clicked(self):
'''
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
import sys
class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot,self).__init__()
        self.okButton=QPushButton('ok',self)
        self.okButton.setObjectName('okButton')#给控件设置一个内部引用的名字（是控件QPushButton的名字，不是okButton的名字）
        self.okButton1=QPushButton('cancel',self)
        self.okButton1.setObjectName('cancelButton')

        layout=QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.okButton1)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)#
        #self.okButton.clicked.connect(self.on_okButton_clicked)#通过connect连接

    @QtCore.pyqtSlot()#标注下面函数是一个槽
    def on_okButton_clicked(self):#槽被@QtCore.pyqtSlot()注释了
        print('点击了ok按钮')

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print('点击了cancel按钮')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoSignalSlot()
    main.show()
    sys.exit(app.exec_())