import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Menu(QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        bar=self.menuBar()#获取菜单栏

        file=bar.addMenu('文件')#添加菜单栏选项
        file.addAction('新建')#添加动作；动作即为子菜单

        save=QAction('保存',self)
        save.setShortcut('Ctrl+s')#创建快捷键
        file.addAction(save)#添加动作

        save.triggered.connect(self.process)

        edit=bar.addMenu('Edit')#添加菜单栏选项
        edit.addAction('copy')
        edit.addAction('paste')
        quit=QAction('退出',self)
        file.addAction(quit)


    def process(self,a):
        print(self.sender().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())