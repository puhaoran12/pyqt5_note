import sys
from PyQt5.QtWidgets import QMainWindow,QApplication#QMainwindow和QApplication这两个是必须的，任何界面编程都需要窗口和应用程序
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        #设置主窗口
        self.setWindowTitle('第一个主窗口')
        #设置窗口尺寸
        self.resize(300,300)
        #获得状态栏
        status=self.statusBar()
        #显示状态栏信息
        status.showMessage('只显示五秒的消息',5000)


if __name__ == "__main__":                  #当运行本文件时运行以下内容
    app = QApplication(sys.argv)            #建立QApplication对象并且放入系统传入参数
    Window = FirstMainWin()                   #建立MainWindow对象
    Window.show()                           #展示MainWindo对象内容
    sys.exit(app.exec_())                   #进入app.exec_事件循环当退出循环后系统整体退出


